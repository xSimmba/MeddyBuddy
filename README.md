# MeddyBuddy

MeddyBuddy is an AgeTech project designed to help elderly people keep track of their medications. It's a web application built using Django that allows users to manage medications, view details, and receive reminders.

## Features

- User authentication (registration, login, logout)
- Profile management
- Add, edit, and delete medications
- Medication detail view
- Responsive UI with a user-friendly interface

## Technologies Used

- Python 3.12
- Django 5.1.2
- PostgreSQL
- HTML, CSS, JavaScript

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/CodeZobac/meddybuddy.git
    ```
2. Navigate to the project directory:
    ```bash
    cd meddybuddy
    ```
3. Install dependencies using Poetry:
    ```bash
    poetry install
    ```
4. Create and configure the `.env` file:
    ```bash
    cp .env.example .env
    ```
    Update the `.env` file with your database credentials and secret key.

5. Apply migrations:
    ```bash
    poetry run python manage.py migrate
    ```
6. Run the development server:
    ```bash
    poetry run python manage.py runserver
    ```

## Usage

- Access the application at `http://localhost:8000/`.
- Register a new account or log in with your credentials.
- Add new medications, view medication details, and manage your profile.

## Contributing

The team that helped create this app are:
- Luis 
- Luka
- Sebastião
- Miguel

## License

This project is licensed under the MIT License.
