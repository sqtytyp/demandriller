# TODO: send converted email
import os
import smtplib
from email.message import EmailMessage


def send(msg):
    with smtplib.SMTP_SSL('smtp.wp.pl', 465) as smtp:
        smtp.login("luenceconf@wp.pl", "C0nfluence")
        print(type(msg))
        smtp.send_message(msg)
        print("Message forwarded")


def sender_test():
    EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
    EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    msg = EmailMessage()
    msg['Subject'] = 'Check out Bronx as a puppy! 16:06'
    # msg['From'] = EMAIL_ADDRESS
    msg['From'] = "luenceconf@wp.pl"
    msg['To'] = 'daniszm@tt.com.pl'
    msg.set_content('This is a plain text email')
    msg.add_alternative("""\
    <!DOCTYPE html>
    <html>
        <body>
            <h1 style="color:SlateGray;">This is an HTML Email!</h1>
        </body>
    </html>
    """, subtype='html')
    with smtplib.SMTP_SSL('smtp.wp.pl', 465) as smtp:
        # smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.login("luenceconf@wp.pl", "C0nfluence")
        print(msg)
        smtp.send_message(msg)
    # return '250 OK'
    # with smtplib.SMTP('localhost', 10026) as smtp:
    #     #smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    #     #smtp.login("luenceconf@wp.pl", "C0nfluence")
    #     print(msg)
    #     smtp.send_mail("test@test.pl", "daniszm@tt.com.pl" ,msg)
    # #return '250 OK'

# sender_test()

# Serwer poczty wychodzącej - smtp.wp.pl
# Port serwera poczty wychodzącej - 465
# Tryb zabezpieczenia - SSL
# Serwer wymaga uwierzytelnienia / włączonej autoryzacji SMTP.
# luenceconf@wp.pl / C0nfluence
