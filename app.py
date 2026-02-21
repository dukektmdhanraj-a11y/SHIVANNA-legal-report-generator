from flask import Flask, request, send_file
from python.dispatcher import dispatch
import os
import re

app = Flask(__name__)

def safe_filename(text):
    if not text:
        return "document"
    text = text.strip().replace(" ", "_")
    return re.sub(r"[^a-zA-Z0-9_]", "", text)


def generate_filename(data, default_name):
    name = (
        data.get("APPLICANT_NAME")
        or data.get("APPLICANT_FULL")
        or data.get("APPLICANT_BOLD")
        or "document"
    )

    date = data.get("DATE", "date")

    name = safe_filename(name)
    date = safe_filename(date)

    return f"{name}_{date}.docx"


@app.route("/")
def home():
    return """
    <h2>Select Document Type</h2>
    <ul>
        <li><a href="/gift">Gift</a></li>
        <li><a href="/sale">Sale</a></li>
        <li><a href="/ots">OTS</a></li>
    </ul>
    """


@app.route("/gift", methods=["GET", "POST"])
def gift():
    if request.method == "POST":
        data = request.form.to_dict()
        filename = generate_filename(data, "gift")
        output_path = os.path.join("output", filename)

        dispatch("gift", data, output_path)
        return send_file(output_path, as_attachment=True)

    return open("html/gift.html", encoding="utf-8").read()


@app.route("/sale", methods=["GET", "POST"])
def sale():
    if request.method == "POST":
        data = request.form.to_dict()
        filename = generate_filename(data, "sale")
        output_path = os.path.join("output", filename)

        dispatch("sale", data, output_path)
        return send_file(output_path, as_attachment=True)

    return open("html/sale.html", encoding="utf-8").read()


@app.route("/ots", methods=["GET", "POST"])
def ots():
    if request.method == "POST":
        data = request.form.to_dict()
        filename = generate_filename(data, "ots")
        output_path = os.path.join("output", filename)

        dispatch("ots", data, output_path)
        return send_file(output_path, as_attachment=True)

    return open("html/ots.html", encoding="utf-8").read()


if __name__ == "__main__":
    os.makedirs("output", exist_ok=True)
    app.run(debug=True)