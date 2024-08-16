from django.urls import path
from .html_views import (
    search,
    get_recommendation,
    recommendation_details,
    login,
    signup,
    create_recommendation,
)

urlpatterns = [
    path("", search, name="search"),
    path("recommendation_details", recommendation_details, name="recommendations-list"),
    path("recommends/<int:pk>/", get_recommendation, name="recommends"),
    path("login/", login, name="login"),
    path("signup/", signup, name="signup"),
    path(
        "create-recommendations/", create_recommendation, name="create-recommendation"
    ),
]
