# Weather Forecast Dashboard

![Weather Dashboard Screenshot](link-to-screenshot.png)

## Overview

The Weather Forecast Dashboard is a simple yet powerful application that provides users with a 5-day weather forecast for any city in the world. The application uses the OpenWeatherMap API to fetch weather data and displays it in an interactive, user-friendly dashboard built with Streamlit.

## Features

- **Real-Time Weather Data:** Fetches and displays current weather information and a 5-day forecast.
- **Interactive UI:** Simple and intuitive interface where users can enter the name of any city.
- **Weather Details:** Provides temperature, humidity, wind speed, and weather descriptions for each day.
- **Responsive Design:** Works seamlessly on desktop and mobile devices.

## How It Works

1. **User Input:** Enter the name of a city in the text box provided.
2. **Data Fetching:** The app uses the OpenWeatherMap API to retrieve weather data for the specified city.
3. **Data Display:** The retrieved data is processed and displayed in a tabular format, showing the 5-day forecast with details.

## Installation

### Prerequisites

- Python 3.x
- Streamlit
- Requests
- Pandas

### Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/weather-forecast-dashboard.git
    cd weather-forecast-dashboard
    ```

2. Install the required packages:
    ```bash
    pip install streamlit requests pandas
    ```

3. Get your API key from [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) and add it to the code.

4. Run the application:
    ```bash
    streamlit run weather_dashboard.py
    ```

## Usage

1. Launch the app by running the above command.
2. Enter the name of any city in the text input box.
3. View the 5-day weather forecast, including temperature, humidity, wind speed, and weather descriptions.

## Example

![Example Output](link-to-another-screenshot.png)

## Potential Enhancements

- Add options for selecting between Celsius and Fahrenheit.
- Implement map integration to show the city's location.
- Save and quickly access favorite cities.
- Deploy the app on Streamlit Cloud for easy sharing.

## Contributing

Feel free to fork this repository, submit issues, and make pull requests. Contributions are highly appreciated!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [OpenWeatherMap](https://openweathermap.org/) for the weather data API.
- [Streamlit](https://streamlit.io/) for the amazing framework to build interactive apps.
