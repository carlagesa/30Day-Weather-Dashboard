# 30-Day Weather Dashboard

This project collects weather data using the **OpenWeatherMap API**, stores it in an **AWS S3 bucket**, and visualizes it using **Amazon QuickSight**. The dashboard provides a 30-day historical and forecasted weather analysis for a specified location.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Project Structure](#project-structure)
3. [Prerequisites](#prerequisites)
4. [Setup Instructions](#setup-instructions)
   - [OpenWeatherMap API](#openweathermap-api)
   - [AWS S3 Bucket](#aws-s3-bucket)
   - [Amazon QuickSight](#amazon-quicksight)
5. [Deployment](#deployment)
6. [Usage](#usage)
7. [Future Features](#future-features)
8. [Contributing](#contributing)
9. [License](#license)

---

## Project Overview
This project automates the collection of weather data using Python, stores it in an AWS S3 bucket, and visualizes it through Amazon QuickSight. The workflow is as follows:
1. Fetch weather data from the OpenWeatherMap API.
2. Upload the data to an S3 bucket.
3. Visualize the data using Amazon QuickSight.

---

## Project Structure
    The repository is organized as follows:
    30Day-Weather-Dashboard/
    ├── src/ # Python scripts for data collection and upload
    │ ├── weather_dashboard.py # Fetches weather data from OpenWeatherMap API & Uploads data to AWS S3 bucket
    │ ├── __init__.py 
    ├── data/ # Sample data files (optional)
    ├── docs/ # Documentation and guides
    ├── tests/ # Documentation and guides
    ├── README.md # Project README
    ├── requirements.txt # Python dependencies

    ---

## Prerequisites
Before setting up the project, ensure you have the following:
1. **Python 3.x** installed.
2. An **OpenWeatherMap API key**.
3. An **AWS account** with access to S3 and QuickSight.
4. **AWS CLI** configured with the necessary permissions.
5. Python libraries listed in `requirements.txt`.

---

## Setup Instructions

### OpenWeatherMap API
1. Sign up for an API key at [OpenWeatherMap](https://openweathermap.org/api).
2. Set the API key as an environment variable:
   ```bash
   export OPENWEATHER_API_KEY="your_api_key_here"
The fetch_weather.py script uses the following endpoints:

Current Weather: https://api.openweathermap.org/data/2.5/weather

5-Day Forecast: https://api.openweathermap.org/data/2.5/forecast

### AWS S3 Bucket
    Create an S3 bucket:

    Name: weather-dashboard-bucket (or any unique name).

    Region: Choose a region close to your location.

    Permissions: Ensure the bucket is private and accessible only to authorized users.

    Set up a folder structure in the bucket:

    Copy
    s3://weather-dashboard-bucket/
    ├── raw-data/              # Raw JSON data from the API
    ├── processed-data/        # Processed data for visualization
    Update the upload_to_s3.py script with your bucket name and folder paths.

### Amazon QuickSight
    Create a new dataset in QuickSight:

    Connect to the S3 bucket (weather-dashboard-bucket).

    Use the processed-data/ folder as the data source.

    Create visualizations:

    Use line charts for temperature trends.

    Use bar charts for precipitation data.

    Use maps for location-based weather analysis.

    Publish the dashboard for sharing.

### Deployment
    The project can be deployed using AWS Lambda and EventBridge for automation.

    Steps to Deploy:
    Package the Python Scripts:

    Create a deployment package with the Python scripts and dependencies.

    Example:

    bash
    Copy
    pip install -r requirements.txt -t ./package
    cp fetch_weather.py upload_to_s3.py ./package
    cd package
    zip -r ../weather-dashboard.zip .
    Create an AWS Lambda Function:

    Upload the weather-dashboard.zip file as the deployment package.

    Set the runtime to Python 3.x.

    Add environment variables:

    OPENWEATHER_API_KEY: Your OpenWeatherMap API key.

    S3_BUCKET_NAME: Your S3 bucket name.

    Set Up EventBridge Trigger:

    Create an EventBridge rule to trigger the Lambda function daily.

    Example cron expression for daily execution:

    Copy
    cron(0 12 * * ? *)  # Runs at 12:00 PM UTC every day
    Test the Deployment:

    Manually trigger the Lambda function to ensure it fetches data and uploads it to S3.

    Verify the data in QuickSight.

### Usage
    Here’s how you can use the 30-Day Weather Dashboard:

    For Developers
    Clone the repository:

    bash
    Copy
    git clone https://github.com/carlagesa/30Day-Weather-Dashboard.git
    Install dependencies:

    bash
    Copy
    pip install -r requirements.txt
    Run the scripts locally:

    bash
    Copy
    python scripts/fetch_weather.py
    python scripts/upload_to_s3.py
    For End Users
    Access the Amazon QuickSight dashboard to view weather visualizations.

### Explore the following features:

    Temperature Trends: View daily temperature changes over 30 days.

    Precipitation Analysis: Analyze rainfall and snowfall patterns.

    Location-Based Insights: Visualize weather data on an interactive map.

### Future Features
    Here are some ideas for future enhancements:

    Multi-Location Support: Extend the dashboard to support multiple cities or regions.

    Advanced Analytics: Add machine learning models to predict weather trends.

    Alert System: Notify users of extreme weather conditions via email or SMS.

    Mobile App: Develop a mobile-friendly version of the dashboard.

    Historical Data Comparison: Compare current weather data with historical averages.

### Contributing
    Contributions are welcome! Please follow these steps:

    Fork the repository.

    Create a new branch for your feature or bugfix.

    Submit a pull request with a detailed description of your changes.

### License
    This project is licensed under the MIT License. See the LICENSE file for details.

    Let me know if you need further adjustments or additional details!

    This README is now ready to be added to your repository. Let me know if you need any further tweaks! 🚀