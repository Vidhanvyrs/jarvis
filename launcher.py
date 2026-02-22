import subprocess
import time

def launch_apps():
    """
    Launches the required applications for the project.
    Adjust the commands below if your system uses different names.
    """
    apps = [
        "antigravity",
        "google-chrome",
        "flatpak run md.obsidian.Obsidian",
        "gnome-terminal",
        "flatpak run com.getpostman.Postman",
        "flatpak run com.spotify.Client",
    ]
    
    print("Initiating launch sequence...")
    for app in apps:
        try:
            print(f"Launching {app}...")
            # Split the command string into a list for subprocess
            command = app.split()
            subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            time.sleep(0.5) # Brief pause between launches
        except FileNotFoundError:
            print(f"Warning: Could not find command for '{app}'. Please verify it is in your PATH.")
        except Exception as e:
            print(f"Error launching {app}: {e}")

    print("All applications have been triggered.")

if __name__ == "__main__":
    launch_apps()