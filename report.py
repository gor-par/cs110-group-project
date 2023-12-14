import os
import webbrowser
from jinja2 import Environment, FileSystemLoader

# Define the path to the folder where the pictures are located
PICTURE_FOLDER = "pictures"

# Define the list of pictures and their descriptions
pictures = [
    {"name": "visuals/world_map.png", "description": "Detailed world map illustration"},
    {"name": "visuals/histogram.png", "description": "Histogram chart displaying data distribution"},
    {"name": "visuals/boxplots.png", "description": "Boxplots visualizing statistical data"},
]

# Define the html template using Jinja2
template = """
<!DOCTYPE html>
<html>
<head>
    <style>
        /* Set the background color to black */
        body {
            background-color: black;
            font-family: 'Courier New', monospace;
            color: #00FF00; /* Neon green */
        }

        /* Set the title color to neon green and center it */
        h1 {
            text-align: center;
        }

        /* Set the image size to 50% of the window width and center it */
        img {
            width: 50%;
            display: block;
            margin-left: auto;
            margin-right: auto;
        }

        /* Set the image description color to white and center it */
        p {
            color: white;
            text-align: center;
        }
        
        
        pre {
            background-color: black;
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
    </style>
</head>
<body>
    <!-- Display the title -->
    <h1>WEATHER DATA REPORT</h1>
    <!-- Display some code blocks with python code -->
    <center><pre>
    --------------------------------------------------------------------------------------------------------------------------
    |GlobalWeatherRepository.csv: 15979 Rows, 41 Columns                                                                     |
    --------------------------------------------------------------------------------------------------------------------------
    |Country   |Locatio...|Latitude  |Longitude |Timezone  |...       |Sunset    |Moonrise  |Moonset   |Moon_phase|Moon_il...|
    --------------------------------------------------------------------------------------------------------------------------
    |Afghani...|Kabul     |34.52     |69.18     |Asia/Kabul|...       |06:24 PM  |05:39 PM  |02:48 AM  |Waxing ...|93.0      |
    --------------------------------------------------------------------------------------------------------------------------
    |Albania   |Tirana    |41.33     |19.82     |Europe/...|...       |07:19 PM  |06:50 PM  |03:25 AM  |Waxing ...|93.0      |
    --------------------------------------------------------------------------------------------------------------------------
    |Algeria   |Algiers   |36.76     |3.05      |Africa/...|...       |07:21 PM  |06:46 PM  |03:50 AM  |Waxing ...|93.0      |
    --------------------------------------------------------------------------------------------------------------------------
    |Andorra   |Andorra...|42.5      |1.52      |Europe/...|...       |08:34 PM  |08:08 PM  |04:38 AM  |Waxing ...|93.0      |
    --------------------------------------------------------------------------------------------------------------------------
    |Angola    |Luanda    |-8.84     |13.23     |Africa/...|...       |06:06 PM  |04:43 PM  |04:41 AM  |Waxing ...|93.0      |
    --------------------------------------------------------------------------------------------------------------------------
    |...       |...       |...       |...       |...       |...       |...       |...       |...       |...       |...       |
    --------------------------------------------------------------------------------------------------------------------------
    |Venezuela |Caracas   |10.5      |-66.92    |America...|...       |06:02 PM  |01:47 PM  |01:05 AM  |Waxing ...|56.0      |
    --------------------------------------------------------------------------------------------------------------------------
    |Vietnam   |Hanoi     |21.03     |105.85    |Asia/Ba...|...       |05:14 PM  |01:04 PM  |No moonset|Waxing ...|56.0      |
    --------------------------------------------------------------------------------------------------------------------------
    |Yemen     |Sanaa     |15.35     |44.21     |Asia/Aden |...       |05:30 PM  |01:12 PM  |12:18 AM  |Waxing ...|56.0      |
    --------------------------------------------------------------------------------------------------------------------------
    |Zambia    |Lusaka    |-15.42    |28.28     |Africa/...|...       |06:19 PM  |12:54 PM  |12:56 AM  |Waxing ...|56.0      |
    --------------------------------------------------------------------------------------------------------------------------
    |Zimbabwe  |Harare    |-17.82    |31.04     |Africa/...|...       |06:12 PM  |12:41 PM  |12:47 AM  |Waxing ...|56.0      |
    --------------------------------------------------------------------------------------------------------------------------
    </pre></center>

    
    <!-- Loop through the pictures and display them with their descriptions -->
    {% for picture in pictures %}
    <!-- Add an id attribute to the first image tag -->
    <img {% if loop.first %}id="bg"{% endif %} src="{{ picture.name }}" alt="{{ picture.description }}">
    <!-- Optionally, remove the description of the first picture from the loop -->
    {% if not loop.first %}<p>{{ picture.description }}</p>{% endif %}
    {% endfor %}
    <center> <pre>
    print("Thank you for your attention, we are almost over")
    </pre></center>
    
</body>
</html>
"""

# Create environment and load the template
env = Environment(loader=FileSystemLoader(PICTURE_FOLDER))
template = env.from_string(template)

# Render the template with the pictures data
html = template.render(pictures=pictures)

# Save the html to a file
with open("weather_data_report.html", "w") as f:
    f.write(html)

# Open the html file in the web browser
webbrowser.open("weather_data_report.html")
