from flask import Flask, request, jsonify
from flask_cors import CORS

import cv2
import dlib
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import array_to_img

app = Flask(__name__)

# Allow CORS for the /detect_shaq route
cors = CORS(app, resources={
            r"/detect_shaq": {"origins": "*"}})

# Load the TensorFlow model
model = tf.keras.models.load_model('shaq-facial-CNN')

# Initialize the Dlib face detector and shape predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

preprocessed_faces = []


def align_and_crop_faces(image, padding=50):

    # Convert the image to grayscale for face detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = detector(gray)

    # Check if a face is detected
    if len(faces) > 0:

        for face in faces:

            # Get the facial landmarks for face alignment
            shape = predictor(gray, face)

            # Define the coordinates for the eyes
            left_eye = shape.part(36)  # Left eye
            right_eye = shape.part(45)  # Right eye

            # Calculate the angle for rotation (to make eyes horizontal)
            angle = np.arctan2(right_eye.y - left_eye.y,
                               right_eye.x - left_eye.x)
            angle = np.degrees(angle)

            # Calculate new coordinates for cropping without padding
            x = max(0, face.left() - padding)
            y = max(0, face.top() - padding)
            w = min(image.shape[1], face.right() + padding) - x
            h = min(image.shape[0], face.bottom() + padding) - y

            # Crop the image with the new coordinates
            cropped_face = image[y:y+h, x:x+w]

            # Check if the cropped face is not empty
            if not cropped_face.size == 0:
                preprocessed_faces.append(cropped_face)


@app.route('/detect_shaq', methods=['POST'])
def detect_shaq():
    # Get the image file from the request
    file = request.files['image']

    # Read the image
    image = cv2.imdecode(np.frombuffer(
        file.read(), np.uint8), cv2.IMREAD_COLOR)

    no_faces = False

    try:
        # Perform face detection and extract the face
        align_and_crop_faces(image)
    except:
        no_faces = True

    # Check if no faces were detected
    if no_faces:
        return jsonify({'error': 'No faces detected in image!'})

    predictions = []

    stored_predictions = []

    for face in preprocessed_faces:

        # save the face as an imahe
        cv2.imwrite('face.jpg', face)

        img = keras.preprocessing.image.load_img(
            "face.jpg", target_size=(256, 256))

        img_array = keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)

        predictions = model.predict(img_array)

        stored_predictions.append(predictions)

    max_score = 0
    index = 0
    i = 0

    # Find the highest scoring prediction and its index
    for prediction in stored_predictions:

        if prediction[0][1] > max_score:
            max_score = prediction[0][1]
            index = i
        i += 1

    # Extract the highest scoring prediction result
    prediction_result = {
        'shaq_probability': float(stored_predictions[index][0][1]),
        'no_shaq_probability': float(stored_predictions[index][0][0])
    }

    # Clear the array for the next request
    preprocessed_faces.clear()

    return jsonify(prediction_result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
