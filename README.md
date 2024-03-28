# Note-Taking Application

This is a simple note-taking application built with FastAPI, and MongoDB. It allows users to register, login, create, view, update, and delete notes.

## Project Structure

- `app/`: Contains the source code for the FastAPI application.
  - `main.py`: Main FastAPI application file with endpoint definitions.
  - `auth.py`: Handles user authentication and authorization.
  - `crud.py`: Implements CRUD operations for notes.
  - `db_config.py`: Establishes connection to MongoDB database.
  - `models.py`: Defines Pydantic models for request/response validation.
- `Dockerfile`: Defines Docker configuration for containerizing the application.
- `requirements.txt`: Lists Python dependencies for the application.
- `README.md`: Documentation file (you're currently reading it!).

## Installation and Setup

1. Ensure you have Python 3.9 or later installed on your system.
2. Install Docker if you haven't already (for containerization).
3. Clone this repository:

   ```bash
   git clone https://github.com/GargAnshu9468/note-taking-app.git
4. Navigate to the project directory:

    ```bash
    cd note-taking-app
5. Install Python dependencies:

    ```bash
    pip install -r app/requirements.txt
6. Set up MongoDB on your local machine.
7. Run the application:

    ```bash
    uvicorn main:app --host localhost --port 8000

## Building and Running the Application with Docker

1. Build the Docker image:

    ```bash
    docker build -t note-taking-app .
2. Run the Docker container:

    ```bash
    docker run -d -p 8000:8000 note-taking-app
3. Access the application in your web browser at http://localhost:8000.

## API Documentation

The API documentation is automatically generated by FastAPI and can be accessed at http://localhost:8000/docs.

## Usage

1. Register a new user using the /register endpoint.
2. Log in with the registered user using the /login endpoint to obtain an access token.
3. Use the obtained access token to authenticate and access other endpoints for creating, viewing, updating, and deleting notes.
