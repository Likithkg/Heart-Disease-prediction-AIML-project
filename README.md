This is the my final year project called as "Heart disease prediction using AIML". It uses python back-end and html, css and javascript front-end.
It uses 7 modules of python for training dataset and predicting the outcome. 6 from scikit-learn module and 7th one is the xgboost.

# Heart Disease Prediction System (Flask + ML)

A web-based **Heart Disease Prediction System** built using **Python, Flask, and Machine Learning**.  
The application allows users to register, log in, enter medical parameters, and predict the risk of heart disease.  
It also exposes a **secured API** protected by **API key authentication**.

---

## Features

- User Authentication (Register / Login / Session-based)
- Machine Learning–based Heart Disease Prediction
- Interactive Prediction UI
- Stores prediction data for analysis
- Secure REST API with API Key validation
- Clean separation of UI routes and API routes

---

## Tech Stack

### Backend
- Python
- Flask
- Machine Learning (Scikit-learn)
- REST API

### Frontend
- HTML
- CSS
- JavaScript
- Bootstrap / Tailwind (UI)

### Security
- Flask Sessions (for browser users)
- API Key Authentication (for API access)

---

## Project Structure

├── app.py
├── auth.py
├── helper/
│ ├── DiseaseaPrediction.py
│ ├── UserEntry.py
│ ├── AddData.py
│ └── FeedBack.py
├── templates/
│ ├── index.html
│ ├── login.html
│ ├── register.html
│ ├── after.html
│ └── static/
│ ├── css/
│ ├── js/
│ └── img/
├── requirements.txt
└── README.md


---

## Installation & Setup

### Clone the repository
```bash
git clone https://github.com/your-username/heart-disease-prediction.git
cd heart-disease-prediction

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt

```

### Images
![Screenshot (67)](https://github.com/Likithkg/Heart-Disease-prediction-AIML-project/assets/109513581/02a51ad8-f7e4-4838-a424-3c4eb08c972d)
![Screenshot (68)](https://github.com/Likithkg/Heart-Disease-prediction-AIML-project/assets/109513581/73fe7adc-15c9-43de-8ff5-bf54f78591bc)
![Screenshot (69)](https://github.com/Likithkg/Heart-Disease-prediction-AIML-project/assets/109513581/a74f37fc-350f-4340-a1cf-6811c447c945)
![Screenshot (70)](https://github.com/Likithkg/Heart-Disease-prediction-AIML-project/assets/109513581/628071b2-6609-46aa-9aa3-1f7c2341efa0)