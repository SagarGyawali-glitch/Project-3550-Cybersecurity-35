# Project-3550-Cybersecurity-35
Enhancing security and user management in the JWKS Server

# Project 3 Flask Application

This repository contains the Project 3 Flask application, designed for secure user registration and authentication. It features AES encryption for data security, utilizing Flask and SQLAlchemy for backend operations and Argon2 for password hashing.

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
