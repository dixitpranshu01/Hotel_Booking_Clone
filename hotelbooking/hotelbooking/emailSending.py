def sendMail(emailid, pwd, subject="", html=""):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    # My email id
    me = ""
    EMAIL_APP_PASSWORD = ''  # The app password you generated
    you = emailid

    msg = MIMEMultipart('alternative')
    msg['From'] = me
    msg['To'] = you

    if subject == "registration confirmation":
        msg['Subject'] = "Profile Created Successfully"
    else:
        msg['Subject'] = subject

    if html == "":
        html = """<html>
                    <head></head>
                    <body>
                        <h1>Welcome to Booking Website</h1>
                        <p>You have successfully registered!!</p>
                        <h2>Username : """ + emailid + """</h2>
                        <h2>Password : """ + str(pwd) + """</h2>
                        <br>
                    </body>
                </html>
            """
    else:
        html = html

    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.login(me, EMAIL_APP_PASSWORD)

    part2 = MIMEText(html, 'html')
    msg.attach(part2)

    s.sendmail(me, you, msg.as_string())
    s.quit()
    print("Mail sent successfully....")
