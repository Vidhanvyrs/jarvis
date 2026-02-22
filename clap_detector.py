import pyaudio
import numpy as np

# Tuning Parameters
THRESHOLD = 1000  # Adjust this: higher means it needs a louder clap
CHUNK = 1024       # How much audio to process at once
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

def detect_clap():
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Clap Detector active. Waiting for a sharp noise...")

    try:
        while True:
            data = stream.read(CHUNK, exception_on_overflow=False)
            audio_data = np.frombuffer(data, dtype=np.int16)
            amplitude = np.max(np.abs(audio_data))

            if amplitude > THRESHOLD:
                print(f"SPIKE DETECTED! (Amplitude: {amplitude})")
                return True
                
    except KeyboardInterrupt:
        print("\nStopping detector...")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

if __name__ == "__main__":
    detect_clap()