from dotenv import load_dotenv
import datetime as dt
import smtplib
import random
import os

load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
send_to = os.getenv("TO_EMAIL")

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", 587, timeout=10) as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(
            from_addr=email,
            to_addrs=send_to,
            msg=f"Subject: Segundas motivacionais\n\n{quote}"
        )
