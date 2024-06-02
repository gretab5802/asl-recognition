# ASL Recognition with Raspberry Pi and MediaPipe

## Project Description
This project aims to facilitate communication between hearing individuals and those who are deaf or hard of hearing by developing a computer vision application that interprets American Sign Language (ASL). Utilizing MediaPipe's Hand Landmark Detection and Singular Value Decomposition (SVD), this system translates visual language into text through real-time ASL recognition.

Developed by Greta Brown and Nathaniel Grenke as part of the CSCI 4511W course, this application leverages the Raspberry Pi Camera Module 2 to capture images which are then processed to detect and recognize ASL gestures.

## Key Features
- Real-time ASL gesture recognition.
- Uses MediaPipe for hand landmark detection.
- Employs SVD for gesture classification based on the ASL alphabet.

## Dependencies
- Python 3.7 or higher
- OpenCV
- MediaPipe
- NumPy
- PiCamera

## Installation
First, ensure that your Raspberry Pi is set up and connected to the Camera Module. A Camera Module 2 was used for our testing. Follow these steps to prepare your system:

1. **Install the Required Libraries:**
    ```bash
    pip install opencv-python mediapipe numpy picamera
    ```

2. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourgithub/ASL_Recognition_RPi.git
    cd ASL_Recognition_RPi
    ```

3. **Prepare the Dataset:**
    Ensure you have the `match.zip` containing the training images in the project's root directory. The training images were taken manually by the group members and are not provided in this repository. To prepare your dataset, simply take pictures of every letter in the ASL alphabet and put them in a `match.zip` or equivalent. We excluded ASL letters 'j' and 'z' because of the non-static nature of the letters.

## Execution
To run the application, execute the main script from the terminal:

```bash
python asl_recognition.py
```

The script will:
* Initialize the camera and capture a photo.
* Detect hand landmarks in the captured image.
* Classify the gesture using a pre-trained SVD model.
* Print the recognized gesture to the console.

## Project Structure
* `cleaned_hand_landmark_test.py`: The main Python script for gesture recognition.
* `match.zip`: Zip file containing gesture images used for training the SVD model.

## Authors
Greta Brown <br />
Nathaniel Grenke

## Acknowledgments
Thanks to the instructors and colleagues in CSCI 4511W for their support and insights throughout the project development.
