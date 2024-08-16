from django.urls import path
from .frontend_views import (
    search,
    get_recommendation,
    recommendation_details,
    login,
    signup,
    create_recommendation,
)

urlpatterns = [
    path("", search, name="search"),
    path("recommendation_details", recommendation_details, name="recommend-form"),
    path("recommends/<int:pk>/", get_recommendation, name="recommends"),
    path("login/", login, name="login"),
    path("signup/", signup, name="signup"),
    path(
        "create-recommendations/", create_recommendation, name="create-recommendation"
    ),
]
