# Presentation Slides Control

This repository contains code for controlling presentation slides using hand gestures. It uses computer vision techniques to detect hand landmarks and interpret gestures to navigate through a set of presentation images.

## How It Works

1. The code uses the `cvzone` library for hand tracking, `opencv-python` for image and video processing, `numpy` for numerical computations, and `pywin32` to retrieve system metrics.

2. Create your presentation as Images (`.jpg` or `.png`) and replace the slides in the (`/Presentation`)

3. Upon running the script, a camera feed is displayed along with the current presentation slide.

4. Hand gestures are used to control the slides:
   - Raising one finger on the left hand navigates to the previous slide.
   - Raising two fingers on the right hand navigates to the next slide.
   - Pointing the index finger of the right hand highlights a specific area on the slide.

5. The code loads presentation images from a specified folder and displays them as slides.

6. Additional features, such as annotations, can be enabled by uncommenting the relevant code. Annotations allow you to draw on the slide by pointing with your index finger.

7. Pressing the 'q' key terminates the application.

## Dependencies

- [cvzone](https://github.com/cvzone/cvzone): A computer vision library used for hand tracking.
- [OpenCV (cv2)](https://github.com/opencv/opencv): A popular computer vision library used for image and video processing.
- [numpy](https://github.com/numpy/numpy): A powerful library for numerical computing.
- [pywin32](https://github.com/mhammond/pywin32): Required for accessing system metrics.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/presentation-slides-control.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Connect a camera to your computer or device.
2. Adjust the camera parameters (`width` and `height`) in the code to match your camera's resolution.
4. Provide the path to your presentation images folder (`folderpath`) in the code.
4. Run the script:

   ```bash
   python presentation_slides_control.py
   ```

5. The camera feed will be displayed, along with the current presentation slide.
6. Perform hand gestures in front of the camera to control the slides:
   - Raise one finger on your left hand to navigate to the previous slide.
   - Raise two fingers on your right hand to navigate to the next slide.
   - Point your index finger with your right hand to highlight a specific area of the slide.
7. Press the 'q' key to quit the application.

## Notes

- The code assumes there is only one hand in the camera frame.
- The code loads images from the specified folder path and displays them as slides.
- Annotations can be enabled by uncommenting the relevant code. Annotations allow you to draw on the slide by pointing with your index finger.
- Make sure to have the required dependencies installed and accessible in your Python environment.

**Enjoy your interactive presentation experience!**

## License

This project is licensed under the [MIT License](LICENSE).