from audio.audioTranscriber import AudioTranscriber

audioTranscriber = AudioTranscriber()
audioTranscriber.startStream()

try:
    print("Recording... Press Ctrl+C to stop.")
    while True:
        audioData = transcribeAudio.readAudio()
        if transcribeAudio.isSpeech(audioData):
            print("Speech detected!")
except KeyboardInterrupt:
    transcribeAudio.stopStream()
    print("Stopped recording.")