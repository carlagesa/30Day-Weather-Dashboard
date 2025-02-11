import streamlit as st
import requests
import plotly.express as px
import pandas as pd

# Title of the app
st.title("🌤️ Weather Dashboard")

# Input for city name
city = st.text_input("Enter a city name", "London")

# API Gateway endpoint
api_url = "https://cqs409ssac.execute-api.us-east-1.amazonaws.com/weather"

# Fetch weather data
if st.button("Get Weather"):
    if city:
        try:
            # Call the API Gateway endpoint
            response = requests.get(f"{api_url}?city={city}")
            if response.status_code == 200:
                weather_data = response.json()

                # Display city name and country
                st.subheader(f"Weather in {weather_data['name']}, {weather_data['sys']['country']}")

                # Create columns for layout
                col1, col2, col3 = st.columns(3)

                # Display metrics
                with col1:
                    st.metric("Temperature", f"{weather_data['main']['temp']} °C")
                with col2:
                    st.metric("Humidity", f"{weather_data['main']['humidity']} %")
                with col3:
                    st.metric("Wind Speed", f"{weather_data['wind']['speed']} m/s")

                # Display weather icon
                icon_url = f"http://openweathermap.org/img/wn/{weather_data['weather'][0]['icon']}.png"
                st.image(icon_url, caption=weather_data['weather'][0]['description'], width=100)

                # Create a DataFrame for historical data (mock data for demonstration)
                historical_data = {
                    "Date": pd.date_range(start="2023-10-01", periods=7, freq="D"),
                    "Temperature (°C)": [15, 16, 14, 17, 18, 16, 15],
                    "Humidity (%)": [70, 72, 68, 75, 74, 73, 71],
                }
                df = pd.DataFrame(historical_data)

                # Display historical temperature trend
                st.subheader("Temperature Trend (Last 7 Days)")
                fig_temp = px.line(df, x="Date", y="Temperature (°C)", title="Temperature Over Time")
                st.plotly_chart(fig_temp)

                # Display historical humidity trend
                st.subheader("Humidity Trend (Last 7 Days)")
                fig_humidity = px.line(df, x="Date", y="Humidity (%)", title="Humidity Over Time")
                st.plotly_chart(fig_humidity)

            else:
                st.error(f"Error: {response.json().get('error', 'Unknown error')}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a city name.")
        