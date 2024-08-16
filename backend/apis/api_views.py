from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from bookRecommender.utils import fetch_books
from bookRecommender.models import Recommendation, Like, Comment
from apis.serializers import (
    RecommendationSerializer,
    LikeSerializer,
    UserSignupSerializer,
    UserLoginSerializer,
    CommentSerializer,
)


class UserSignupView(generics.CreateAPIView):
    serializer_class = UserSignupSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class BookSearchView(APIView):
    def get(self, request):
        query = request.GET.get("q")
        books = fetch_books(query)
        if books:
            return Response(books)
        return Response({"error": "No books found"}, status=404)


class RecommendationListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        recommendations = Recommendation.objects.all()

        serializer = RecommendationSerializer()
        filtered_recommendations = serializer.filter_and_sort(
            recommendations, request.GET
        )

        data = RecommendationSerializer(filtered_recommendations, many=True).data
        return Response(data)

    def post(self, request):
        serializer = RecommendationSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecommendationDetailView(APIView):
    def get(self, request, pk):
        try:
            recommendation = Recommendation.objects.get(pk=pk)
            serializer = RecommendationSerializer(recommendation)
            return Response(serializer.data)
        except Recommendation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            recommendation = Recommendation.objects.get(pk=pk)
            recommendation.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Recommendation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class LikeRecommendationView(APIView):
    def post(self, request, pk):
        recommendation = get_object_or_404(Recommendation, pk=pk)
        user = request.user

        # Check if the user has already liked this recommendation
        if Like.objects.filter(user=user, recommendation=recommendation).exists():
            return Response(
                {"detail": "You have already liked this recommendation."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = LikeSerializer(
            data={"user": user.id, "recommendation": recommendation.id}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        recommendation = get_object_or_404(Recommendation, pk=pk)
        user = request.user

        like = Like.objects.filter(user=user, recommendation=recommendation).first()
        if like:
            like.delete()
            return Response(
                {"detail": "Like removed."}, status=status.HTTP_204_NO_CONTENT
            )
        else:
            return Response(
                {"detail": "Like not found."}, status=status.HTTP_404_NOT_FOUND
            )


class AddCommentView(APIView):
    def post(self, request, pk):
        recommendation = Recommendation.objects.get(pk=pk)
        data = {
            "user": request.user.id,
            "recommendation": recommendation.id,
            "text": request.data.get("text"),
        }
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user, recommendation=recommendation)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RemoveCommentView(APIView):
    def delete(self, request, pk, comment_id):
        try:
            comment = Comment.objects.get(
                pk=comment_id, recommendation__id=pk, user=request.user
            )
            comment.delete()
            return Response(
                {"detail": "Comment removed"}, status=status.HTTP_204_NO_CONTENT
            )
        except Comment.DoesNotExist:
            return Response(
                {
                    "detail": "Comment not found or you don't have permission to delete it"
                },
                status=status.HTTP_404_NOT_FOUND,
            )
