import requests
import json

def emotion_detector(text_to_analyse):
    # API URL
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'

    # Handle blank input
    if not text_to_analyse.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    # Create payload
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Make request
    response = requests.post(url, json=myobj)

    # If server returns 400 → blank/invalid input
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    # Extract emotions
    response_dict = response.json()
    emotions = response_dict['documentSentiment']['emotion']

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": emotions['anger'],
        "disgust": emotions['disgust'],
        "fear": emotions['fear'],
        "joy": emotions['joy'],
        "sadness": emotions['sadness'],
        "dominant_emotion": dominant_emotion
    }
