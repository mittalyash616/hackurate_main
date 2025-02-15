# import sounddevice as sd
# import numpy as np
# import speech_recognition as sr
# import datetime
# def stt():
#     fs = 44100  # Sampling frequency
#     duration = 5  # Duration in seconds

#     recognizer = sr.Recognizer()

#     # List to store recognized texts
#     recognized_texts = []

#     print("Voice Assistant Started. Say 'stop recording' to exit.")

#     while True:
#         print("Recording...")
#         # Record audio (using int16 for proper sample width)
#         myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
#         sd.wait()

#         # Convert the recorded audio into an AudioData object without saving to a file
#         audio_data_obj = sr.AudioData(myrecording.tobytes(), fs, 2)

#         print("Converting speech to text...")
        
#         text = recognizer.recognize_google(audio_data_obj)
        
#         # Stop the assistant if the user says "stop recording"
#         if "stop recording" in text.lower():
#             print("Stopping voice assistant.")
#             last=text.split()
#             last.remove("stop")
#             last.remove("recording")
#             recognized_texts.append(" ".join(last))
#             print("All recognized texts:", recognized_texts)
#             break
#         else:
#             recognized_texts.append(text)
#             print("Recognized text:", text)
