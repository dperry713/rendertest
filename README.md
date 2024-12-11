# Sum Tracker App

This is a simple Flask application that tracks sums of two numbers. Users can submit two numbers and retrieve the results of previous calculations.

## Features
- Add two numbers and store the result
- Retrieve all sums
- Retrieve sums by result

## Requirements
- Python 3.9+
- Flask
- Flask-SQLAlchemy
- Pytest
- Gunicorn

## Running the Application
1. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set the environment variable for the database (optional):
   ```bash
   export DATABASE_URL="your_database_url"  # On Windows: set DATABASE_URL=your_database_url
   ```
4. Run the application:
   ```bash
   python app.py
   ```

## Running Tests
To run the tests, use:
```bash
pytest tests/
```

## Deployment to Render
This application is configured for deployment on Render.com. To deploy:

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Use the following settings:
   - Environment: Python
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

### GitHub Actions Integration
The repository includes GitHub Actions workflow for CI/CD:
1. Runs tests on every push and pull request
2. Automatically deploys to Render when changes are pushed to main branch

To enable automatic deployment:
1. Get your Render API key from the Render dashboard
2. Add the following secrets to your GitHub repository:
   - `RENDER_API_KEY`: Your Render API key
   - `RENDER_SERVICE_ID`: Your Render service ID
