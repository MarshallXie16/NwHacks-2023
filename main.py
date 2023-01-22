from flask import Flask, render_template, request
import csv
import sqlite3

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():

    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    # retrieve data from html form
    date = "Jan 1st"
    mood = request.form.get("mood")
    journal = request.form.get("journal")
    data = [date, mood, journal]
    # write to csv file
    with open('data.csv', mode='a', newline='') as file:
        # create csv writer
        writer = csv.writer(file)
        # write value to a single row
        writer.writerow([date, mood, journal])

    return render_template("today_result.html", date = date, mood = mood, journal = journal)

@app.route("/input", methods=["GET"])
def input():

    return render_template("today_input.html", date = "22")


if __name__ == "__main__":
    app.run(debug=True, port=5000)









