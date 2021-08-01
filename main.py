from flask import Flask, render_template
import random
import datetime
import requests
app = Flask(__name__)
dt = datetime.datetime.today()


@app.route('/')
def home():
    random_number = random.randint(1,10)
    return render_template('index.html', num=random_number, year=dt.year)

@app.route('/guess/<name>')
def guess(name):
    guess_year = random.randint(1, 80)
    gender_url = f"https://api.genderize.io/?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    return render_template('guess_game.html', name=name, gender=gender ,years=guess_year)

@app.route("/blog/<num>")
def blog(num):
    print(num)
    blog_url = "https://www.npoint.io/docs/5abcca6f4e39b4955965"
    response_blog = requests.get(blog_url)
    all_posts = response_blog.json()
    return render_template("blog.html", posts=all_posts)
if __name__ == "__main__":
    app.run(debug=True)


