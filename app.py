import logging
import threading
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from audio.audioTranscriber import AudioTranscriber
import json

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = 'yourSecretKey'

# Initialize the AudioTranscriber
audioTranscriber = AudioTranscriber()

transcriptionData = []  # Store transcriptions for UI display
isListening = False  # Listening state flag

def startListening():
    global isListening

    if not isListening:
        isListening = True
        logger.info("Starting audio transcription thread...")
        threading.Thread(target=audioProcessor, daemon=True).start()
        logger.info("Listening thread started.")

def stopListening():
    global isListening

    if isListening:
        isListening = False
        logger.info("Listening stopped.")

@app.route('/')
def index():
    return redirect(url_for('mainInterface'))

@app.route('/mainInterface')
def mainInterface():
    if 'userId' not in session:
        return redirect(url_for('login'))
    return render_template('mainInterface.html')

@app.route('/toggleListening', methods=['POST'])
def toggleListening():
    global isListening

    if isListening:
        stopListening()
        return jsonify({"status": "stopped"})
    else:
        startListening()
        return jsonify({"status": "started"})

@app.route('/getTranscriptions', methods=['GET'])
def getTranscriptions():
    return jsonify(transcriptionData)

def audioProcessor():
    while isListening:
        logger.debug("Checking audio queue...")
        audioData = audioTranscriber.readAudio()
        if audioData and audioTranscriber.isSpeech(audioData):
            logger.debug("Speech detected.")
            responses = audioTranscriber.transcribeAudio(audioData)
            if responses:
                for response in responses:
                    if not response.results:
                        continue
                    result = response.results[0]
                    if not result.alternatives:
                        continue
                    transcript = result.alternatives[0].transcript
                    transcriptionData.append({"transcript": transcript})
                    logger.info(f"Transcript: {transcript}")
                    saveTranscriptionToFile(transcript)

def saveTranscriptionToFile(transcript):
    # Load existing data if the file already exists
    if os.path.exists("data/transcriptions.json"):
        with open("data/transcriptions.json", "r") as file:
            existing_data = json.load(file)
    else:
        existing_data = []

    # Append the new transcript
    existing_data.append({"transcript": transcript})

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['userId'] = 1  # Example user ID after login
        return redirect(url_for('mainInterface'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('userId', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)