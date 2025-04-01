## 📌 Project Description
This API scrapes the Instagram account https://www.instagram.com/nasa/ every 10 minutes, fetching the last 10 posts.
It also analyzes the text and predicts which city is mentioned in the content.

## ⚡ Quick Start

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/hikehikehike/instagram-parser.git
```

### 2️⃣ Ensure Docker is Installed
Check if Docker is installed:
```bash
docker --version
```
If not, download it from the [official website](https://www.docker.com/).

### 3️⃣ Build and Start the Containers

```bash
docker-compose up --build
```
This will:
* 	Build the necessary images.
* 	Start the FastAPI application.
* 	Start a PostgreSQL database.
*   Start a redis.
*   Start a celery_worker.
*   Start a celery_beat.
*   Start a test.

### 4️⃣ Access the API

You need to open the detect_city_service file and insert your API token there (you can get it here: https://huggingface.co/docs/hub/security-tokens).

Once running, open:

http://127.0.0.1:8000/docs

This opens the FastAPI Swagger documentation.

### 5️⃣ Stop the Containers
To stop the containers, use:

```bash
docker-compose down
```
