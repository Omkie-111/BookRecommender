import requests


def fetch_books(query):
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {"q": query}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        books_data = response.json().get("items", [])
        books = []
        for item in books_data:
            volume_info = item.get("volumeInfo", {})
            book = {
                "title": volume_info.get("title"),
                "author": ", ".join(volume_info.get("authors", [])),
                "description": volume_info.get("description"),
                "cover_image": volume_info.get("imageLinks", {}).get("thumbnail"),
                "ratings": volume_info.get("averageRating"),
                "publish_date": volume_info.get("publishedDate"),
            }
            books.append(book)
        return {"totalBooks": len(books), "books": books}
    else:
        return {"error": "Unable to fetch data"}
