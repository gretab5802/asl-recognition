import cv2
import numpy as np
import mediapipe as mp
from mediapipe.framework.formats import landmark_pb2
from mediapipe.tasks.python import vision
import zipfile
from picamera import PiCamera
from picamera.array import PiRGBArray
import time
import subprocess

def install_libraries():
    # Installs necessary Python libraries
    subprocess.run(['pip', 'install', 'mediapipe', 'opencv-python', 'picamera', 'numpy'])

def take_picture():
    # Initializes Raspberry Pi camera, captures a single image, saves it as 'photo.jpg'
    camera = PiCamera()
    camera.resolution = (640, 480)  # Set the resolution of the camera
    camera.framerate = 32           # Set the framerate
    rawCapture = PiRGBArray(camera, size=(640, 480))

    # Allow the camera to warm up
    time.sleep(0.1)

    # Capture the image to a NumPy array and then save it as 'photo.jpg'
    camera.capture(rawCapture, format="bgr")
    image = rawCapture.array
    cv2.imwrite('photo.jpg', image)
    return 'photo.jpg'

def coord_matrix(photo_name):
    # Uses Mediapipe to detect hand landmarks from an image file,
    # converts these landmarks into x, y, and z coordinates
    base_options = mp.python.BaseOptions(model_asset_path='hand_landmarker.task')
    options = vision.HandLandmarkerOptions(base_options=base_options, num_hands=2)
    detector = vision.HandLandmarker.create_from_options(options)
    image = mp.Image.create_from_file(photo_name)
    detection_result = detector.detect(image)

    hand_landmarks_list = detection_result.hand_landmarks

    if hand_landmarks_list:
        hand_landmarks = hand_landmarks_list[0]  # Use the first hand detected
        x_coords = [landmark.x for landmark in hand_landmarks.landmark]
        y_coords = [landmark.y for landmark in hand_landmarks.landmark]
        z_coords = [landmark.z for landmark in hand_landmarks.landmark]

        return np.array([x_coords, y_coords, z_coords])
    return None

def load_gestures():
    # Processes hand gestures from zip file and returns a list of matrices representing the gestures
    gestures = []
    with zipfile.ZipFile("match.zip", "r") as z:
        for filename in z.namelist():
            if filename.endswith('.jpg'):
                z.extract(filename, path="/tmp")  # Extract to temp directory
                matrix = coord_matrix(f"/tmp/{filename}")
                if matrix is not None:
                    gestures.append(matrix)
    return gestures

def build_svd_model(gestures):
    # Builds SVD model from gesture matrices, computes U, sigma, and V^T
    A = np.hstack([gesture.reshape((-1, 1)) for gesture in gestures])
    A_bar = A - np.mean(A, axis=1, keepdims=True)  # Center the matrix
    U, sigma, V_T = np.linalg.svd(A_bar, full_matrices=False)
    return U, sigma, V_T

def guess_image(photo_name, U, sigma, V_T):
    # Uses the SVD model to find closest gesture to provided image
    test_matrix = coord_matrix(photo_name)
    if test_matrix is not None:
        z_1 = test_matrix.reshape((-1, 1))
        z_1_bar = z_1 - np.mean(z_1)
        w_1 = U.T @ z_1_bar

        distances = np.linalg.norm(V_T - w_1, axis=1)
        nearest_index = np.argmin(distances)
        return chr(65 + nearest_index)  # Return gesture label as a character, 'A' begins at 65
    return "No hand detected"

def main():
    install_libraries()      # Install required libraries (only needed once)
    photo_name = take_picture()  # Capture a photo from the camera
    gestures = load_gestures()  # Load and process gestures from a zip file
    U, sigma, V_T = build_svd_model(gestures)  # Build the SVD model from gestures
    result = guess_image(photo_name, U, sigma, V_T)  # Guess the gesture in the captured photo
    print(f"The gesture is: {result}")

if __name__ == "__main__":
    main()
