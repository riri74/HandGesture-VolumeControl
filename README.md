## Gesture-Based Volume Control using Pycaw, Mediapipe, and OpenCV

This project demonstrates a hand gesture recognition system that allows you to control the system's volume using the positions of your thumb and index finger. The project leverages the power of:
- **OpenCV**: For real-time video capture and image processing.
- **Mediapipe**: For hand-tracking and detecting the positions of the hand landmarks.
- **Pycaw**: To interact with the system's audio interface and control the volume.

### Features:
- Adjust the system volume by varying the distance between your thumb and index finger.
- Real-time hand tracking with feedback on the screen.
- Visual indicators, such as lines connecting the thumb and index, and a volume bar on the side of the screen.
- Smooth interpolation between hand gestures and volume levels for seamless control.

### How It Works:
- When the distance between the thumb and index finger changes, the system adjusts the volume accordingly.
- When the thumb and index finger are close (less than 50 pixels apart), the volume is set to the minimum, and when farther apart, the volume increases.
- The volume range is mapped to the hand gesture using linear interpolation.

### Requirements:
- Python 3.x
- OpenCV
- Mediapipe
- Pycaw

### Usage:
Run the script, and the webcam will open. Use your index finger and thumb to adjust the volume. Press the **'d'** key to exit the application.

