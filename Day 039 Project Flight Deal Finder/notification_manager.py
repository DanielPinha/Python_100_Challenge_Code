import smtplib
import os

MY_EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('EMAIL_PASS')
SMTP_SERVER = os.getenv('SMTP_SERVER')


class NotificationManager:

    def __init__(self):
        self.email = MY_EMAIL
        self.password = PASSWORD
        self.smtp = SMTP_SERVER

    def send_email(self, travel_info):
        with smtplib.SMTP(self.smtp) as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            connection.sendmail(
                from_addr=self.email,
                to_addrs=self.email,
                msg=f"Subject:Promotional flight to {travel_info['to_city']}!\n\n"
                    f"From: {travel_info['from_city']}\n"
                    f"To: {travel_info['to_city']}\n"
                    f"Lowest priced flight details:\n"
                    f"  Price: {travel_info['lowest_option']['travel price']}\n"
                    f"  Flight Link: {travel_info['lowest_option']['link']}"
            )
