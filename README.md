# Weather-App-Django
This app titled 'Weather Checker' is used to check weather of every city around the world. Backend is supported by Django Framework and Front End using HTML/CSS. I use OpenWeatherMap to consume the API for this application.

<h2>Result</h2>

https://user-images.githubusercontent.com/67228966/219857473-daf47178-e584-4076-b6c5-30dc90e67873.mp4



<h3>Implementation</h3>

Get an API key: To use the OpenWeatherMap API, you need to get an API key. You can sign up for a free account on the OpenWeatherMap website to get your API key.

Set up a Django project: Start by creating a new Django project and a new Django app within the project using the command python manage.py startapp <appname>. Make sure to add the app to the installed apps in the project settings.

Create a view function: In your app's views.py file, create a function that will handle the request for weather data. The function should use the requests library to make a GET request to the OpenWeatherMap API using the API key and the city name provided by the user.

Parse the JSON data: The weather data returned by the OpenWeatherMap API is in JSON format. You can use the json module in Python to parse the JSON response and extract the weather details you need.

Create a template: Create a template in your app's templates directory that will display the weather details. You can use HTML and CSS to create a user-friendly interface.

Add a URL pattern: In the urls.py file in your app, add a URL pattern that will map the user's request to the view function you created in step 3.

Test the app: Start the Django development server using the command python manage.py runserver and test the app by entering a city name in the browser and submitting the form. The app should display the weather details for the city entered by the user.
