# #################### Extra Hard Starting Project ##################### #
import smtplib
import datetime as dt
import random
import pandas
# ---------- CREATE CONSTANT ---------- #
MY_EMAIL = 'danielpinhapog@gmail.com'
PASSWORD = 'pogtrial123'
SMTP_SERVE = 'smtp.gmail.com'

# ---------- Get birthday date information ---------- #


def get_birthday_date(birthday_info):
    """Receive pandas Series and return datetime class with date information only"""
    birthday_year = birthday_info[1]['year']
    birthday_month = birthday_info[1]['month']
    birthday_day = birthday_info[1]['day']
    return dt.datetime(birthday_year, birthday_month, birthday_day).date()


# ---------- Send email for birthday person ---------- #


def send_email(birthday_info, letter_choice):
    birthday_name = birthday_info[1]['name']
    birthday_email = birthday_info[1]['email']
    email_body = letter_choice.replace('[NAME]', birthday_name)

    with smtplib.SMTP(SMTP_SERVE) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_email,
            msg=f"Subject:Happy Birthday {birthday_name}!\n\n{email_body}"
        )


# ---------- Open Birthday File ---------- #
birthday_list = pandas.read_csv('birthdays.csv')


# ---------- Open letter templates and add in letter list ---------- #
with open('./letter_templates/letter_1.txt') as file1:
    letter1 = file1.read()

with open('./letter_templates/letter_2.txt') as file2:
    letter2 = file2.read()

with open('./letter_templates/letter_3.txt') as file3:
    letter3 = file3.read()

letter_list = (letter1, letter2, letter3)

# ---------- Get current date information ---------- #
current_date = dt.datetime.now()
current_month_day = (current_date.month, current_date.day)

# ---------- Check if any birthday date is matching with current date ---------- #
for birthday in birthday_list.iterrows():
    birthday_date = get_birthday_date(birthday)
    birthday_month_day = (birthday_date.month, birthday_date.day)
    # If date is a match, get random letter template and call send email function
    if birthday_month_day == current_month_day:
        letter = random.choice(letter_list)
        send_email(birthday, letter)
