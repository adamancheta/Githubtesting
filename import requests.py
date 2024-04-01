import requests
from bs4 import BeautifulSoup



def construct_links(URL):
    try:
        response = requests.get(URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        links_with_labels = [(link['href'], link.get_text()) for link in links]
        
        return links_with_labels
    except Exception as e:
        print("Error:", e)
        return []


def count_missing_alt(URL):
    try:
        # Send a GET request to the URL
        response = requests.get(URL)
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all image tags <img> without alt attribute
        images = soup.find_all('img', alt=False)
        
        # Count the number of images without alt attribute
        num_images = len(images)
        
        # Find total number of image tags
        total_images = len(soup.find_all('img'))
        
        # Calculate the percentage
        if total_images == 0:
            return 0.0
        else:
            percent_missing_alt = num_images / total_images
            return percent_missing_alt
    except Exception as e:
        print("Error:", e)
        return 0.0
import requests

def get_weather_json(lat, lon, api_key):
    try:
        # Construct the API URL with the provided latitude, longitude, and API key
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=imperial"
        
        # Send a GET request to the API
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            weather_data = response.json()
            return weather_data
        else:
            print("Failed to retrieve weather data. Status code:", response.status_code)
            return None
    except Exception as e:
        print("Error:", e)
        return None

# Example usage:
latitude = 40.7128  # Example latitude (New York City)
longitude = -74.0060  # Example longitude (New York City)
api_key = "YOUR_API_KEY_HERE"  # Replace "YOUR_API_KEY_HERE" with your actual API key

weather_data = get_weather_json(latitude, longitude, api_key)
if weather_data:
    print("Current weather data:")
    print(weather_data)