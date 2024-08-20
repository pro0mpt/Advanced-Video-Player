<<<<<<< HEAD
Prompt :- # Advanced-Video-Player
Create a PyQt5-based advanced video player interface integrated with VLC, capable of playing various video formats such as .mp4, .avi, .mkv, .mov, and .flv. The application should feature:
=======
# Advanced-Video-Player

Prompt :- Create a PyQt5-based advanced video player interface integrated with VLC, capable of playing various video formats such as .mp4, .avi, .mkv, .mov, and .flv. The application should feature:
>>>>>>> 518d513c1d9e16d7537d587da7ce4947e648e35f

A video display area that dynamically resizes with the main window.
Control buttons for playing, pausing, stopping, and toggling fullscreen.
A volume slider that adjusts the audio volume.
A seek slider to jump to specific parts of the video, which should update in real-time during playback.
A "Load Video" button to open and load a video file using a file dialog.
Error handling with a message box to alert the user if an error occurs during playback.
The ability to toggle fullscreen mode with a button click.
<<<<<<< HEAD
The application should have a clean, minimalistic design with appropriate icons for each control button and should handle window close events gracefully by stopping the video playback.
=======



---

## Advanced Video Player
### Table of Contents
- Overview
- Features
- Requirements
- Installation and Setup
- How to Use
- How to Run in VS Code

### Overview
This repository contains a Python-based software application for video playback:

**Advanced Video Player**: A feature-rich video player built with PyQt5 and VLC, capable of playing various video formats and providing a simple, clean user interface for controlling video playback.

### Features
- **Play and Pause**: Toggle between playing and pausing the video.
- **Stop**: Stop video playback and reset the playhead.
- **Volume Control**: Adjust the volume of the video.
- **Seek Control**: Jump to different positions in the video using a seek slider.
- **Fullscreen Mode**: Toggle between fullscreen and windowed mode.
- **Load Video**: Load and play videos in various formats (`.mp4`, `.avi`, `.mkv`, `.mov`, `.flv`).
- **Error Handling**: Display error messages if any issues occur during playback.

### Requirements
To run the Advanced Video Player, you'll need the following Python libraries:
- `PyQt5`
- `python-vlc`

Install the dependencies via pip:

```bash
pip install PyQt5 python-vlc
```

### Installation and Setup
1. **Clone the Repository**: Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-repo-url.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd your-repo-directory
   ```

3. **Install the Dependencies**: Install the required Python packages listed above by running the following command:

   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure Python is Installed**: Make sure you have Python 3.x installed. You can verify by running:

   ```bash
   python --version
   ```

### How to Use
1. **Launch the Application**: Run the Advanced Video Player application by executing the Python file:

   ```bash
   python VideoPlayer.py
   ```

2. **Usage**:
   - **Load a Video**: Click the "Load Video" button to select a video file (`.mp4`, `.avi`, `.mkv`, `.mov`, `.flv`).
   - **Play/Pause Video**: Use the "Play" button to start playback, and "Pause" to pause it.
   - **Stop Video**: Click the "Stop" button to stop playback and reset the playhead.
   - **Adjust Volume**: Use the volume slider to control the audio level.
   - **Seek in Video**: Drag the seek slider to jump to different parts of the video.
   - **Toggle Fullscreen**: Use the "Fullscreen" button to switch between fullscreen and windowed mode.

### How to Run in VS Code
1. **Open the Project in VS Code**: Launch Visual Studio Code and open the project directory.
2. **Install the Python Extension**: Ensure the Python extension is installed in VS Code.
3. **Run the Application**: Open `VideoPlayer.py` in the editor and click the "Run" button or use the terminal to execute the script:

   ```bash
   python VideoPlayer.py
   ```

---



>>>>>>> 518d513c1d9e16d7537d587da7ce4947e648e35f
