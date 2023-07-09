# Elevator System

This repository contains the source code for an Elevator System implemented using Django and Django REST Framework.

## Features

- Elevator model with status, current floor, and direction fields
- Request model to handle floor requests for elevators
- API endpoints to manage elevators and requests
- Serializers for data serialization
- Viewsets to handle CRUD operations
- Django project configuration and settings

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/elevator-system.git

2. Move to the project directory: cd elevator-system
   
3. Create a virtual environment (optional but recommended): python -m venv venv

4. Activate the virtual environment:

- For Windows: venv\Scripts\activate
- For macOS and Linux: source venv/bin/activate

5. Install the following dependencies:

Django: pip install django

Django Rest Framework: pip install djangorestframework

Core API: pip install coreapi


6. Apply database migrations:
- python manage.py migrate

7. Start the development server:
- python manage.py runserver

### Access the API endpoints at http://localhost:8000/api/elevators/ and http://localhost:8000/api/requests/.

# Video Demonstration
Check out the video demonstration to see the Django Elevator System in action - [click here](<https://drive.google.com/file/d/1BuNRrR036NOEz0lpQ5Fbc9O028wqnHER/view?usp=drivesdk>)

# Usage

* Elevator API Endpoints:

    * GET /api/elevators/: Get a list of all elevators.
    * GET /api/elevators/{id}/: Get details of a specific elevator.
    * POST /api/elevators/: Create a new elevator.
    * PUT /api/elevators/{id}/: Update details of a specific elevator.
    * DELETE /api/elevators/{id}/: Delete a specific elevator.
  
* Request API Endpoints:

    * GET /api/requests/: Get a list of all requests.
    * GET /api/requests/{id}/: Get details of a specific request.
    * POST /api/requests/: Create a new request.
    * PUT /api/requests/{id}/: Update details of a specific request.
    * DELETE /api/requests/{id}/: Delete a specific request.

# Contributing
Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

When contributing, please ensure that your code adheres to the existing code style and conventions. Also, provide clear and descriptive commit messages.
   
Please ensure that your code adheres to the existing coding style and includes appropriate tests and documentation.

# License
This project is licensed under the MIT License.

# Acknowledgements
Special thanks to the contributors of the Django and Django Rest Framework communities for their excellent frameworks.
