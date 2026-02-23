# 🌱 AGROSEEDS — Smart Agriculture & E-Trade Platform

AGROSEEDS is a Django-based web application that combines agriculture intelligence, crop prediction, and an online seed marketplace into one platform. It helps farmers and agricultural users make better decisions using machine learning and provides a simple e-commerce interface for purchasing agricultural products.

---

## 🚀 Features

### 🔐 Authentication System

* User registration
* Login / logout
* Secure authentication using Django built-in system

### 🛒 E-Trade Marketplace

* View all products
* Filter products by category
* Add items to cart
* View cart contents

### 🌾 Crop Prediction System

Predicts suitable crop based on:

* Temperature
* Humidity
* pH level
* Rainfall

Uses trained ML model file:

```
final_model.sav
```

### 💬 Feedback System

* Users can submit feedback
* Feedback stored in database

### 👤 User Personalization

* Displays logged-in username across pages
* Session-based interaction

---

## 🛠 Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS
* **Database:** SQLite
* **Machine Learning:** Joblib serialized model
* **Authentication:** Django built-in auth system

---

## ⚙ Installation Steps

1. Clone the repository

```
git clone <https://github.com/koushikpj/AGROSEEDS>
```

2. Install virtual environment

```
pip install virtualenv
```

3. Create virtual environment

```
python -m venv ve
```

4. Activate environment (Windows)

```
ve\Scripts\activate
```

5. Install dependencies

```
pip install django pillow joblib scikit-learn
```

6. Run server

```
python manage.py runserver
```

---

## ✅ Usage

Open browser and go to:

```
http://127.0.0.1:8000
```

---

## 🎯 Project Goal

This project provides a farmer-friendly web application that:

* Recommends crops based on land and weather conditions
* Helps farmers decide agricultural inputs
* Connects farmers directly with consumers or retailers
* Eliminates middlemen in agricultural trade

---

## 👨‍💻 Author

**Koushik PJ**

---

## 📜 License

MIT License
