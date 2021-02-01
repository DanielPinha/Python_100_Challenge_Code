from flask import Flask, render_template, request
import smtplib
import os

MY_EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('EMAIL_PASS')
SMTP_SERVER = os.getenv('SMTP_SERVER')

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/forms-entry', methods=["POST"])
def receive_data():
    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Contact received from Portfolio!\n\n"
                f"Name: {request.form['username']}\n"
                f"Email: {request.form['email']}\n"
                f"Phone Number: {request.form['phone']}\n"
                f"Message: {request.form['message']}\n"
        )
    return f"<h1>Email sent successfully</h1>"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)
