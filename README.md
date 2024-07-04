# MyBTP

MyBTP is a platform designed to facilitate interactions between students and professors regarding thesis projects. Built using Flask as the backend and MySQL as the database, MyBTP allows students to apply for various thesis projects under different professors and enables professors to manage applications and project topics efficiently.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [License](#license)
- [Contact](#contact)

## Features

- **Student Functionality**:
  - View available thesis projects.
  - Apply for projects under different professors.
  - Choose one professor from the accepted requests.
  - View and track application status.

- **Professor Functionality**:
  - Approve or decline student requests.
  - Update and manage project topics.
  - Set cutoff criteria (e.g., CGPA) for applications.
  - Sort and filter applications by CGPA, department, etc.

## Installation

### Prerequisites

- Python 3.7+
- MySQL Server
- Flask and other required Python packages (listed in `requirements.txt`)

### Steps

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/guru-divine/MyBTP.git
    cd mybtp
    ```

2. **Install Dependencies**:

    Create a virtual environment and install the necessary packages:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Configure MySQL**:

    - Create a MySQL database for MyBTP.
    - Update the database configuration in `config.py`.

4. **Initialize the Database**:

    Run the script to create necessary tables:

    ```bash
    flask db upgrade
    ```

5. **Run the Application**:

    ```bash
    flask run
    ```

    The application will be available at `http://127.0.0.1:5000`.

## Configuration

Edit the `config.py` file to configure the database and application settings:

```python
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/mybtp_db'
    SECRET_KEY = 'your_secret_key'
```

## Usage
1. **For students**:
   - Register and log in to the platform.
   - Browse available thesis projects.
   - Apply for projects and track application status.
2. **For professors**:
   - Log in to manage projects and student applications.
   - Approve or decline student applications.
   - Update project details and cutoff criteria.

## Screenshots

### Student Dashboard

### Professor Dashboard

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any queries or suggestions, please contact [divya.raj5935@gmail.com].
