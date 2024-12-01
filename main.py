from tkinter import *
import json
import requests

# Storing data in JSON format in data.json file
file_path = 'data.json'

API_KEY = 'enter your API key'
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def on_btn_click():
    global API_KEY, BASE_URL

    get_city_name = city_name_input.get()

    url = f"{BASE_URL}?q={get_city_name}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    with open(file_path, 'w') as file:
        json.dump(data, file)

    if response.status_code == 200:
        print("Data successfully stored in data.json file")
        city_name.config(text=f"City: {get_city_name}")
        city_temperature.config(text=f"Temperature: {data['main']['temp']} °C")
        city_humidity.config(text=f"Humidity: {data['main']['humidity']}%")
        city_weather.config(text=f"Weather: {data['weather'][0]['description']}")
    else:
        print("Error:", data.get("message", "Unable to fetch data"))

# Initializing Tkinter
root = Tk()
# Defining window size
root.geometry("700x600")
root.minsize(300, 200)

# Input for City name
city_name_input = Entry(root, width=60, font=("Arial", 15))
city_name_input.pack(pady=30)

# Button to check weather
button = Button(root, text="Check Weather", width=30, font=("Arial", 15), command=on_btn_click)
button.pack(pady=15)

# Show City name
city_name = Label(root, text="", font=("Arial", 15))
city_name.pack(pady=15)
# Show Temperature
city_temperature = Label(root, text="", font=("Arial", 15))
city_temperature.pack(pady=10)
# Show Humidity
city_humidity = Label(root, text="", font=("Arial", 15))
city_humidity.pack(pady=10)
# Show Weather
city_weather = Label(root, text="", font=("Arial", 15))
city_weather.pack(pady=10)

root.mainloop()