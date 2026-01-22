Expense Tracking System 💸📊

A full-stack Expense Tracking System that allows users to add/update daily expenses and visualize spending patterns using analytics dashboards.
This project is built with Streamlit (Frontend UI), FastAPI (Backend APIs), and MySQL (Database).

✨ Features
✅ Add / Update Expenses (CRUD)

Select a date and add expenses for that day

Update existing expense entries for the selected date

Add details:

-Amount
-Category
-Notes

Categories supported:

-Rent
-Food
-Shopping
-Entertainment
-Other

📊 Expense Analytics Dashboard

Select a start date and end date

Get analytics for expense utilization across the chosen date range

✅ Displays:

Bar chart (Expense Breakdown by Category)

Summary table showing:

Category

Total amount spent

Percentage contribution

🧾 Backend API Support

FastAPI endpoints for:

Fetching expenses by date

Adding/updating expenses

Fetching analytics between date ranges

🗄️ MySQL Database Storage

Stores all expense records

Persistent CRUD operations using MySQL queries

🛠️ Tech Stack

Frontend: Streamlit

Backend: FastAPI

Database: MySQL

Language: Python

Visualization: Streamlit charts (Bar chart)

Testing: Pytest (test structure included)

📸 Screenshots
Add / Update Expenses UI

Easy-to-use input form for entering daily expenses

Analytics UI

Category-wise bar chart

Table showing total and percentage utilization

📂 Project Structure
expense_tracking_system/
│
├── backend/
│   ├── db_helper.py
│   ├── logging_setup.py
│   ├── server.py
│   ├── server.log
│   └── db_helper.log
│
├── frontend/
│   ├── app.py
│   ├── intro_streamlit.py
│   ├── add_update_ui.py
│   └── analytics_ui.py
│
├── tests/
│   ├── backend/
│   ├── frontend/
│   └── conftest.py
│
├── requirements.txt
└── README.md

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone <your-repo-link>
cd expense_tracking_system

2️⃣ Create Virtual Environment
python -m venv .venv


Activate environment:

Windows

.venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

🗄️ MySQL Database Setup

Create database:

CREATE DATABASE expense_manager;


Create table:

CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    expense_date DATE NOT NULL,
    amount FLOAT NOT NULL,
    category VARCHAR(100) NOT NULL,
    notes VARCHAR(255)
);


Configure DB connection in:
📌 backend/db_helper.py

▶️ Run the Application
✅ Start FastAPI Backend

From project root:

uvicorn backend.server:app --reload


Backend server runs at:

http://127.0.0.1:8000


FastAPI docs:

http://127.0.0.1:8000/docs

✅ Start Streamlit Frontend

From project root:

streamlit run frontend/app.py


Frontend runs at:

http://localhost:8501

🔗 API Endpoints (Sample)

GET /expenses/{expense_date}
Fetch expenses for a given date

POST /expenses/
Add or update expenses

POST /analytics/
Expense breakdown between start and end dates

🧪 Run Tests
pytest

🚀 Future Enhancements

Authentication (login/signup)

Export analytics as CSV/PDF

Monthly & yearly dashboards

Interactive charts (Pie/Line chart)

Deployment to cloud (Render/AWS/GCP)

👨‍💻 Author

Preet Shah
Expense Tracking System using Streamlit + FastAPI + MySQL