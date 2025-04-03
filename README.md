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

## 📡 API Endpoints

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

- **POST** `/api/follow/{username}/` → Follow/Unfollow a user
- **GET** `/api/followers/` → List followers
- **GET** `/api/following/` → List following

### 🏆 Profile

- **GET** `/api/profile/{username}/` → View user profile
- **PUT** `/api/profile/{username}/` → Update user profile

## 🔥 Contributing

Pull requests are welcome! 🚀 If you have suggestions, feel free to open an issue. Let's build something amazing together! 💪

## 📜 License

MIT License © 2025 Tesfamichael Tafere

---

🌍 Built with ❤️ by Tesfamichael Tafere & Team 🚀
