import requests

# We’ll check the weather for London as a test
url = "https://api.open-meteo.com/v1/forecast?latitude=51.5072&longitude=0.1276&current_weather=true"

response = requests.get(url)   # send request
data = response.json()         # convert response to Python dictionary

# Print full API response
print("Full API response:", data)

# Extract just the current temperature
temperature = data["current_weather"]["temperature"]
print(f"The current temperature in London is {temperature}°C")
