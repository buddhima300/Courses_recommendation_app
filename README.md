

---

```markdown
# University Recommendation API

This project is a **FastAPI-based application** for recommending universities based on course names. It uses a pre-trained machine learning model (`courses_recommender.joblib`) to provide predictions and supports both GET and POST methods for interacting with the API.

## Features

- **Course Recommendations**: Get university recommendations for specific courses.
- **Pre-trained ML Model**: Uses a `.joblib` model file for predictions.
- **Endpoints**:
  - `/`: Root endpoint that provides a welcome message.
  - `/university`: Get the top university for a given course name.
  - `/university/predict`: Predict the university ranking for a given course.

## Requirements

Make sure the following dependencies are installed before running the application:

- Python 3.10+
- FastAPI
- Uvicorn
- Joblib

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure the model file (`courses_recommender.joblib`) is present in the root directory.

## Usage

### Running Locally

Start the FastAPI application:

```bash
uvicorn app:app --host 127.0.0.1 --port 8000
```

The API will be available at `http://127.0.0.1:8000`.

### API Endpoints

#### 1. **Root Endpoint**
   - **URL**: `/`
   - **Method**: GET
   - **Description**: Returns a welcome message.

#### 2. **Top University Endpoint**
   - **URL**: `/university`
   - **Method**: GET
   - **Parameters**:
     - `course_name` (str): Name of the course.
   - **Response**:
     ```json
     {
       "course_name": "Course Name",
       "top_university": "Recommended University"
     }
     ```
   - **Error**:
     ```json
     {
       "detail": "Course not found"
     }
     ```

#### 3. **Prediction Endpoint**
   - **URL**: `/university/predict`
   - **Method**: POST
   - **Request Body**:
     ```json
     {
       "course_name": "Course Name"
     }
     ```
   - **Response**:
     ```json
     {
       "prediction": "Predicted University"
     }
     ```
   - **Error**:
     ```json
     {
       "detail": "Course name must be provided"
     }
     ```

## Deployment

### Deploying on Railway
1. Create a Railway project.
2. Add the repository to Railway.
3. Configure environment variables and files:
   - `requirements.txt`
   - Python version (e.g., 3.10)
4. Run the build process.

### Deploying on PythonAnywhere
1. Upload your code files to PythonAnywhere.
2. Set up a new web application with `Flask` or `FastAPI` as the framework.
3. Add the `app.py` file in the **WSGI** configuration.
4. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Reload the web application.

## Files in the Repository

- `app.py`: FastAPI application code.
- `courses_recommender.joblib`: Pre-trained machine learning model.
- `requirements.txt`: Python dependencies.
- `CourseData.py`: Pydantic schema for request validation.
- `Coursera.csv`: Dataset used for recommendations.
- `README.md`: Documentation.

## License

This project is licensed under the MIT License.

## Author

Created by Buddhima chathuranga lakmal.
```
