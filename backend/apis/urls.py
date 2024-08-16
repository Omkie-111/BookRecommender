from django.urls import path
from .api_views import (
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
    path("signup/", UserSignupView.as_view(), name="api-signup"),
    path("login/", UserLoginView.as_view(), name="api-login"),
    path("search/", BookSearchView.as_view(), name="api-search"),
    path(
        "recommendations/",
        RecommendationListCreateView.as_view(),
        name="api-recommendation",
    ),
    path(
        "recommendations/<int:pk>/",
        RecommendationDetailView.as_view(),
        name="api-recommendation-details",
    ),
    path(
        "recommendations/<int:pk>/like/",
        LikeRecommendationView.as_view(),
        name="api-like",
    ),
    path(
        "recommendations/<int:pk>/comments/",
        AddCommentView.as_view(),
        name="api-add-comment",
    ),
    path(
        "recommendations/<int:pk>/comments/<int:comment_id>/",
        RemoveCommentView.as_view(),
        name="api-remove-comment",
    ),
]
