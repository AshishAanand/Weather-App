# Weather App (Mausam Ka Haal)🌦️
A simple and intuitive Weather App built with Python and Tkinter that fetches live weather data using the OpenWeather API.

## Features ✨
- Retrieve real-time weather data for any city.
- Displays:
    - Current temperature.
    - Humidity levels.
    - Weather conditions (e.g., clear sky, rain, etc.).
- Easy-to-use graphical user interface (GUI).
## Prerequisites 📋
To run this project, ensure you have the following:

1. Python installed on your system.

2. The following Python libraries installed:
- ***tkinter*** (comes pre-installed with Python in most cases).

- ***requests*** (for fetching data from the OpenWeather API).
```bash
pip install requests
```
- ***json*** (comes pre-installed with Python).
# Getting Started 🚀
### 1. Clone the Repository
```bash
git clone https://github.com/your-username/weather-app.git
cd weather-app
```

### 2. Get Your OpenWeather API Key
Go to the [OpenWeatherMap](https://openweathermap.org/) website.
Sign up or log in to your account.
Navigate to the API section and generate your free API key.

### 3. Add Your API Key
- Open the ***weather_app.py file*** in a text editor.
- Locate the line where the API key is defined:


``` python
API_KEY = "enter_your_api_key_here"
```

- Replace ***"enter_your_api_key_here"*** with your own API key:

```python
API_KEY = "your_actual_api_key"
```

### 4. Run the Application
Execute the Python script to launch the Weather App:

```python
python weather_app.py
```
## Example Output 📊
Input: City Name: London
Output:
City: London
Temperature: 15°C
Humidity: 75%
Weather: Clear Sky
## Notes 📝
Ensure your system is connected to the internet while using the app.
Your API key is private. Avoid sharing it publicly or committing it to public repositories.

# Contributing 🤝
Contributions are welcome! Feel free to fork this repository and submit pull requests for any improvements or new features.
