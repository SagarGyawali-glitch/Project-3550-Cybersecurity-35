# Project-3550-Cybersecurity-35
Enhancing security and user management in the JWKS Server

# Project 3 Flask Application

This repository contains the Project 3 Flask application, designed for secure user registration and authentication as part of Project-3550-Cybersecurity-35. It features AES encryption for data security, utilizing Flask and SQLAlchemy for backend operations and Argon2 for password hashing.

## Features

- **User Registration**: Users can register by providing a username and email, receiving a unique, securely hashed password.
- **User Authentication**: Users can authenticate using their unique user ID to access the system.
- **AES Encrypted Storage**: Sensitive data such as passwords are securely encrypted using AES before storage.

## Prerequisites

You will need Python installed on your machine, along with the following packages:

```bash

pip install flask flask_sqlalchemy argon2-cffi cryptography pytest flask-testing

Setup
To get started with this project, clone the repository and navigate to the project directory:

git clone https://github.com/sbg0073/Project3.git
cd Project3
Set the environment variable for the AES key:

export NOT_MY_KEY=$(openssl rand -base64 32)

Running the Application

Start the application using:

python3 Project3A.py
The server will run on http://127.0.0.1:8080/.

Running Tests

Execute automated tests with:

pytest test_app.py

Deployment:

Notes on how to deploy this on a live system will vary based on the platform (e.g., Docker, Kubernetes, AWS, Azure, or Heroku) and should be tailored based on the specific deployment strategy and environment.

Built With:

Flask: The web framework used.
SQLAlchemy: ORM for database interactions.
Argon2: For hashing passwords securely.
Cryptography: Used for encrypting sensitive data.

Acknowledgments: 
Inspiration and code snippets from various Flask tutorials and documentation.
![image](https://github.com/SagarGyawali-glitch/Project-3550-Cybersecurity-35/assets/115506851/ec3bf836-25f0-42e4-942a-cd18be94e8ae)
