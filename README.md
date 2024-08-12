# flask_data_app

Flask Data Processing Application:
    This Flask application simulates a simplified data retrieval and processing system. The application fetches data from a mock API, processes it (e.g., converts text to uppercase and       sums prices), and stores the processed data in memory. The application provides two API endpoints:

    /fetch-data: Fetches and processes the data from the mock API.
    /get-processed-data: Retrieves the processed data stored in memory.

Features:
    Fetch data from a mock API (e.g., Shopify).
    Process the fetched data (e.g., convert text to uppercase, sum prices).
    Store the processed data in memory.
    Retrieve and display processed data via an API endpoint.

Prerequisites:
    Before setting up and running the application, ensure you have the following installed on your machine:
    Python 3.6+
    pip (Python package installer)
    virtualenv (optional but recommended for creating a virtual environment)

Setup Instructions:
    1. Clone the Repository
    First, clone the repository to your local machine:

    git clone https://github.com/your-username/flask_data_app.git
    cd flask_data_app

Set Up a Virtual Environment:
    # Create a virtual environment
    python -m venv venv

    # Activate the virtual environment
    # On Windows:
    venv\Scripts\activate

    # On macOS/Linux:
    source venv/bin/activate

Install Dependencies:
    pip install -r requirements.txt

Run the Application:
    python app.py

Test the API Endpoints:
    http://127.0.0.1:5000/fetch-data
    http://127.0.0.1:5000/get-processed-data

Project Structure:

    flask_data_app/
    │
    ├── venv/                   # Virtual environment directory (created after setup)
    ├── app.py                  # Main Flask application
    ├── requirements.txt        # List of dependencies
    └── README.md               # Documentation (this file)
