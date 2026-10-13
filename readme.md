# Weather App

A simple command-line weather application built with Python. This project was created as a hands-on exercise in working with HTTP requests, environment variables, and external APIs.

The application asks for a city name, retrieves its current weather data using the [OpenWeatherMap Current Weather API](https://openweathermap.org/current), and displays useful weather information directly in the terminal.

## Features

* **City-based search:** Enter a city name to look up its current weather.
* **Current temperature:** Displays the temperature in degrees Celsius.
* **Feels-like temperature:** Shows the perceived temperature reported by the API.
* **Weather description:** Provides a brief description of the current weather conditions.
* **Environment variables:** Loads the API key from a `.env` file instead of hardcoding it in the source code.

## Built With

* **Python** — application logic
* **Requests** — sends HTTP requests to the weather API
* **python-dotenv** — loads environment variables from a `.env` file
* **OpenWeatherMap API** — provides current weather data

## How It Works

1. The application loads environment variables from the `.env` file.
2. It prompts the user to enter a city name.
3. It constructs an API request containing the city, API key, and metric units.
4. It sends an HTTP request to OpenWeatherMap and parses the JSON response.
5. It displays the city's temperature, feels-like temperature, and weather description.

## Getting Started

### Prerequisites

* Python 3
* An [OpenWeatherMap account and API key](https://home.openweathermap.org/users/sign_up)

### 1. Clone the Repository

```bash
git clone https://github.com/aqilmuh/weather.git
cd weather
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Your API Key

Create a file named `.env` in the project directory and add your OpenWeatherMap API key:

```env
API_KEY=your_openweathermap_api_key
```

Replace `your_openweathermap_api_key` with your actual API key.

**Keep your API key private.** Do not commit your `.env` file or expose your API key in a public repository.

### 4. Run the Application

```bash
python weather.py
```

Enter a city name when prompted. The application will retrieve and display the current weather information returned by the API.

## Example Output

The following is illustrative output. Actual values depend on the city and current weather conditions.

```text
Enter the city name:
London

Showing current weather for London:

The temperature is 15.2°C
Feels like 14.7°C
Description: scattered clouds
```

## Project Structure

```text
weather/
├── weather.py       # Main application
├── requirements.txt # Python dependencies
├── .gitignore       # Files excluded from Git
└── readme.md        # Project documentation
```

## What I Learned

This project provides practical experience with:

* Making HTTP requests using Python's `requests` library
* Retrieving and processing JSON data from an external API
* Managing API keys using environment variables
* Using third-party Python packages
* Building an interactive command-line application

## Future Improvements

Possible improvements include:

* Handling invalid city names and API errors
* Adding network error handling
* Validating user input
* Displaying additional weather information, such as humidity and wind speed

## API Reference

* [OpenWeatherMap Current Weather API](https://openweathermap.org/current)
