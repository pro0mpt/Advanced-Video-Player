import sys
import vlc
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QSlider,
    QHBoxLayout, QLabel, QFileDialog, QMessageBox
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon

class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Advanced Video Player")
        self.setGeometry(100, 100, 800, 600)

        self.instance = vlc.Instance("--no-xlib --file-caching=3000 --network-caching=3000")
        self.player = self.instance.media_player_new()

        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)
        self.vbox = QVBoxLayout()
        self.widget.setLayout(self.vbox)

        # Video Frame
        self.video_frame = QWidget(self)
        self.vbox.addWidget(self.video_frame)

        self.player.set_hwnd(self.video_frame.winId())

        # Control Layout
        self.control_layout = QHBoxLayout()

        # Play Button
        self.play_button = QPushButton("Play")
        self.play_button.setIcon(QIcon.fromTheme("media-playback-start"))
        self.control_layout.addWidget(self.play_button)
        self.play_button.clicked.connect(self.play_pause_video)

        # Stop Button
        self.stop_button = QPushButton("Stop")
        self.stop_button.setIcon(QIcon.fromTheme("media-playback-stop"))
        self.control_layout.addWidget(self.stop_button)
        self.stop_button.clicked.connect(self.stop_video)

        # Volume Slider
        self.volume_slider = QSlider(Qt.Horizontal, self)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setValue(50)
        self.player.audio_set_volume(50)
        self.control_layout.addWidget(QLabel("Volume"))
        self.control_layout.addWidget(self.volume_slider)
        self.volume_slider.valueChanged.connect(self.set_volume)

        # Seek Slider
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setMaximum(1000)
        self.control_layout.addWidget(self.slider)
        self.slider.sliderMoved.connect(self.set_position)

        # Fullscreen Button
        self.fullscreen_button = QPushButton("Fullscreen")
        self.fullscreen_button.setIcon(QIcon.fromTheme("view-fullscreen"))
        self.control_layout.addWidget(self.fullscreen_button)
        self.fullscreen_button.clicked.connect(self.toggle_fullscreen)

        # Load Video Button
        self.load_button = QPushButton("Load Video")
        self.load_button.setIcon(QIcon.fromTheme("document-open"))
        self.control_layout.addWidget(self.load_button)
        self.load_button.clicked.connect(self.load_video)

        # Add control layout to the main layout
        self.vbox.addLayout(self.control_layout)

        # Timer for updating the slider
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_slider)
        self.timer.start()

        # Error handling for media player
        self.player.event_manager().event_attach(vlc.EventType.MediaPlayerEncounteredError, self.handle_error)

        self.is_fullscreen = False

    def load_video(self):
        # Load video file
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(self, "Open Video File", "", "Video Files (*.mp4 *.avi *.mkv *.mov *.flv)")
        if file_path:
            media = self.instance.media_new(file_path)
            self.player.set_media(media)
            self.play_video()
        else:
            QMessageBox.warning(self, "No File Selected", "Please select a video file to load.")

    def play_video(self):
        self.player.play()

    def play_pause_video(self):
        if self.player.is_playing():
            self.player.pause()
            self.play_button.setText("Play")
            self.play_button.setIcon(QIcon.fromTheme("media-playback-start"))
        else:
            self.player.play()
            self.play_button.setText("Pause")
            self.play_button.setIcon(QIcon.fromTheme("media-playback-pause"))

    def stop_video(self):
        self.player.stop()
        self.play_button.setText("Play")
        self.play_button.setIcon(QIcon.fromTheme("media-playback-start"))
        self.slider.setValue(0)

    def set_volume(self, volume):
        self.player.audio_set_volume(volume)

    def set_position(self, position):
        self.player.set_position(position / 1000.0)

    def update_slider(self):
        # Update the slider to reflect the current position in the video
        if self.player.is_playing():
            self.slider.setValue(int(self.player.get_position() * 1000))

    def toggle_fullscreen(self):
        if self.is_fullscreen:
            self.showNormal()
            self.is_fullscreen = False
        else:
            self.showFullScreen()
            self.is_fullscreen = True

    def handle_error(self, event):
        QMessageBox.critical(self, "Error", "An error occurred during playback.")
        self.stop_video()

    def closeEvent(self, event):
        self.player.stop()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.show()
    sys.exit(app.exec_())
