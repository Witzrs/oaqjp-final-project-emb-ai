"""This is an implementation of an emotion detection application"""
import json
import requests

URL='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyse):
    input={ "raw_document": { "text": text_to_analyse } }
    response = requests.post(URL, json = input, headers=HEADERS, timeout=1000)
    if response.status_code == 400:
        return {'anger': None,
              'disgust': None,
              'fear': None,
              'joy': None,
              'sadness': None,
              "dominant_emotion": None
             }
    stats = json.loads(response.text)

    emotions = []
    anger = {"name":"anger","score":stats['emotionPredictions'][0]['emotion']['anger']}
   
    disgust = {"name":"disgust","score":stats['emotionPredictions'][0]['emotion']['disgust']}
    emotions.append(disgust)
    
    fear = {"name":"fear","score":stats['emotionPredictions'][0]['emotion']['fear']}
    emotions.append(fear)
    
    joy = {"name":"joy","score":stats['emotionPredictions'][0]['emotion']['joy']}
    emotions.append(joy)
    
    sadness = {"name":"sadness","score":stats['emotionPredictions'][0]['emotion']['sadness']}
    emotions.append(sadness)
    temp_emotion = anger
    dominant_emotion = "anger"

    #iteration to identify the dominant emotion
    for emotion in emotions:
        if emotion['score']>temp_emotion['score']:
            temp_emotion = emotion
            dominant_emotion = emotion['name']

    #dict with the results for all
    result = {'anger': anger['score'],
              'disgust': disgust['score'],
              'fear': fear['score'],
              'joy': joy['score'],
              'sadness': sadness['score'],
              "dominant_emotion": dominant_emotion
             }
    return result

#emotion_detector('I Love this new technology')