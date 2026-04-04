
# 🚗 AI Car Recommendation System

> Content-Based Filtering • FastAPI • MongoDB Atlas • Production-Ready REST API

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-green?style=for-the-badge&logo=mongodb)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-FF6B6B?style=for-the-badge&logo=scikit-learn)

---

## 📌 What I Built

An AI-powered car recommendation system that suggests 
similar cars based on **category** and **price** — 
fully integrated with a live MongoDB database and 
exposed via a **FastAPI REST API**.

---

## 📅 Day-by-Day Work

| Day | Task | Work Done |
|-----|------|-----------|
| Day 1 | Setup & Planning | Python env, libraries, GitHub repo |
| Day 2 | Data Understanding | Analyzed SRS, identified datasets |
| Day 3 | Database & FastAPI | MongoDB Atlas connected |
| Day 4 | EDA | 6+ visualizations, price analysis |
| Day 5 | Feature Engineering | OneHotEncoder + MinMaxScaler |
| Day 6 | Recommendation Model | Cosine Similarity engine |
| Day 7 | FastAPI Endpoints | REST API with validation |
| Day 8 | MongoDB Integration | Live data, dynamic categories |

---

## 🏗️ System Architecture

```
User Request
     ↓
FastAPI Endpoint
/recommendation?category=SUV&max_price=100
     ↓
MongoDB Atlas → Live Car Data
     ↓
Feature Engineering (Dynamic)
     ↓
Cosine Similarity Calculation
     ↓
Top N Car IDs Returned
     ↓
Backend (Node.js) → React Frontend
```

---

## 🤖 AI Technique Used

**Content-Based Filtering using Cosine Similarity**

- **Input** → category + max_price
- **Output** → [car_id_1, car_id_2, car_id_3...]
- Similarity computed on normalized features

---

## 🔗 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API status + available categories |
| `/recommendation` | GET | Get car recommendations |
| `/cars` | GET | All cars from database |
| `/databases` | GET | DB structure explorer |

**Example Request:**
```
GET /recommendation?category=SUV&max_price=100&top_car=5
```

**Example Response:**
```json
{
  "category": "SUV",
  "max_price": 100,
  "car_ids": [2, 3, 4, 5, 41]
}
```

---

## 🛠️ Technologies Used

| Category | Tools |
|----------|-------|
| Language | Python 3.10+ |
| AI/ML | Scikit-learn, Pandas, NumPy |
| API | FastAPI, Uvicorn |
| Database | MongoDB Atlas, PyMongo |
| Data Analysis | Matplotlib, Seaborn, Jupyter |
| Environment | dotenv, certifi |
| Version Control | Git, GitHub |

---

## ✅ Key Achievements

- ✅ Live MongoDB integration — real data, not CSV
- ✅ Dynamic categories — no hardcoding
- ✅ Professional API with validation & error handling
- ✅ CORS enabled for React frontend
- ✅ Team coordination with backend developers

---

## ⚡ Challenges Solved

**1. MongoDB SSL Error**
Solved using `certifi` for SSL certificate handling.

**2. Hardcoded Categories Problem**
Made categories dynamic — automatically read from DB.

**3. Missing car_id in DB**
Generated car_id from DataFrame index.

**4. Feature Matrix Mismatch**
Two separate DataFrames — one for filtering, 
one for similarity.

---

## 📁 Project Structure

```
car-rental-recommendation-system/
│
├── api/
│   ├── main.py        ← FastAPI app
│   └── model.py       ← Recommendation logic
│
├── data/
│   ├── raw/           ← Original dataset
│   └── processed/     ← Feature matrix
│
├── notebooks/         ← EDA + Feature Engineering
├── models/            ← Saved models
├── docs/              ← Documentation
└── README.md
```

---

## 🚀 How to Run

```bash
# 1. Clone the repo
git clone https://github.com/RehmanAhmad333/car-rental-recommendation-system

# 2. Install dependencies
pip install -r requirements.txt

# 3. Setup .env file
MONGODB_URI=your_mongodb_uri

# 4. Run the API
uvicorn main:app --reload

# 5. Open browser
http://127.0.0.1:8000/docs
```

---

## 👤 Author

**Rehman Ahmad**
AI Developer Intern — TechNexus Virtual University

[![GitHub](https://img.shields.io/badge/GitHub-RehmanAhmad333-black?style=flat&logo=github)](https://github.com/RehmanAhmad333)

---

*Built with dedication during AI Developer Internship* 🚀
