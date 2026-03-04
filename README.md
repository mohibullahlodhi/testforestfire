# FWI Prediction Web Application

A Flask-based web application for predicting the Fire Weather Index (FWI) using machine learning. This application uses a trained Ridge regression model to forecast fire weather conditions based on meteorological data.

## Features

- **Web Interface**: User-friendly dark-themed dashboard for entering fire weather parameters
- **Ridge Regression Model**: Pre-trained machine learning model for accurate FWI predictions
- **Real-time Predictions**: Instant results based on input parameters
- **Data Normalization**: Automatic feature scaling using StandardScaler for consistent predictions
- **Responsive Design**: Modern, developer-friendly dark interface with grid overlay aesthetics
- **Flask Backend**: Lightweight and efficient backend API

## Project Structure

```
ridge_workspace/
├── application.py           # Flask application and prediction logic
├── requirements.txt         # Python package dependencies
├── models/
│   ├── ridge.pkl           # Trained Ridge regression model
│   └── scaler.pkl          # Fitted StandardScaler for feature normalization
├── templates/
│   ├── index.html          # Home page
│   └── predict.html        # Prediction form and results page
└── notebook/               # Jupyter notebooks for model development
```

## Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup

1. Clone or download the project:
```bash
cd ridge_workspace
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Flask application:
```bash
python application.py
```

4. Open your browser and navigate to:
```
http://localhost:5000
```

## Dependencies

- **Flask**: Web framework for building the application
- **NumPy**: Numerical computing library
- **Pandas**: Data manipulation and analysis
- **scikit-learn**: Machine learning algorithms and preprocessing

See `requirements.txt` for specific versions.

## Usage

### Home Page
Visit the home page to access the application interface.

### Making Predictions

1. Navigate to the prediction page
2. Enter the following parameters:
   - **Temperature**: Air temperature (°C)
   - **RH**: Relative Humidity (%)
   - **Ws**: Wind Speed (km/h)
   - **Rain**: Rainfall (mm)
   - **FFMC**: Fine Fuel Moisture Code
   - **DMC**: Duff Moisture Code
   - **ISI**: Initial Spread Index
   - **Classes**: Forest classes category
   - **Region**: Geographic region code

3. Click the **Predict** button to generate the FWI prediction
4. View the prediction result displayed on the page

## Model Details

- **Model Type**: Ridge Regression
- **Features**: 9 meteorological and forest fire indices
- **Input Scaling**: StandardScaler normalization applied to all inputs
- **Output**: Predicted Fire Weather Index (FWI) value

## API Endpoints

### GET `/`
Returns the home page.

### GET/POST `/prediction`
- **GET**: Returns the prediction form
- **POST**: Accepts form data and returns prediction result
  - **Form Parameters**: Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region
  - **Response**: HTML page with prediction result

## Design System

The interface features a modern dark theme inspired by VS Code:
- **Primary Background**: Deep navy (#080b12)
- **Surface Cards**: Gradient backgrounds (#0d1120 to #111827)
- **Accent Colors**: Orange (#f97316), Cyan (#38bdf8), Green (#34d399), Purple (#a78bfa)
- **Typography**: Outfit font for headings, Fira Code for monospace elements
- **Grid Overlay**: Subtle cyan lines for visual structure

## Configuration

To modify the application settings, edit `application.py`:

```python
app.run(host='0.0.0.0', port=5000, debug=True)  # Enable debug mode
```

## Error Handling

- Invalid input validation is performed on all form fields
- Numerical values are required for all parameters
- The application handles prediction errors gracefully

## Future Enhancements

- Model version management
- Batch prediction support
- Historical prediction tracking
- Advanced visualization of prediction confidence
- API documentation with Swagger/OpenAPI

## License

This project is provided as-is for educational and research purposes.

## Contact

For questions or issues, please refer to the project documentation or contact the development team.
