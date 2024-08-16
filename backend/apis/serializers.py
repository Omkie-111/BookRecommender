from rest_framework import serializers
from django.contrib.auth.models import User
from bookRecommender.models import Book, Recommendation, Like, Comment
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data["username"], password=data["password"])
        if not user:
            raise serializers.ValidationError("Invalid login credentials")
        refresh = RefreshToken.for_user(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]


class RecommendationSerializer(serializers.ModelSerializer):
    book = BookSerializer()  # Nested serializer to include book details
    # user = UserSerializer()
    total_likes = serializers.SerializerMethodField()
    all_comments = serializers.SerializerMethodField()

    class Meta:
        model = Recommendation
        fields = ["book", "comments", "id", "total_likes", "all_comments"]

    def get_total_likes(self, obj):
        return obj.like_set.count()

    def get_all_comments(self, obj):
        comments = obj.comment_set.all()
        return CommentSerializer(comments, many=True).data

    def to_representation(self, instance):
        # Custom method to handle data processing and representation
        representation = super().to_representation(instance)

        # Adding detailed book information
        book_data = BookSerializer(instance.book).data
        representation["book_details"] = book_data
        user = instance.user.username
        representation["user"] = str(user)

        return representation

    def filter_and_sort(self, recommendations, filters):
        # Apply filtering based on the provided filters
        genre = filters.get("genre")
        if genre:
            recommendations = recommendations.filter(book__genre=genre)

        min_rating = filters.get("min_rating")
        if min_rating:
            recommendations = recommendations.filter(book__rating__gte=min_rating)

        publication_date = filters.get("publication_date")
        if publication_date:
            recommendations = recommendations.filter(
                book__publication_date=publication_date
            )

        # Sorting by rating or publication date if requested
        sort_by = filters.get("sort_by")
        if sort_by in ["rating", "-rating", "publication_date", "-publication_date"]:
            recommendations = recommendations.order_by(sort_by)

        return recommendations

    def create(self, validated_data):
        book_data = validated_data.pop("book")
        book, created = Book.objects.get_or_create(**book_data)
        recommendation = Recommendation.objects.create(book=book, **validated_data)
        return recommendation


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"

    def create(self, validated_data):
        like, created = Like.objects.get_or_create(
            user=validated_data["user"], recommendation=validated_data["recommendation"]
        )
        return like


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "text", "created_at", "user", "recommendation"]
        read_only_fields = ["user", "recommendation"]
