# 🚀 Django Social Media API

A fully functional social media backend built with Django and Django REST Framework (DRF). This project includes user authentication, post creation, interactions (likes & comments), follow system, and profile management.

## 📌 Features

- ✅ User Authentication (JWT-based) 🔐
- ✅ CRUD for Posts 📝
- ✅ Like & Comment System ❤️💬
- ✅ Follow/Unfollow Users 🔄
- ✅ Profile Management 🏆
- ✅ CORS Support 🌍
- ✅ Scalable & Secure Design 🔒

## 🏗️ Installation & Setup

1️⃣ **Clone the repository**

```bash
git clone https://github.com/your-username/django-social-media.git
cd django-social-media
```

2️⃣ **Create & activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3️⃣ **Install dependencies**

```bash
pip install -r requirements.txt
```

4️⃣ **Run migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

5️⃣ **Create a superuser**

```bash
python manage.py createsuperuser
```

6️⃣ **Start the server**

```bash
python manage.py runserver
```

## 📡 API Endpoints (Brief)

### 🔑 Authentication

- **POST** `/api/auth/register/` → User Registration
- **POST** `/api/auth/login/` → User Login (JWT)

### 📝 Posts

- **GET** `/api/posts/` → List all posts
- **POST** `/api/posts/` → Create a post
- **GET** `/api/posts/{id}/` → Retrieve a single post
- **PUT** `/api/posts/{id}/` → Update a post
- **DELETE** `/api/posts/{id}/` → Delete a post

### ❤️ Likes & Comments

- **POST** `/api/posts/{id}/like/` → Like a post
- **POST** `/api/posts/{id}/comment/` → Comment on a post

### 🔄 Follow System

- **POST** `/api/follow/{username}/` → Follow/Unfo llow a user
- **GET** `/api/followers/` → List followers
- **GET** `/api/following/` → List following

### 🏆 Profile

- **GET** `/api/profile/{username}/` → View user profile
- **PUT** `/api/profile/{username}/` → Update user profile

## 📡 API Endpoints Doc **_Swagger_** (Detailed)

For a comprehensive and interactive API documentation, Swagger UI is integrated into the project. You can access it by navigating to:

- **URL**: `http://127.0.0.1:8000/swagger/`

This provides a user-friendly interface to explore and test all available API endpoints.

![alt text](image.png)
![alt text](image-1.png)
![alt text](image-2.png)
![alt text](image-3.png)
![alt text](image-4.png)

### 🗂️ Models

In this project, the following models are implemented to support the social media functionality:

- **👤 User**: Represents the users of the platform, including authentication and profile details.
- **📝 Post**: Stores the content of posts created by users.
- **❤️ Like**: Tracks likes on posts by users.
- **💬 Comment**: Manages comments made on posts.
- **🔄 Follow**: Handles the follow/unfollow relationships between users.

Each model is designed with scalability and security in mind to ensure a robust backend structure.

![alt text](image-5.png)
![alt text](image-6.png)

## 🔥 Contributing

Pull requests are welcome! 🚀 If you have suggestions, feel free to open an issue. Let's build something amazing together! 💪

## 📜 License

MIT License © 2025 Tesfamichael Tafere

---

🌍 Built with ❤️ by Tesfamichael Tafere & Team 🚀
