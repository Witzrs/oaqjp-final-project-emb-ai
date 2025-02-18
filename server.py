"""This is the class for the server instantiation"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def detect_emotion():
    """"This function handles the calls to the emotion_detector function
        It is responsible for extracting the provided parameters
        and passing them on to the server
    """
    text_input = request.args.get('textToAnalyze')
    result = emotion_detector(text_input)
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    result_simplified = f"'anger': {result['anger']},'disgust': {result['disgust']}, "
    result_simplified = result_simplified + f"'fear': {result['fear']}, 'joy': {result['joy']} "
    result_simplified = result_simplified + f"and 'sadness': {result['sadness']}"
    final_string = f"For the given statement the system response is {result_simplified}. "
    final_string = final_string + f"The dominant emotion is { result['dominant_emotion'] }"
    return final_string

@app.route('/')
def index():
    """"This function is responsible for loading the index.html page
        when a user first visits the web application
    """
    return render_template("index.html")
if (__name__) == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
