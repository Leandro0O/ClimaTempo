from flask import Flask, render_template, request
from API import Tempo

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")


@app.route("/form", methods=["GET", "POST"])
def form():
    cidade = request.form['cidade']
    url = Tempo.base_url(cidade)
    urlJ = Tempo.url_json(url)
    desc = urlJ["weather"][0]['description']
    temp = int(float(urlJ["main"]["temp"]) - 273.15)
    tmin = int(float(urlJ["main"]["temp_min"]) - 273.15)
    tmax = int(float(urlJ["main"]["temp_max"]) - 273.15)
    sens = int(float(urlJ["main"]["feels_like"]) - 273.15)
    umi = int(urlJ["main"]["feels_like"])
    
    return render_template("index.html",
                           cidade=request.form["cidade"].title(),
                           desc=desc,
                           temp=temp,
                           tmin=tmin,
                           tmax=tmax,
                           sens=sens,
                           umi=umi,
                           hora = Tempo.hora())
                           


if __name__ == "__main__":
    app.run(debug=True)
