import requests
import tkinter as tk
from tkinter import messagebox
from urllib.parse import quote

API_KEY = 'your_openweathermap_api_key' 
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

def get_weather_data(city):
    city_encoded = quote(city)
    request_url = f"{BASE_URL}appid={API_KEY}&q={city_encoded}&units=metric"
    print(f"Request URL: {request_url}")  
    try:
        response = requests.get(request_url)
        print(f"Response Status Code: {response.status_code}")
        response.raise_for_status()  
        data = response.json()
        print(f"Response JSON: {data}")  
        if data.get('cod') != 200:
            return None, data.get('message', 'Error fetching weather data')
        return {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }, None
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}") 
        return None, f"HTTP error occurred: {http_err}"
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")  
        return None, f"Request error occurred: {req_err}"

def show_weather():
    city = city_entry.get()
    weather, error = get_weather_data(city)
    if weather:
        result = f"City: {weather['city']}\n"
        result += f"Temperature: {weather['temperature']}°C\n"
        result += f"Description: {weather['description']}\n"
        result += f"Humidity: {weather['humidity']}%\n"
        result += f"Wind Speed: {weather['wind_speed']} m/s"
        weather_info.config(text=result)
    else:
        messagebox.showerror("Error", error or "City not found!")


root = tk.Tk()
root.title("Weather App")


city_label = tk.Label(root, text="Enter city name:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

search_button = tk.Button(root, text="Search", command=show_weather)
search_button.pack()

weather_info = tk.Label(root, text="", justify='left')
weather_info.pack()


root.mainloop()
