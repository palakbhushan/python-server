# 🚀 FastAPI CRUD API with MongoDB

A scalable CRUD API built with FastAPI, MongoDB, and Motor.

---

## 📁 Project Structure

```
python-server/
│── app/
│   ├── users/              # Users Module
│   │   ├── models.py       # Pydantic models
│   │   ├── service.py      # Business logic
│   │   ├── router.py       # API endpoints
│   ├── purchases/          # Purchases Module (Similar structure)
│   ├── db.py               # Database Connection
│   ├── main.py             # Main FastAPI app
│── .env                    # Environment Variables
│── requirements.txt        # Dependencies
│── README.md               # Documentation
```

---

## 🚀 Setup Guide

### 1️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 2️⃣ Set Up Environment Variables
Create a `.env` file and add your MongoDB details:
```ini
MONGO_URI=mongodb://localhost:27017
DATABASE_NAME=fastapi_db
```

### 3️⃣ Run the Server
```sh
uvicorn app.main:app --reload
```

### 4️⃣ Test API Endpoints
Use Postman or cURL:

#### 📌 Create a User
```sh
curl -X POST "http://127.0.0.1:8000/users/" \
     -H "Content-Type: application/json" \
     -d '{"name": "John Doe", "email": "john@example.com"}'
```

#### 📌 Get Users
```sh
curl -X GET "http://127.0.0.1:8000/users/"
```

---

## 🛠️ Available Endpoints

### Users
| Method | Endpoint        | Description     |
|--------|---------------|---------------|
| POST   | `/users/`     | Create User   |
| GET    | `/users/`     | Get All Users |
| PUT    | `/users/{id}` | Update User   |

### Purchases
| Method | Endpoint       | Description      |
|--------|--------------|----------------|
| POST   | `/purchases/` | Create Purchase |
| GET    | `/purchases/` | Get All Purchases |

---

## ⚡ Features
- 🚀 FastAPI for rapid API development.
- 🏦 MongoDB as the NoSQL database.
- ⚡ Motor for asynchronous MongoDB operations.
- 📌 Scalable project structure for maintainability.

---

## 👨‍💻 Contributing
1. Fork the repository 🍴  
2. Create a new branch: `git checkout -b feature-branch`  
3. Commit changes: `git commit -m "Added new feature"`  
4. Push branch: `git push origin feature-branch`  
5. Open a PR 🚀  

---

## 📜 License
This project is licensed under the MIT License.

---

## ✅ Next Steps
- 🔐 Add JWT Authentication
- 📝 Implement Logging
- 🧪 Write Unit Tests

