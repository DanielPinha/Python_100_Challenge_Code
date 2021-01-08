from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", all_posts=blog_post)


@app.route('/post/<id>')
def post(id):
    return render_template("post.html", post=blog_post[int(id)-1])


if __name__ == "__main__":
    blog_post_response = requests.get("https://api.npoint.io/5abcca6f4e39b4955965")
    blog_post_response.raise_for_status()
    blog_post = blog_post_response.json()
    app.run(debug=True)
