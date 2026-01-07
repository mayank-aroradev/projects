import datetime as dt
import pandas
import random
import smtplib

# Get today's date
today = dt.datetime.now()
today_tuple = (today.month, today.day)

# Read birthdays CSV
data = pandas.read_csv(r"birthday wisher\birthdays.csv")

# Create birthday dictionary
birthdays_dict = {
    (row.month, row.day): row
    for _, row in data.iterrows()
}

# Check if today matches any birthday
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]

    # Pick random letter
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    my_email = "mayankarora25071@gmail.com"
    password = "dobsgglmazwvyv"  # app password

    # Send email
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday 🎉\n\n{contents}"
        )

   



