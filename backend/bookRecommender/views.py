from django.shortcuts import render


def search(request):
    return render(request, "search.html")


def recommendation_details(request):
    return render(request, "all_recommendations.html")


def get_recommendation(request, pk):
    return render(request, "recommend.html")


def signup(request):
    return render(request, "signup.html")


def login(request):
    return render(request, "login.html")


def create_recommendation(request):
    return render(request, "create_recommendations.html")
