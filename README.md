# Book Recommendation Platform

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

### Running Tests

To run tests, use the following command:
```bash
python manage.py test
```

## Html API Endpoints

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
