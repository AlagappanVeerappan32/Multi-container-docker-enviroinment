from flask import Flask, request, jsonify
import csv
import os
from collections import OrderedDict


app = Flask(__name__)


# Checking if the lines contain a comma
def validate_csv(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

        # Check if the first line contains headers
        if not lines[0].strip().startswith("product,amount"):
            return False

        for line in lines:
            if "," not in line:
                return False

    return True


# Reading the file to calculate sum
def calculate_sum(file_path, product):
    with open(file_path, "r") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        total_sum = 0
        for row in csv_reader:
            if row["product"] == product:
                total_sum += int(row["amount"])
    return total_sum


# Receives the POST request from Container 1 and performs operations [1,2]
@app.route("/result", methods=["POST"])
def receive_payload():
    if request.method == "POST":
        try:
            json_payload = request.get_json()
            print("Received payload:")
            print(json_payload)

            # Extracting file_name and product column
            file_name = json_payload.get("file")
            product = json_payload.get("product")

            current_directory = os.getcwd()
            file_path = os.path.join(current_directory, file_name)

            print("File path:")
            print(file_path)

            if not validate_csv(file_path):
                response_data = OrderedDict(
                    [("file", file_name), ("error", "Input file not in CSV format.")]
                )
                return jsonify(response_data)

            sum = calculate_sum(file_path, product)

            response_data = {"file": file_name, "sum": sum}
            return jsonify(response_data)

        except Exception as e:
            print("Error processing payload:", str(e))
            return "Error processing payload", 500
    else:
        return "Method Not Allowed", 405


# Runs on port 8080
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)


# Referene
# [1] - https://sentry.io/answers/flask-getting-post-data/
# [2] - https://flask.palletsprojects.com/en/2.3.x/quickstart/#routing
# modified the code according to the requirements
