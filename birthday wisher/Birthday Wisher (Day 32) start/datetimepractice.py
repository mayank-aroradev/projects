# import smtplib

# my_email = "mayankarora25071@gmail.com"
# password = "dobs gglm azwv yvig"

# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(
# from_addr=my_email,
# to_addrs="mayankaro25071@gmail.com",
# msg="Subject: Test Email\n\nHello from Python!"
# )


import datetime as dt
now = dt.datetime.now()
time= now.time()
year=now.year
month=now.month 
print(time)
