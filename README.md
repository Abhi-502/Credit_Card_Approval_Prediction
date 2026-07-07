# 💳 Credit Card Approval Prediction

A Machine Learning based web application that predicts whether a customer's credit card application will be approved or rejected based on personal and financial information.

The project uses Flask for the backend and a trained Machine Learning model for prediction.

---

# 🚀 Features

- Predicts Credit Card Approval
- User-friendly web interface
- Machine Learning powered predictions
- Real-time results
- Responsive design
- Easy deployment

---

# 🛠 Technologies Used

### Programming Language
- Python 3

### Machine Learning
- Scikit-learn
- Pandas
- NumPy
- Pickle

### Data Visualization
- Matplotlib
- Seaborn

### Web Development
- Flask
- HTML5
- CSS3

---

# 📁 Project Structure

```
CreditCardApprovalPrediction/
│
├── app.py
├── model.pkl
├── encoders.pkl
├── requirements.txt
├── README.md
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── application_record.csv
├── credit_record.csv
└── train_model.py
```

---

# 📊 Dataset

The project uses two datasets:

- application_record.csv
- credit_record.csv

These datasets are merged using the customer ID before training the model.

---

# ⚙ Machine Learning Workflow

1. Load datasets
2. Handle missing values
3. Remove duplicates
4. Convert credit status into binary labels
5. Merge datasets
6. Encode categorical features using LabelEncoder
7. Split data into training and testing sets
8. Train multiple machine learning models
9. Compare model accuracy
10. Save the best performing model

---

# 🤖 Models Used

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

The model with the highest accuracy is automatically selected and saved as:

```
model.pkl
```

Categorical encoders are saved as:

```
encoders.pkl
```

---

# 📋 Input Features

The model predicts using the following features:

- Gender
- Own Car
- Own Property
- Number of Children
- Annual Income
- Income Type
- Education Type
- Family Status
- Housing Type
- Days Since Birth
- Days Employed
- Occupation Type

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/CreditCardApprovalPrediction.git
```

Move into the project folder

```bash
cd CreditCardApprovalPrediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

Start the Flask server

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000/
```

---

# 📷 Screens

### Home Page

- Enter applicant details
- Click Predict

### Result Page

Displays

- Credit Card Approved

or

- Credit Card Rejected

---

# 📈 Future Improvements

- Probability Score
- Feature Importance Visualization
- User Authentication
- Database Integration
- Cloud Deployment
- Explainable AI (SHAP/LIME)
- REST API Support

---

# 👨‍💻 Author

**Abhi Illuri**

B.Tech Computer Science and Engineering

Rajeev Gandhi Memorial College of Engineering and Technology

---

# 📄 License

This project is developed for educational and learning purposes.

Feel free to use and modify it.

---

# ⭐ Acknowledgements

- Scikit-learn
- Flask
- Pandas
- NumPy
- Matplotlib
- Seaborn
