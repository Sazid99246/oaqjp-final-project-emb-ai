import requests
import json

def emotion_detector(text_to_analyze):
    # Define the URL for the Watson NLP Emotion Predict API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Set the header to specify the model
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Input payload
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    # Make the POST request
    response = requests.post(url, headers=headers, json=input_json)
    
    # Return the text attribute of the response object
    return response.text
