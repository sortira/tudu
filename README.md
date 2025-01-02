# To-Do App with Authentication (Flask & Firebase)

This To-Do app is a simple web application built with Flask and Firebase, designed to help users manage their tasks securely. It includes authentication features using Firebase to allow users to sign up, log in, and manage their tasks.

## Purpose
This project serves as an attempt to learn user authentication with Flask and Firebase. It provides a secure, personalized experience for managing tasks. Firebase is used for both user authentication and storing the tasks in the Firestore database.

## Features
- **User Authentication**: Users can sign up, log in, and log out securely.
- **Task Management**: Authenticated users can add, view, and delete tasks from their To-Do list.
- **Real-Time Database**: Tasks are stored in Firebase Firestore, providing real-time updates across devices.
- **Dark Mode**: The app features a modern dark mode design for a minimalistic, user-friendly interface.

## Technologies Used
- **Flask**: A lightweight Python web framework for building the app.
- **Firebase**: Used for user authentication and Firestore database for storing tasks.
- **HTML/CSS**: For structuring and styling the app.
- **Bootstrap**: For responsive and modern UI components.
- **Animate.css**: For adding smooth animations to the UI.

## Installation

### Prerequisites
To run this project locally, you will need:
- Python 3.6 or higher
- Firebase account and Firestore database

How to Use

    Sign Up: Create a new account by providing an email, password, and username.
    Login: After signing up, you can log in using your email and password.
    Add Tasks: Once logged in, you can add new tasks to your To-Do list.
    Delete Tasks: You can remove tasks from your list by clicking the "Delete" button next to each task.
    Logout: You can log out at any time to securely end your session.

Folder Structure

/todo-app-flask-firebase
│
├── app.py                # Main Flask application
├── templates/            # HTML templates (home, login, signup)
│   ├── home.html
│   ├── login.html
│   └── signup.html
├── static/               # Static files (CSS, JS)
│   └── styles.css

License

This project is open-source and available under the MIT License.


### Key Sections in the README:
1. **Project Purpose and Features**: Describes the goal of the app and its features.
2. **Technologies Used**: Lists the main technologies used in the project.
3. **Installation**: Provides instructions on setting up the project locally.
4. **How to Use**: A simple guide to help users interact with the app.
5. **Folder Structure**: Helps users understand the organization of files within the project.
6. **License**: Includes licensing information (MIT License, in this case).
