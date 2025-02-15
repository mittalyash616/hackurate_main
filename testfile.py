import sounddevice as sd
import numpy as np
import speech_recognition as sr
import datetime
import threading
import time
def voice(recognized_texts1,recognized_texts2):
    def process_channel(channel, start_offset_samples, recognized_texts):
            read_index = start_offset_samples
            chunk_samples = int(chunk_duration * fs)
            while not stop_event.is_set():
                with buffer_lock:
                    current_length = len(audio_buffer)
                if read_index + chunk_samples <= current_length:
                    with buffer_lock:
                        chunk = audio_buffer[read_index: read_index + chunk_samples]
                    read_index += chunk_samples

                    audio_array = np.array(chunk, dtype=np.int16)
                    audio_bytes = audio_array.tobytes()
                    audio_data = sr.AudioData(audio_bytes, fs, 2)

                    try:
                        text = recognizer.recognize_google(audio_data)
                        #timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        print(f"[Channel-{channel}] Recognized text:", text)
                        recognized_texts.append(f"{text}")
                        if "stop recording" in text.lower():
                            stop_event.set()
                    except sr.UnknownValueError:
                        pass
                    except sr.RequestError:
                        pass
                else:
                    time.sleep(0.1)
    def audio_callback(indata, frames, time_info, status):
            if status:
                print(status)
            with buffer_lock:
                audio_buffer.extend(indata[:, 0].tolist())                
    fs = 44100         # Sampling frequency
    chunk_duration = 5  # Duration (in seconds) of each processing chunk

    recognizer = sr.Recognizer()

    stop_event = threading.Event()

    audio_buffer = []
    buffer_lock = threading.Lock()

    print("Voice Assistant Started. Say 'stop recording' to exit.")

    stream = sd.InputStream(samplerate=fs, channels=1, dtype='int16', callback=audio_callback)
    stream.start()

    thread1 = threading.Thread(target=process_channel, args=(1, 0, recognized_texts1))
    thread2 = threading.Thread(target=process_channel, args=(2, int(2 * fs), recognized_texts2))

    thread1.start()
    thread2.start()

    while not stop_event.is_set():
        time.sleep(0.1)

    stream.stop()
    stream.close()

    thread1.join()
    thread2.join()
    

    print("\nChannel 1 Recognized Texts:")
    for entry in recognized_texts1:
        print(entry)

    print("\nChannel 2 Recognized Texts:")
    for entry in recognized_texts2:
        print(entry)

    print("Voice assistant stopped.")
