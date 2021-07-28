import random
import smtplib
import pandas as pd
import datetime as dt

MY_EMAIL = "nadunnissankatest@gmail.com"
MY_PASSWORD = "nadun123"

now = dt.datetime.now()
today = (now.month, now.day)

data = pd.read_csv("birthdays.csv")
birthday_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}
if today in birthday_dict:
    birthday_person = birthday_dict[today]
    birthday_person_email = birthday_person["email"]
    random_integer = random.randint(1, 3)
    file_path = f"letter_templates/letter_{random_integer}.txt"
    with open(file_path) as letter:
        content = letter.read()
        new_content = content.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person_email,
            msg=f"Subject:Happy Birthday!\n\n{new_content}"
        )
