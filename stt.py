import sounddevice as sd
import numpy as np
import speech_recognition as sr
import datetime

fs = 44100  # Sampling frequency
duration = 5  # Duration in seconds

recognizer = sr.Recognizer()

# List to store recognized texts
recognized_texts = []

print("Voice Assistant Started. Say 'stop recording' to exit.")

while True:
    print("Recording...")
    # Record audio (using int16 for proper sample width)
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()

    # Convert the recorded audio into an AudioData object without saving to a file
    audio_data_obj = sr.AudioData(myrecording.tobytes(), fs, 2)

    print("Converting speech to text...")
    try:
        text = recognizer.recognize_google(audio_data_obj)
        recognized_texts.append(text)
        print("Recognized text:", text)
        print("All recognized texts:", recognized_texts)

        # Stop the assistant if the user says "stop recording"
        if text.lower() == "stop recording":
            print("Stopping voice assistant.")
            break

    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError:
        print("Could not request results. Check your internet connection.")
