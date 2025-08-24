from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

# Route for home page (renders index.html)
@app.route("/")
def home():
    return render_template("index.html")

# Route for emotion detection API
@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze:
        return "Please provide a text to analyze using ?textToAnalyze=your_text", 400

    result = emotion_detector(text_to_analyze)

    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return formatted_response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
