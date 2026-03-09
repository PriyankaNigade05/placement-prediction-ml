from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load your trained model
model = joblib.load("RandomForestFinal.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    # Get form values
    IQ_level = int(request.form["IQ_level"])
    Prev_Sem_Result = float(request.form["Prev_Sem_Result"])
    CGPA = float(request.form["CGPA"])
    Academic_Performance=int(request.form["Academic_Performance"])
    Internship_Experience = int(request.form["Internship_Experience"])
    Extra_Curricular_Score= int(request.form["Extra_Curricular_Score"])
    Communication_Skills = int(request.form["Communication_Skills"])
    Projects_Completed = int(request.form["Projects_Completed"])

    # Create DataFrame in SAME ORDER as training
    input_data = pd.DataFrame([[
        IQ_level,
        Prev_Sem_Result,
        CGPA,
        Academic_Performance,
        Internship_Experience,
        Extra_Curricular_Score,
        Communication_Skills,
        Projects_Completed,
        
    ]],
    columns=[
        "IQ_level",
        "Prev_Sem_Result",
        "CGPA",
        "Academic_Performance",
        "Internship_Experience",
        "Extra_Curricular_Score",
        "Communication_Skills",
        "Projects_Completed",
    ])
    input_data['Total_Score'] = input_data['CGPA'] + input_data['Academic_Performance'] + input_data['Prev_Sem_Result']
    input_data['Skills_Score'] = input_data['Communication_Skills'] + input_data['Extra_Curricular_Score'] + input_data['Projects_Completed']
    input_data['Experience_Score'] = input_data['Internship_Experience'] + input_data['Projects_Completed']
    
    input_data = input_data[['IQ_level', 'Total_Score', 'Skills_Score', 'Experience_Score']]


    # Prediction
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        result = "🎉 Student is Likely to be PLACED"
        color = "green"
    else:
        result = "❌ Student is Likely to be NOT PLACED"
        color = "red"

    return render_template("result.html",
                       prediction_text=result,
                       color=color)


if __name__ == "__main__":
    app.run(debug=True)