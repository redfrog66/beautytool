# Facial recognision beauty tool using OpenCV and Python

The goal of the project is to have an application that has MVC architecture and is aesthetically pleasing, user-friendly.

## Model:
The Model component represents the data and the business logic of the application. The Model will be responsible for handling image processing, facial feature recognition, and any other relevant data operations.

Tasks in the Model:

* Load and preprocess the input image.
* Load the pretrained facial recognition model.
* Detect facial regions in the preprocessed image.
* Extract facial features from the detected regions.
* Perform facial feature recognition tasks (e.g., eye detection, smile detection, expression recognition).

## View:
The View component is responsible for presenting the information to the user and receiving their input. We will create a GUI, so the View will be mainly concerned with the visual representation of the app.

Tasks in the View:

* Design and create the graphical user interface (if applicable) to display the input image and the detected facial features.
* Show the results of facial feature recognition to the user.
* Handle user input for interacting with the app, such as loading images, selecting options, or performing specific actions.

## Controller:
The Controller component acts as an intermediary between the Model and the View. It handles user input, processes it, and updates the Model accordingly. The Controller also ensures that the Model's data is correctly reflected in the View.

Tasks in the Controller:

* Receive user input from the View (e.g., when the user loads an image or interacts with the app).
* Pass the input image to the Model for processing.
* Receive the results of facial feature recognition from the Model.
* Update the View with the results obtained from the Model.