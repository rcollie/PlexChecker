# PlexChecker

I encountered issues with Plex Media Server spontaneously quitting on my 2020 Mac Mini M1. Discovering the original version of PlexChecker by Gavin Fuller on GitLab (https://gitlab.com/Flaming_Keyboard/plex-checker), I found it was designed for Windows. To run it on my Mac, I rewrote it based on his original code. The original data is included in this repository, named `original_plex-checker-master.zip`.

## Installation and Setup

1. **Download and Install Python:** Ensure you're using Python 3.12.2 or the latest version available at https://www.python.org/downloads/macos/.
   
   - **Note:** If Python was installed via HomeBrew, adjust the related paths accordingly.

2. **Configure `PlexChecker.plist`:** Edit `PlexChecker.plist` to fit your configuration and place it in `~/Library/LaunchAgents/`.
   
   - **Note:** This assumes you are currently logged into the user account running the Plex Media Server.

3. **Edit `PlexChecker.py`:** Customize `PlexChecker.py` for your setup and store it in a convenient location. I keep mine on the desktop in its own folder for easy access to the log file.

4. **Set `PlexChecker.py` to 'Read-Only':** Right-click on the file, navigate to "Sharing & Permissions," and change all privileges to read-only. This step isn't mandatory but recommended as a precaution against malicious use.

## Finalizing Setup

Enable your Python interpreter (e.g., Python Launcher, if installed via HomeBrew) to open at login:

- Go to `System Preferences > Users & Groups > Login Items` and add Python Launcher. If `PlexChecker.plist` is correctly placed, it should allow the script to run in the background. If not, add `PlexChecker.plist` to the list here as well.

You can now launch `PlexChecker.py`. Quit Plex Media Server and wait (the default wait time is 5 minutes, which can be adjusted in the script).

## Share & Enjoy

We hope PlexChecker enhances your Plex experience. Contributions, suggestions, and feedback are welcome! Feel free to open an issue or pull request.

## Notes

### Customization Options

- **Run Time:** The script is set to check the server every 5 minutes by default. You can adjust this interval in the script:

```python
while True:
    main()
    time.sleep(300)  # Waits for 5 minutes.
```
- **Logging:** By default, the script creates a log file in the same location as PlexChecker.py. You can disable this feature in the script if preferred.

## Contributions

Contributions to PlexChecker are welcome! If you have suggestions, improvements, or bug fixes, please feel free to submit a pull request or open an issue.

## Acknowledgments

A special thanks to Gavin Fuller for creating the original PlexChecker on which this project is based. Check out the original version at https://gitlab.com/Flaming_Keyboard/plex-checker.
