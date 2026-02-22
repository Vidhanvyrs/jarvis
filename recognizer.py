import speech_recognition as sr

def listen_for_command():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening for trigger phrase...")
        # Adjust for ambient noise for 1 second
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        try:
            # Listen for 5 seconds max
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            print("Processing speech...")
            
            # Using Google's free speech-to-text API
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            
            if "startup" in command or "let's go jarvis" in command:
                return True
            else:
                print("Phrase did not match.")
                return False
                
        except sr.WaitTimeoutError:
            print("Timed out waiting for speech.")
            return False
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return False
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return False
        except Exception as e:
            print(f"Error: {e}")
            return False

if __name__ == "__main__":
    if listen_for_command():
        print("TRIGGER ACTIVATED!")
    else:
        print("Trigger failed.")