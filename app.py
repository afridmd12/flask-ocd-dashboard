from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd
import os

app = Flask(__name__)
app.secret_key = "secret123"

UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

dataframe = None

@app.route("/", methods=["GET", "POST"])
def index():
    global dataframe
    tables = None

    if request.method == "POST":
        # Upload CSV
        if "file" in request.files:
            file = request.files["file"]
            if file.filename.endswith(".csv"):
                filepath = os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(filepath)
                dataframe = pd.read_csv(filepath)
                flash("CSV file uploaded successfully!", "success")
            else:
                flash("Please upload a valid CSV file!", "error")

        # Search by Age + Gender
        elif "age" in request.form and "gender" in request.form:
            if dataframe is not None:
                age = request.form.get("age")
                gender = request.form.get("gender")
                results = dataframe[
                    (dataframe["Age"].astype(str) == age) &
                    (dataframe["Gender"].str.lower() == gender.lower())
                ]
                if not results.empty:
                    tables = results.to_html(classes="table table-bordered", index=False)
                else:
                    flash("No records found for given Age and Gender.", "error")

        # Search by Patient ID
        elif "patientid" in request.form:
            if dataframe is not None:
                pid = request.form.get("patientid")
                results = dataframe[dataframe["PatientID"].astype(str) == pid]
                if not results.empty:
                    tables = results.to_html(classes="table table-bordered", index=False)
                else:
                    flash("No records found for given Patient ID.", "error")

    return render_template("index.html", tables=tables)

if __name__ == "__main__":
    app.run(debug=True)
