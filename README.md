
# Customer Churn Prediction Web App

## 📌 Project Overview
This project predicts whether a customer will **STAY** or **LEAVE** using
**Logistic Regression Machine Learning model** and a **Flask web application**.

It is useful for:

* Telecom companies
* Banks
* Subscription-based apps
  to identify customers who may leave the service.

---

## 🚀 Features

* User login page (access for everyone)
* Customer churn prediction using ML model
* Result shown instantly on the same page
* Prediction history tracking
* Simple HTML + CSS UI
* Flask backend integration

---

## 🛠 Technologies Used

* Python
* Flask
* Pandas
* Scikit-learn
* HTML
* CSS

---

## 📂 Project Structure

```
churn_final_project/
│
├── app.py
├── customer_churn.csv
│
├── templates/
│     ├── login.html
│     ├── index.html
│     ├── history.html
│
└── static/
      └── style.css
```

---

## ▶️ How to Run the Project

### 1️⃣ Install Python libraries

```
pip install flask pandas scikit-learn
```

### 2️⃣ Run the Flask app

```
python app.py
```

### 3️⃣ Open in browser

```
http://127.0.0.1:5000
```

Login → Enter customer details → Click **Predict**
➡ Result will show **STAY or LEAVE** below the button.

---

## 📊 Dataset Format (customer_churn.csv)

```
Age,Tenure,MonthlyCharge,Complaints,Churn
25,12,500,0,0
40,5,1200,3,1
30,24,700,1,0
50,2,1500,4,1
```

* **Churn = 1 → Leave**
* **Churn = 0 → Stay**

---

## 🔮 Future Improvements

* Database storage for users & history
* Admin dashboard
* Graphical analytics charts
* Online deployment (Render / Railway)
* Better UI design

---

## 👩‍💻 Author

**Student Machine Learning Project