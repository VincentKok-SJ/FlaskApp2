from flask import Flask, request, render_template, jsonify, redirect
import json
import requests

app = Flask(__name__)

@app.route('/firstrequest', methods=['GET'])
def firstRequest():
    return(render_template('index.html'))

@app.route('/secondrequest', methods=['GET'])
def secondRequest():
    userAgent = str(request.headers['User-Agent'])
    return(render_template('start.html', userAgent = userAgent))

@app.route('/fourthrequest', methods=['GET'])
def fourthRequest():
    API_KEY = 'dc20d3160e7d504175d202850b79b74b'
    city = request.args.get('q')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)
    #data = response.content
    #temperature = response.content('main')
    temperature = response.json()
    weather = temperature["weather"][0]['description']
    return 'Weathher: ' + weather

@app.route('/thirdrequest', methods=['GET', 'POST'])
def thirdRequest():
    return redirect("http://www.github.com/VincentK16", code=302)
    
@app.route('/form-example', methods=['GET', 'POST']) #allow both GET and POST requests
def form_example():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        language = request.form.get('language')
        framework = request.form.get('framework')
        return '''<h1>The language value is: {}</h1>
                  <h1>The framework value is: {}</h1>'''.format(language, framework) 
    
    return '''<form method="POST">
                  Language: <input type="text" name="language"><br>
                  Framework: <input type="text" name="framework"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''

if __name__ == '__main__':
    app.run(debug=True)
