import requests

# Replace with your OpenWeatherMap API key
api_key = "YOUR_API_KEY"  # Get your key from https://openweathermap.org/

def get_weather(city):
  """
  Retrieves weather data for a given city using OpenWeatherMap API.

  Args:
      city: The name of the city to get weather information for.

  Returns:
      A dictionary containing weather data or None if an error occurs.
  """
  base_url = "http://api.openweathermap.org/data/2.5/weather"
  params = {
    "q": city,
    "appid": api_key,
    "units": "metric"  # Change to "imperial" for Fahrenheit
  }

  try:
    response = requests.get(base_url, params=params)
    response.raise_for_status()  # Raise an exception for non-200 status codes

    # Parse JSON response
    data = response.json()
    return data
  except requests.exceptions.RequestException as e:
    print(f"Error retrieving weather data: {e}")
    return None

def main():
  """
  Prompts the user for a city and displays the current weather.
  """
  while True:
    city = input("Enter a city name (or 'q' to quit): ")
    if city.lower() == 'q':
      break

    weather_data = get_weather(city)

    if weather_data:
      # Extract and display relevant weather information
      city_name = weather_data["name"]
      temperature = weather_data["main"]["temp"]
      description = weather_data["weather"][0]["description"]
      print(f"\nWeather in {city_name}:")
      print(f"  Temperature: {temperature:.2f} °C")
      print(f"  Description: {description}")
    else:
      print("Error retrieving weather data for", city)

if __name__ == "__main__":
  main()
