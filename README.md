# Project-3550-Cybersecurity-35
Enhancing security and user management in the JWKS Server

# Project 3 Flask Application

This repository contains the Project 3 Flask application, designed for secure user registration and authentication. It features AES encryption for data security, utilizing Flask and SQLAlchemy for backend operations and Argon2 for password hashing.

## Features

- **User Registration**: Users can register by providing a username and email, receiving a unique, securely hashed password.
- **User Authentication**: Users can authenticate using their unique user ID to access the system.
- **AES Encrypted Storage**: Sensitive data such as passwords are securely encrypted using AES before storage.

### Prerequisites

You need Python and the following packages:
```bash
pip install flask flask_sqlalchemy argon2-cffi cryptography pytest flask-testing

Setup::
To get started with this project, clone the repository and navigate to the project directory:
git clone https://github.com/sbg0073/Project3.git
cd Project3
Set the environment variable for the AES key::
export NOT_MY_KEY=$(openssl rand -base64 32)

Running the Application
Start the application using:
python3 Project3A.py

The server will run on http://127.0.0.1:8080/.

Running Tests
Execute automated tests with:
pytest test_app.py

Deployment
Notes on how to deploy this on a live system will vary based on the platform (e.g., Docker, Kubernetes, AWS, Azure, or Heroku) and should be tailored based on the specific deployment strategy and environment.

Built With
Flask - Web framework used.
SQLAlchemy - ORM for database interactions.
Argon2 - For hashing passwords securely.
Cryptography - For encrypting sensitive data.
Acknowledgments
Inspiration and code snippets from various Flask tutorials and documentation.


### Instructions for Use:

- **Clone and Setup**: Follow the setup instructions closely to ensure all dependencies are correctly installed and the environment variables are set.
- **Run the Application**: Instructions are clear on how to start the server and access the application.
- **Tests**: Detailed steps on how to run tests to ensure everything is functioning as expected.

