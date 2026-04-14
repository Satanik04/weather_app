from flask import Flask,redirect,render_template,url_for,request
import requests

app=Flask(__name__)
Api_key="ad2ccaf222faaec0e27220dfd6555492"

@app.route("/",methods=["GET","POST"])
def home():
    weather=None
    if request.method=="POST":
        city=request.form["city"]
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={Api_key}&units=metric"
        responce=requests.get(url)
        data=responce.json()
        if data["cod"]==200:
            weather={
                "city":city,
                "temp":data["main"]["temp"],
                "humidity":data["main"]["humidity"],
                "Desc":data["weather"][0]["description"],
                "main":data["weather"][0]["main"],
            }
        else:
            weather="city not found"

    return render_template("index.html",weather=weather)

if __name__=="__main__":
    app.run(debug=True)