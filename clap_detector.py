import pyaudio
import numpy as np

# Tuning Parameters
THRESHOLD = 1000  # Adjust this: higher means it needs a louder clap
CHUNK = 1024       # How much audio to process at once
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

import time

def detect_clap():
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Double-Clap Detector active. Waiting for two sharp noises...")
    
    last_clap_time = 0
    clap_count = 0

    try:
        while True:
            data = stream.read(CHUNK, exception_on_overflow=False)
            audio_data = np.frombuffer(data, dtype=np.int16)
            amplitude = np.max(np.abs(audio_data))

            if amplitude > THRESHOLD:
                current_time = time.time()
                
                # If this is the second clap within 0.1s to 1.0s
                if clap_count == 1 and 0.1 < (current_time - last_clap_time) < 1.0:
                    print(f"DOUBLE CLAP DETECTED! (Amplitude: {amplitude})")
                    return True
                
                # Register first clap
                print(f"First clap detected... (Amplitude: {amplitude})")
                clap_count = 1
                last_clap_time = current_time
                
                # Brief pause to avoid counting the same noise twice
                time.sleep(0.1)

            # Reset count if too much time passes between claps
            if clap_count == 1 and (time.time() - last_clap_time) > 1.0:
                print("Second clap timeout. Resetting...")
                clap_count = 0
                
    except KeyboardInterrupt:
        print("\nStopping detector...")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

if __name__ == "__main__":
    detect_clap()