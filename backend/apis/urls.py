from django.urls import path
from .views import (
    UserSignupView,
    UserLoginView,
    BookSearchView,
    RecommendationDetailView,
    RecommendationListCreateView,
    LikeRecommendationView,
    AddCommentView,
    RemoveCommentView,
)

urlpatterns = [
    path("signup/", UserSignupView.as_view(), name="user-signup"),
    path("login/", UserLoginView.as_view(), name="user-login"),
    path("search/", BookSearchView.as_view(), name="search"),
    path(
        "recommendations/",
        RecommendationListCreateView.as_view(),
        name="recommendation-list-create",
    ),
    path(
        "recommendations/<int:pk>/",
        RecommendationDetailView.as_view(),
        name="recommendation-detail",
    ),
    path(
        "recommendations/<int:pk>/like/",
        LikeRecommendationView.as_view(),
        name="like-recommendation",
    ),
    path(
        "recommendations/<int:pk>/comments/",
        AddCommentView.as_view(),
        name="add-comment",
    ),
    path(
        "recommendations/<int:pk>/comments/<int:comment_id>/",
        RemoveCommentView.as_view(),
        name="remove-comment",
    ),
]
