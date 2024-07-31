from flask import Flask, request, render_template_string
from datetime import datetime
from backend import WeatherAppBackend

app = Flask(__name__)

# Initialize WeatherAppBackend with API key
api_key = '5dd09ae78dfe16cade77b62b87b1b292'
weather_backend = WeatherAppBackend(api_key)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_info = None
    if request.method == 'POST':
        city_name = request.form.get('city_name')
        if city_name:
            weather_info = weather_backend.get_weather_details(city_name)
    
    now = datetime.now()
    data = {
        'current_date': now.strftime("%B %d, %Y"),
        'current_time': now.strftime("%H:%M:%S"),
        'greeting': 'The 4 Seasons',
        'weather_info': weather_info
    }
    
    template = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Weather App</title>
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300..800;1,300..800&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
    
            body {
                font-family: 'Poppins', sans-serif;
                background-color: #282c34;
                color: #61dafb;
                margin: 0;
                padding: 0;
                text-align: center;
                background : url("https://cdn-images.imagevenue.com/6b/5a/f3/ME18ULW6_o.jpg");
                background-repeat: no-repeat;
                background-size: cover;
               height: 95vh;
            #    overflow: hidden;
            }
            h1 {
                color: #61dafb;
                margin-bottom: 0;
                animation: shadow-pulse 2s infinite;
                font-family: 'Poppins', sans-serif;
                
            }
            p {
                color: #fff;
                margin: 10px 0;
                font-family: 'Poppins', sans-serif;
            }
            form {
                margin: 20px auto;
                max-width: 400px;
                padding: 20px;
                background-color: #1e1e1e;
                border-radius: 10px;
            }
            input[type="text"] {
                padding: 10px;
                margin: 10px 0;
                border: 2px solid #61dafb;
                border-radius: 5px;
                background-color: #1e1e1e;
                color: #abb2bf;
                width: 100%;
                box-sizing: border-box;
            }
            input[type="submit"] {
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                background-color: #61dafb;
                color: #282c34;
                font-size: 16px;
                cursor: pointer;
                transition: background-color 0.3s ease;
            }
            input[type="submit"]:hover {
                background-color: #4fa3d4;
            }
            h2 {
                color: #ffffff;
                margin: 20px 0;
                font-weight: 700;
                font-family: 'Poppins', sans-serif;
            }
            /* Keyframes for the box-shadow animation */
            @keyframes shadow-pulse {
                0% {
                    text-shadow: 0 0 10px rgba(0, 0, 255, 0.7);
                }
                50% {
                    text-shadow: 0 0 20px rgba(0, 0, 255, 0.5);
                }
                100% {
                    text-shadow: 0 0 10px rgba(0, 0, 255, 0.7);
                }
            }
        </style>
        <script>
            function capitalizeInput() {
                var input = document.querySelector('input[name="city_name"]');
                input.value = input.value.split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
            }
            function validateForm(event) {
                var input = document.querySelector('input[name="city_name"]');
                if (input.value.trim() === '') {
                    alert('City name cannot be empty.');
                    event.preventDefault(); // Prevent form submission
                }
            }
            document.addEventListener('DOMContentLoaded', function() {
                var form = document.querySelector('form');
                form.addEventListener('submit', function(event) {
                    validateForm(event);  // Validate first
                    capitalizeInput();    // Then capitalize
                });
            });
        </script>
    </head>
    <body>
        <h1>{{ greeting }}</h1>
        <p>Date: {{ current_date }}</p>
        <form method="post">
            <input type="text" name="city_name" placeholder="Enter city name..." required autocomplete="off">
            <input type="submit" value="Get Weather">
        </form>
        {% if weather_info %}
            <h2>Weather in {{ weather_info.city }}</h2>
            <p>Humidity: {{ weather_info.humidity }}%</p>
            <p>Min Temperature: {{ weather_info.min_temp }}°C</p>
            <p>Max Temperature: {{ weather_info.max_temp }}°C</p>
            <p>Conditions: {{ weather_info.conditions }}</p>
            <p>Season: {{ weather_info.season }}</p>
        {% endif %}
    </body>
    </html>
    '''
    
    return render_template_string(template, **data)

if __name__ == '__main__':
    app.run(debug=True)
