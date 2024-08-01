# Sign Language Tracker Prototype

## Overview

The Sign Language Tracker Prototype is a web application designed to recognize and count sign language gestures using a combination of React for the frontend and OpenCV for computer vision tasks. This prototype demonstrates the basic functionality of tracking and counting sign language gestures in real-time.

## Features

- Real-time sign language gesture detection
- Gesture counting functionality
- Built with React for a dynamic user interface
- Utilizes OpenCV for computer vision tasks

## Technologies Used

- **React**: A JavaScript library for building user interfaces.
- **OpenCV**: An open-source computer vision library used for real-time image processing and gesture detection.

## Installation

To get started with the project, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/sign-language-tracker.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd sign-language-tracker
    ```

3. **Install the necessary dependencies:**

    - **Frontend (React):**

        ```bash
        cd client
        npm install
        ```

    - **Backend (OpenCV):**

        ```bash
        cd server
        pip install -r requirements.txt
        ```

4. **Start the development server:**

    - **Frontend:**

        ```bash
        cd client
        npm start
        ```

    - **Backend:**

        ```bash
        cd server
        python app.py
        ```

    The frontend application should now be running at `http://localhost:3000`, and the backend server should be running at `http://localhost:3000`.

## Usage

- Open the web application in your browser.
- Allow the application to access your webcam.
- Perform sign language gestures in front of the camera.
- The application will detect and count the gestures in real-time.

## Acknowledgments

- [React](https://reactjs.org/) - For building the user interface.
- [OpenCV](https://opencv.org/) - For computer vision functionalities.


Thank you for checking out the Sign Language Tracker Prototype!
