# ShaqDetector

## Description

ShaqDetector is a facial recognition application built with React, Flask, and TensorFlow, that identifies the presence of Shaquille O'Neal in images with a high level of accuracy. Powered by a convolutional neural network (CNN), this project showcases a deep learning model, along with the integration of frontend and backend technologies for image analysis.

## Table of Contents

- [Overview](#overview)
- [Get Started Guide](#get-started)
- [Thanks](#thanks)

## Overview

ShaqDetector leverages machine learning to recognize Shaquille O'Neal's face in images. The project is divided into three main components:

- **Flask Backend (flask-backend):**
  - A Python Flask application responsible for receiving images from the React frontend.
  - Utilizes a face detection algorithm and a pre-trained CNN to predict the presence of Shaq in the images.
  - The `shape_predictor_68_face_landmarks.dat` file and the zipped CNN model are included in this folder.

- **React Frontend (react-frontend):**
  - The frontend of the application built using React.
  - Allows users to upload images for analysis and displays the results from the Flask backend.

- **Notebooks (notebooks):**
  - Contains Jupyter notebooks used for creating and training the CNN.
  - Includes 681 images of Shaquille O'Neal used in training, but not the Labeled Faces in the Wild (LFW) dataset which is avalable publicly elsewhere.


## CNN Performance

### Model Training Details

- **Framework:** TensorFlow (latest version)
- **Architecture:** Transfer learning using VGG16 model with frozen convolutional layers, and incorperating a single dense layer, followed by a dropout layer (0.5) and an output layer using the fostmax activation function
- **Loss Function:** Sparse Categorical Crossentropy
- **Optimzer:** Adam
- **Number of Epochs:** 10
- **Accuracy:** 99.24%
- **Loss:** 0.0279

### Training Data

- **Shaquille O'Neal Images:** 681 images containing Shaq, augmented to 1420 (cropped around the face)
- **LFW Dataset:** 1500 image subset randomly selected and used for training

### Training Environment

The CNN was trained on a 2021 M1 Pro 14" MacBook Pro, showcasing its efficiency in handling deep learning tasks. The use of transfer learning from the VGG16 model, combined with data augmentation, contributed to the model's robustness.

### Performance Metrics

- **Accuracy:** Achieved an impressive accuracy of 99.24%, indicating the model's capability to accurately recognize Shaquille O'Neal's face in various conditions.
- **Loss:** Minimal loss of 0.0279 demonstrates the effectiveness of the training process in minimizing errors.

The high accuracy and low loss highlight the success of the CNN in achieving the desired facial recognition outcomes.

## Get Started

### 1. Clone the Repository

git clone https://github.com/LiamJ009/Shaq-Detector.git
cd Shaq-Detector

### 2. Unzip CNN Files

In the flask-backend folder, locate the zipped CNN files (shaq-facial-CNN.zip). Unzip them to extract the necessary model files.

### 3. Downalod LFW Dataset (Optional)

For model training, download the Labled Faces in the Wild (LFW) dataset. You can find it at http://vis-www.cs.umass.edu/lfw/. Extract the dataset and place it in the notebooks folder.

### 4. Install Required Dependencies

#### Frontend (React)
Node.js, React, Axios

#### Backend (Flask)
Python, Flask, Flask-CORS

#### Machine Learning
OpenCV, Dlib, NumPy, TensorFlow

#### Model Training (Jupyter Notebook)
Pandas, OS, Shutil, Matplotlib

#### Python Libraries
cv2, dlib, NumPy, Random, TensorFlow, Keras, ImageDataGenerator

#### Additional Libraries
Axios (Frontend HTTP requests), Matplotlib (Data visualization)

### 5. Run the Application

Start the React Frontend:
cd react-frontend
npm start

Start the Flask backend:
cd flask-backend
python app.py

Open your browser and navigate to http://localhost:3000 to use the ShaqDetect application.

## Thanks for Viewing my Project!
