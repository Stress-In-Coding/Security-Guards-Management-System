Security Guards Management API

Overview

The Security Guards Management API is a RESTful service built using Flask and SQLAlchemy. It manages clients, employees, employee categories, and assignments for a security guards management system. The API includes features such as CRUD operations, JWT authentication, and unit testing.

Features

CRUD Operations: Manage clients, employees, and employee categories.

JWT Authentication: Secure access with token-based authentication.

Unit Testing: Comprehensive test coverage using unittest.

Endpoints

Clients

Get All Clients

GET /clients

Response: List of clients.

Add a New Client

POST /clients

Request Body: { "client_details": "string" }

Update a Client

PUT /clients/<client_id>

Request Body: { "client_details": "string" }

Delete a Client

DELETE /clients/<client_id>

Employees

Get All Employees

GET /employees

Response: List of employees.

Add a New Employee

POST /employees

Request Body: { "category_code": "string", "employee_details": "string" }

Update an Employee

PUT /employees/<employee_id>

Request Body: { "category_code": "string", "employee_details": "string" }

Delete an Employee

DELETE /employees/<employee_id>

Authentication

Login

POST /login

Request Body: { "username": "string", "password": "string" }

Response: { "token": "JWT token" }

Protected Route

GET /protected

Header: Authorization: <JWT token>

Setup

Clone the repository.

Install dependencies:

pip install -r requirements.txt

Run the application:

python security_guards_api.py

Access the API at http://localhost:5000.

Testing

Run the test suite:

python -m unittest security_guards_api.py

Ensure all tests pass.

Deployment

Deploy the application on PythonAnywhere.

Upload the project files and configure the web app.

Verify endpoints via the provided domain.

Database Schema

clients: Stores client details.

employee_category: Stores categories of employees.

employees: Stores employee details linked to categories.

Future Improvements

Add endpoints for managing assignments and training courses.

Implement pagination for large datasets.

Enhance role-based access control for finer-grained permissions.


