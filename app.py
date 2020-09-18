import requests

from flask import Flask, render_template,request,url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        district_id = request.form.get('district')        
        url = f"https://data.nepalcorona.info/api/v1/districts/{district_id}"
        r = requests.get(url).json()
        num_of_cases =len(r['covid_cases'])

        get_dist = requests.get('https://data.nepalcorona.info/api/v1/districts').json()
        return render_template('index.html',district_list=get_dist, dis=r, num=num_of_cases)
    # le = len(r.covid_cases)
    get_dist = requests.get('https://data.nepalcorona.info/api/v1/districts').json()
    return render_template('index.html',district_list=get_dist)

@app.route('/news')
def news():
    url = "https://nepalcorona.info/api/v1/news"
    news = requests.get(url).json()
    return render_template('news.html',news=news)


if __name__ == "__main__":
    app.run()