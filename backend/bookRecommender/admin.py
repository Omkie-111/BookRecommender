from django.contrib import admin
from .models import Book, Recommendation, Like, Comment


class BookAdmin(admin.ModelAdmin):

    list_display = ["id", "title", "author", "rating", "publication_date"]
    list_filter = ["id", "title", "author", "rating", "publication_date"]


admin.site.register(Book, BookAdmin)


class RecommendationAdmin(admin.ModelAdmin):

    list_display = ["id", "book", "user", "comments", "created_at"]
    list_filter = ["id", "book", "user", "comments", "created_at"]


admin.site.register(Recommendation, RecommendationAdmin)


class LikeAdmin(admin.ModelAdmin):

    list_display = ["id", "recommendation", "user", "created_at"]
    list_filter = ["id", "recommendation", "user", "created_at"]


admin.site.register(Like, LikeAdmin)


class CommentAdmin(admin.ModelAdmin):

    list_display = ["id", "recommendation", "user", "text", "created_at"]
    list_filter = ["id", "recommendation", "user", "text", "created_at"]


admin.site.register(Comment, CommentAdmin)
