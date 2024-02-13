# FastAPI
# Overview
This program is a Python-based API developed using FastAPI, designed to interact with an in-memory database. The API provides a simple interface to create, retrieve, list, and delete data represented as a chosen data model.

# Features
- In-Memory Database: Utilizes a custom DataBase class to simulate database operations in memory.
- CRUD Operations: Supports Create, Read, Update, and Delete operations on the data model through API endpoints.
- Fully Tested: Includes a suite of unit tests to ensure that all API endpoints function as expected.
- Data Model Flexibility: The data model can be adapted to various use cases.
- Virtual Environment: Leverages a virtual environment for dependency management and isolation.

# Getting Started
To get started with this API, you should set up a virtual environment and install the required dependencies as outlined in the provided Pipfile.

# Set Up Virtual Environment
Install pipenv if you haven't already.
Navigate to the project's root directory and run pipenv install to create a virtual environment and install dependencies.

# Running the API
Activate the virtual environment with pipenv shell.
Start the FastAPI server with hypercorn main:app --reload.

# Running Tests
To ensure that the API is functioning correctly, run the tests using the following command:
pytest
