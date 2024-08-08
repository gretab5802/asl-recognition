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
    git clone https://github.com/gretab5802/asl-recognition.git
    cd asl-recognition
    ```

3. **Prepare the Dataset:**
    Ensure you have the `match.zip` containing the training images in the project's root directory. The training images were taken manually by the group members and are not provided in this repository. To prepare your dataset, simply take pictures of every letter in the ASL alphabet and put them in a `match.zip` or equivalent. We excluded ASL letters 'j' and 'z' because of the non-static nature of the letters.

## Execution
To run the application, execute the main script from the terminal:

```bash
python cleaned_hand_landmark_test.py
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

## License
MIT License

Copyright (c) 2024 Greta Brown

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
