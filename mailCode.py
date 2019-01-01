# Python code to illustrate Sending mail from
# your Gmail account
import config

# Recepient
to_addr = 'sid.rvce@gmail.com'
test = "https://lol.cs"
# message to be sent
msg = """ 
Greetings!

You are receiving this email because you just registered for the RMS Tour of India 2019 Event. 
To complete this registration, please click on the link provided below: \n
""" + test + """ 
Thank you! 
- Team Name

P.S.: If you did not register for this event, please ignore this email. 
"""


def send_email(user, pwd, recipient, subject, body):
    import smtplib

    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.ehlo()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')

    except:
        print("failed to send mail")


send_email(config.username, config.password, to_addr, "Test", msg)
