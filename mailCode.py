# Python code to illustrate Sending mail from
# your Gmail account


def send_email(user , pwd , recipient , body, subject):
    import smtplib

    FROM = user
    TO = recipient if isinstance(recipient , list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM , ", ".join(TO) , SUBJECT , TEXT)
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com" , 465)
        server.ehlo()
        server.login(user , pwd)
        server.sendmail(FROM , TO , message)
        server.close()
        print('successfully sent the mail')

    except:
        print("failed to send mail")
