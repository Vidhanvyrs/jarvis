import time
from clap_detector import detect_clap
from recognizer import listen_for_command
from launcher import launch_apps

def main():
    print("--- JARVIS SYSTEM INITIALIZED ---")
    
    try:
        while True:
            # Step 1: Sentinel Mode (Listening for Clap)
            print("\n[Sentinel] Waiting for clap...")
            if detect_clap():
                print("[Sentinel] Clap detected! Activating Ears...")
                
                # Step 2: The Ear (Listening for Trigger Phrase)
                # We give some feedback (like a beep or just a print)
                time.sleep(0.5) 
                if listen_for_command():
                    print("[Sentinel] Trigger phrase confirmed!")
                    
                    # Step 3: The Execution
                    launch_apps()
                    print("[Sentinel] Mission complete. Shutting down.")
                    return # Exit the function and program
                else:
                    print("[Sentinel] Trigger failed. Returning to Sentinel mode.")
            
            # Small rest to prevent CPU spikes
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\n--- JARVIS SHUTTING DOWN ---")

if __name__ == "__main__":
    main()