from flask import Flask, render_template, request
import requests
import smtplib
import os

MY_EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('EMAIL_PASS')
SMTP_SERVER = os.getenv('SMTP_SERVER')

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


@app.route('/forms-entry', methods=["POST"])
def receive_data():
    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Contact received from Blog!\n\n"
                f"Name: {request.form['username']}\n"
                f"Email: {request.form['email']}\n"
                f"Phone Number: {request.form['phone']}\n"
                f"Message: {request.form['message']}\n"
        )
    return f"<h1>Message sent successfully</h1>"


if __name__ == "__main__":
    blog_post_response = requests.get("https://api.npoint.io/43644ec4f0013682fc0d")
    blog_post_response.raise_for_status()
    blog_post = blog_post_response.json()
    app.run(debug=True)
