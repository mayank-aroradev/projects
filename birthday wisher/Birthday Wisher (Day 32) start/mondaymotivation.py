import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()
if weekday==6:
    with open(r"C:\Users\dell\Desktop\projects\birthday wisher\Birthday Wisher (Day 32) start\quotes.txt") as quotes_file:


        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)


    my_email = "mayankarora25071@gmail.com"
    password = "dobs gglm azwv yvig"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password= password)
        connection.sendmail(from_addr=my_email,to_addrs="mayankaro25071@gmail.com", msg=f"Subject:Monday Motivation\n\n{quote}")

        