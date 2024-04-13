# Project-3550-Cybersecurity-3550

Enhancing security and user management in the JWKS Server


```bash # Project 3 Flask Application

Welcome to the GitHub repository for Project 3 of the Cybersecurity course. This Flask application is engineered to enhance security and manage user interactions within a JWKS server. It implements AES encryption for private keys, adds robust user registration capabilities, logs authentication requests, and optionally introduces a rate limiter to manage request frequency effectively.

## Features

- **User Registration**: Users can register by providing a username and email, and receive a securely hashed password in return.
- **User Authentication**: Authentication is managed through unique user IDs, ensuring secure access to the system.
- **AES Encrypted Storage**: Critical data, including private keys and passwords, are encrypted using AES encryption to ensure data integrity and security.

## Getting Started

### Prerequisites

Ensure you have Python installed along with the following packages:

pip install flask flask_sqlalchemy argon2-cffi cryptography pytest flask-testing 
```
# Installation
Clone the repository and set up the necessary environment variables:
```bash
git clone https://github.com/sbg0073/Project3.git
cd Project3
export NOT_MY_KEY=$(openssl rand -base64 32)  # Set the AES key
```

# Running the Application
Start the server with the following command:
```bash
python3 Project3A.py
```
# Testing
Run the automated tests to ensure the application's functionality:
```bash
pytest test_app.py
```

# Deployment
Deployment strategies may vary based on the environment (Docker, Kubernetes, AWS, Azure, or Heroku). Customize the deployment steps according to your platform's requirements.

# Built With
Flask: The web framework used for building the application.
SQLAlchemy: Used for database interactions.
Argon2: Utilized for secure password hashing.
Cryptography: Implements encryption mechanisms within the application.

# Acknowledgments
Thanks to various Flask tutorials and documentation that provided insights and code snippets crucial for building this application.

# Additional Notes

Rate Limiting: The optional rate limiter is configured to allow up to 10 requests per second per user, with excess requests receiving a 429 Too Many Requests response.

Logging: Authentication requests are logged with details such as the IP address, timestamp, and user ID.


