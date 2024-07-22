# Blog API By Elijah Ekpen Mensah

## Overview
This is a simple blog application built with Flask that provides RESTful endpoints for managing blog posts. The application also includes Swagger UI for API documentation.

## Setup

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd blog_app
    ```

2. Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python app.py
    ```

5. Open your browser and navigate to `http://127.0.0.1:5000/api/docs` to view the API documentation.

## Endpoints

- **GET /posts**: Get all posts.
- **GET /posts/{post_id}**: Get post details.
- **POST /posts/{post_id}**: Create a new post.
- **PUT /posts/{post_id}**: Update a post.
- **DELETE /posts/{post_id}**: Delete a post.
