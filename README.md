# Book Recommendation Platform

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
   - [Integration with Google Books API](#integration-with-google-books-api)
   - [Community Book Recommendations](#community-book-recommendations)
   - [API Creation Guide](#api-creation-guide)
3. [Project Structure](#project-structure)
   - [Key Components](#key-components)
4. [Setup Instructions](#setup-instructions)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
5. [HTML API Endpoints](#html-api-endpoints)
   - [Fetching Books from Google Books API](#fetching-books-from-google-books-api)
   - [Submitting Book Recommendations](#submitting-book-recommendations)
   - [Filtering and Sorting Recommendations](#filtering-and-sorting-recommendations)
6. [API Endpoints](#api-endpoints)
   - [User Signup](#user-signup-signup)
   - [User Login](#user-login-login)
   - [Book Search](#book-search-search)
   - [List/Create Recommendations](#listcreate-recommendations-recommendations)
   - [Recommendation Details](#recommendation-details-recommendationsintpk)
   - [Like Recommendation](#like-recommendation-recommendationsintpklike)
   - [Add Comment](#add-comment-recommendationsintpkcomments)
   - [Remove Comment](#remove-comment-recommendationsintpkcommentsintcommentid)
7. [Custom API Creation Guide](#custom-api-creation-guide)
   - [Setting Up Django](#setting-up-django)
   - [Defining Models](#defining-models)
   - [Creating Serializers](#creating-serializers)
   - [Writing Views](#writing-views)
   - [URL Routing](#url-routing)
   - [Best Practices](#best-practices)
8. [Frontend Integration](#frontend-integration)
   - [HTML & JavaScript](#html--javascript)
9. [Conclusion](#conclusion)

## Overview

This project is a backend application designed as a central hub for a community-driven platform focused on sharing and exploring book recommendations. The application integrates with the Google Books API to fetch book data and offers features for users to submit, filter, and explore book recommendations. Additionally, it includes an API creation guide to help developers create custom book-related functionalities.

## Features

1. **Integration with Google Books API:**
   - Fetch book data including title, author, description, cover image, and ratings.
   - Search books based on keywords, authors, or categories.
   - Error handling for API requests and responses.

2. **Community Book Recommendations:**
   - Users can submit book recommendations.
   - API endpoints to manage book entries, retrieve recommended books, and handle user interactions (likes, comments).
   - Filter and sort recommendations based on genre, rating, and publication date.

3. **API Creation Guide:**
   - A comprehensive guide for developers on creating custom API endpoints.
   - Includes topics on setting up Django, defining models, serializers, views, and URL routing.
   - Examples of CRUD operations, authentication, and data validation.

## Project Structure

```
backend/
├── apis/
│   ├── __init__.py
│   ├── apps.py
│   ├── serializers.py
│   ├── urls.py
│   └── api_views.py
├── backend/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── bookRecommender/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── html_views.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── utils.py
├── manage.py
└── db.sqlite3
```

### Key Components

- **models.py:** Defines the database schema using Django ORM, including the `Book` and `Recommendation` models.
- **serializers.py:** Handles data serialization and deserialization, crucial for converting complex data types (like querysets) into JSON.
- **api_views.py:** Contains the logic for handling HTTP requests and returning appropriate responses. Implements functionalities such as fetching book data, filtering recommendations, and processing user input.
- **html_views.py:** Contains logic for managing html templates.
- **urls.py:** Maps URLs to the corresponding views, defining the API's endpoints.

## Setup Instructions

### Prerequisites

- Python 3.x
- Django 3.x or later
- Django REST Framework
- An API key from Google Books API

### Installation

1. **Create Virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
   
2. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd backend
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

### HTML API endpoints

Here's a brief documentation for each of the provided URLs, explaining their purpose and usage:

1. **Search (`"/books/"`)**
   - **Endpoint:** `""` (root path)
   - **Usage:** This endpoint serves as the search page. It is typically used to render a book search form.

2. **Signup (`"/books/signup/"`)**
   - **Endpoint:** `"signup/"`
   - **Usage:** This endpoint is for user registration. It directs users to a signup page where they can create a new account by providing the necessary information.

3. **Login (`"/books/login/"`)**
   - **Endpoint:** `"login/"`
   - **Usage:** This endpoint is used for user authentication. It directs users to a login page where they can enter their credentials to access their accounts.

4. **Get Recommendation (`"/books/recommends/<int:pk>/"`)**
   - **Endpoint:** `"recommends/<int:pk>/"`
   - **Usage:** This endpoint is used to retrieve details of a specific recommendation based on its primary key (`pk`).

5. **Recommendation Details (`"/books/recommendation_details"`)**
   - **Endpoint:** `"recommendation_details"`
   - **Usage:** This endpoint is used to display a list of recommendations. It likely returns a page with a summary or detailed list of all recommendations stored in the system.

6. **Create Recommendation (`"/books/create-recommendations/"`)**
   - **Endpoint:** `"create-recommendations/"`
   - **Usage:** This endpoint allows users to create new recommendations. It likely presents a form for users to fill in details and submit a new recommendation to be stored in the system.

These URLs represent different functionalities in the application, allowing users to search, view recommendations, authenticate, and manage their accounts.

## Example Html API Endpoints

### Fetching Books from Google Books API

- **Endpoint:** `/books/search`
- **Method:** `GET`
- **Parameters:**
  - `q`: Search query (e.g., title, author)
- **Response:** List of books matching the query

### Submitting Book Recommendations

- **Endpoint:** `/books/recommendations/`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
      "book": {
          "title": "Example Book",
          "author": "Author Name",
          "genre": "Fiction",
          "rating": 4.5,
          "publication_date": 2024-08-10
      },
      "comments": "This is a great book!"
  }
  ```
- **Response:** Details of the submitted recommendation

### Filtering and Sorting Recommendations

- **Endpoint:** `/books/recommendations/`
- **Method:** `GET`
- **Parameters:**
  - `genre`: Filter by genre
  - `min_rating`: Filter by minimum rating
  - `publication_date`: Filter by publication date
  - `sort_by`: Sort results (e.g., `rating`, `-rating`, `publication_date`, `-publication_date`)

### API Endpoints

Here’s a concise documentation for each endpoint, focusing on the endpoint URL and its usage:

1. **User Signup (`"signup/"`)**
   - **Endpoint:** `"signup/"`
   - **Usage:** Allows users to register for a new account using the `UserSignupView`. This is typically used to create a new user account.

2. **User Login (`"login/"`)**
   - **Endpoint:** `"login/"`
   - **Usage:** Authenticates users and provides access to their account using the `UserLoginView`. This is used for logging into an existing account.

3. **Book Search (`"search/"`)**
   - **Endpoint:** `"search/"`
   - **Usage:** Allows users to search for books using the `BookSearchView`. This endpoint is typically used to filter and retrieve book data based on search criteria.

4. **List/Create Recommendations (`"recommendations/"`)**
   - **Endpoint:** `"recommendations/"`
   - **Usage:** Displays a list of recommendations or allows users to create a new recommendation using the `RecommendationListCreateView`. It’s used to manage recommendation data.

5. **Recommendation Details (`"recommendations/<int:pk>/"`)**
   - **Endpoint:** `"recommendations/<int:pk>/"`
   - **Usage:** Retrieves, updates, or deletes a specific recommendation based on its primary key (`pk`) using the `RecommendationDetailView`. It’s used for detailed management of a single recommendation.

6. **Like Recommendation (`"recommendations/<int:pk>/like/"`)**
   - **Endpoint:** `"recommendations/<int:pk>/like/"`
   - **Usage:** Allows users to like a specific recommendation using the `LikeRecommendationView`. It’s used to express approval or support for a recommendation.

7. **Add Comment (`"recommendations/<int:pk>/comments/"`)**
   - **Endpoint:** `"recommendations/<int:pk>/comments/"`
   - **Usage:** Allows users to add a comment to a specific recommendation using the `AddCommentView`. It’s used to contribute feedback or opinions on a recommendation.

8. **Remove Comment (`"recommendations/<int:pk>/comments/<int:comment_id>/`")**
   - **Endpoint:** `"recommendations/<int:pk>/comments/<int:comment_id>/"`
   - **Usage:** Allows users to remove a specific comment from a recommendation using the `RemoveCommentView`. It’s used to delete feedback or opinions previously provided.

These endpoints represent different API actions, providing users with functionalities for user management, searching, interacting with recommendations, and handling comments.

### Example API Request

```bash
curl -X GET "http://localhost:8000/recommendations/?genre=Fiction&min_rating=4"
```

## Custom API Creation Guide

1. **Setting Up Django:**
   - Ensure Django and Django REST Framework are installed.
   - Create a Django project and app.

2. **Defining Models:**
   - Define your models in `models.py`. Use Django's ORM to represent your database schema.

3. **Creating Serializers:**
   - Use Django REST Framework's `serializers` to manage the conversion of data between JSON and Python objects.

4. **Writing Views:**
   - Implement your views in `views.py` to handle different HTTP methods (GET, POST, etc.).

5. **URL Routing:**
   - Map your views to URLs in `urls.py`.

6. **Best Practices:**
   - Implement authentication using Django's built-in mechanisms or JWT.
   - Use pagination for large datasets.
   - Handle errors gracefully.

## Frontend Integration

### HTML & JavaScript

- **Real-time Search Suggestions:** Implemented using on change event API call with a debounce to query the backend as the user types and avoid excessive calls.
- **Dynamic Filtering Options:** Filters such as genre, rating, and publication date can be adjusted dynamically without page reloads.
- **User Authentication:** JWT-based authentication with session management to personalize recommendations.

## Conclusion

This project serves as a comprehensive backend solution for a community-driven book recommendation platform. It integrates with external APIs, offers robust data handling, and provides a guide for developers to extend its functionality. The frontend integration enhances user interaction, making the platform dynamic and engaging.
