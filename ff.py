import streamlit as st
import requests
import pandas as pd

# Function to get weather data
def get_weather(city_name, api_key):
    base_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    data = response.json()
    return data

# Function to parse the data into a DataFrame
def parse_data(data):
    forecast_list = data['list']
    weather_data = {
        "Date": [entry['dt_txt'] for entry in forecast_list],
        "Temperature (°C)": [entry['main']['temp'] for entry in forecast_list],
        "Humidity (%)": [entry['main']['humidity'] for entry in forecast_list],
        "Wind Speed (m/s)": [entry['wind']['speed'] for entry in forecast_list],
        "Description": [entry['weather'][0]['description'] for entry in forecast_list]
    }
    return pd.DataFrame(weather_data)

# Streamlit app
def main():
    st.title("Weather Forecast Dashboard")
    
    api_key = "YOUR_API_KEY_HERE"  # Replace with your OpenWeatherMap API key
    
    city_name = st.text_input("Enter a city name:", "New York")
    
    if city_name:
        weather_data = get_weather(city_name, api_key)
        if weather_data['cod'] == '200':
            df = parse_data(weather_data)
            st.subheader(f"5-Day Weather Forecast for {city_name}")
            st.dataframe(df)
        else:
            st.error(f"City {city_name} not found!")

if __name__ == "__main__":
    main()
