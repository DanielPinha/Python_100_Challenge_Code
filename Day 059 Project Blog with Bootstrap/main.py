from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", all_posts=blog_post)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template("post.html", post=blog_post[post_id-1])


if __name__ == "__main__":
    blog_post_response = requests.get("https://api.npoint.io/43644ec4f0013682fc0d")
    blog_post_response.raise_for_status()
    blog_post = blog_post_response.json()
    app.run(debug=True)
