from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form.get('city')
        data = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID=API_KEY')
        json_data = json.loads(data.text)
        print(json_data)
        print(data.status_code)
        if data.status_code == 404:
            return render_template('index.html', show = True, wrong = True)
        if data.status_code == 200:
            return render_template('index.html', show = True, name = json_data['name'], country = json_data['sys']['country'],temp=json_data['main']['temp'], min=json_data['main']['temp_min'], max=json_data['main']['temp_max'], feels_like=json_data['main']['feels_like'], desc=json_data['weather'][0]['description'], weather_img = "http://openweathermap.org/img/w/" + json_data['weather'][0]['icon'] + ".png")


    return render_template('index.html')


app.run(debug=True)
