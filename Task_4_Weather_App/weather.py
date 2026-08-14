# Weather App - Task 4 Beginner Tier
import requests

# Your API key
API_KEY = "b7de0051f363ee984d628686a40dd511"

# Ask user for city
city = input("Enter city name: ")

# Build the URL
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# Get weather data
response = requests.get(url)

# Check if city was found
if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind = data['wind']['speed']
    
    print("\n" + "=" * 40)
    print(f"Weather in {city}:")
    print(f"Temperature: {temp}°C")
    print(f"Description: {desc}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind} m/s")
    print("=" * 40)
else:
    print("City not found. Please check the name and try again.")