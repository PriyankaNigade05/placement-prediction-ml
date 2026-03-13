# 🎓 Placement Prediction using Machine Learning

This project predicts whether a student will be **placed or not placed** using Machine Learning.
The model analyzes student academic performance and other related features to make predictions about placement outcomes.

---

## 📌 Project Description

This is a Machine Learning classification project that uses the **Random Forest Classifier** to predict student placement status based on academic data.

---

## 🛠 Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn

---

## 🤖 Machine Learning Algorithm

* Random Forest Classifier

---

## 📊 Model Evaluation

The model was evaluated using the following metrics:

* Accuracy Score
* Confusion Matrix
* ROC Curve

These metrics help measure how well the model predicts student placement.

---

## 📈 Model Performance

The Random Forest model achieved **87% accuracy** on the test dataset.

### Classification Report

| Class          | Precision | Recall | F1-Score | Support |
| -------------- | --------- | ------ | -------- | ------- |
| 0 (Not Placed) | 0.93      | 0.91   | 0.92     | 323     |
| 1 (Placed)     | 0.62      | 0.70   | 0.65     | 69      |

### Overall Metrics

* **Accuracy:** 0.87
* **Macro Average F1 Score:** 0.79
* **Weighted Average F1 Score:** 0.87

### Training vs Testing Accuracy

* **Training Accuracy:** 97.63%
* **Testing Accuracy:** 86.99%

---

## 📷 Screenshots

### User Interface

![UI](images/ui.png)

### Confusion Matrix

![Confusion Matrix](images/confusion_matrix.jpg)

### ROC Curve

![ROC Curve](images/ROC_curve.jpg)

---

## 📁 Project Files

* `placement_prediction.ipynb` – Machine learning model training
* `college_student_placement_dataset.csv` – Dataset used for training
* `RandomForestFinal.pkl` – Saved trained model
* `app.py` – Flask application for prediction
* `requirements.txt` – Python libraries used

---

## 🚀 Future Improvements

* Improve model accuracy with more training data
* Try advanced machine learning algorithms
* Deploy the project on a cloud platform

---



