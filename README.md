# Blogging Platform API

This is a RESTful API for a blogging platform, built with FastAPI, designed to manage blog posts. It provides a full set of functionalities for creating, reading, updating, and deleting blog posts.

## Features

-   **Create** a new blog post
-   **Read** a single blog post or a list of all posts
-   **Update** an existing blog post
-   **Delete** an existing blog post

## Installation

### Prerequisites

-   Python 3.8+
-   `pip` (Python package installer)

### Setup

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd <your-repository-directory>
    ```

2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    -   **On macOS and Linux:**
        ```bash
        source venv/bin/activate
        ```
    -   **On Windows:**
        ```bash
        venv\Scripts\activate
        ```

4.  **Install dependencies:**
    The project uses a `requirements.txt` file to manage its dependencies.
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the API

You can run the API server using :
```bash
fastapi app/main.py

https://roadmap.sh/projects/blogging-platform-api
