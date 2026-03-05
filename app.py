from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

OPENROUTER_API_KEY = "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"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():

    prompt = request.json["prompt"]

    response = requests.post(
        "https://openrouter.ai/api/v1/images/generations",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "sourceful/riverflow-v2-pro",
            "prompt": prompt,
            "size": "1024x1024"
        }
    )

    data = response.json()

    if "data" in data:
        image_url = data["data"][0]["url"]
        return jsonify({"image": image_url})
    else:
        return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
