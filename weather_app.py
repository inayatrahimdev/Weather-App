import streamlit as st
import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        icon = data['weather'][0]['icon']
        return {
            'weather': weather,
            'temperature': temp,
            'humidity': humidity,
            'wind_speed': wind_speed,
            'icon': icon
        }
    else:
        return None

def display_weather_info(weather_info, city):
    st.write(f"## Weather in {city}")
    st.image(f"http://openweathermap.org/img/wn/{weather_info['icon']}@2x.png")
    st.write(f"**Description:** {weather_info['weather']}")
    st.write(f"**Temperature:** {weather_info['temperature']}°C")
    st.write(f"**Humidity:** {weather_info['humidity']}%")
    st.write(f"**Wind Speed:** {weather_info['wind_speed']} m/s")

    # Example of an alert based on weather conditions
    if weather_info['temperature'] > 35:
        st.warning("🌞 It's very hot! Stay hydrated and avoid prolonged exposure to the sun.")
    elif weather_info['temperature'] < 0:
        st.warning("❄️ It's freezing! Make sure to dress warmly.")
    if 'rain' in weather_info['weather'].lower():
        st.info("☔ It's raining. Don't forget to take an umbrella!")
    if 'snow' in weather_info['weather'].lower():
        st.info("❄️ Snowfall expected. Drive safely!")

def main():
    st.title("🌤️ Weather Information App")
    st.write("Enter the name of any city to get the current weather information and alerts.")

    api_key = "7c8e37d0082cf3035641624f0d67c783"
    city = st.text_input("City name:")
    
    if st.button("Get Weather"):
        if city:
            weather_info = get_weather(api_key, city)
            if weather_info:
                display_weather_info(weather_info, city)
            else:
                st.error("City not found or an error occurred. Please check the city name and try again.")
        else:
            st.warning("Please enter a city name.")

if __name__ == "__main__":
    main()
