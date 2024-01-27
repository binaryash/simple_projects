import smtplib

my_email = "123@email.com"
password = "******"

connection = smtplib.SMTP("smtp.office365.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs="456@email.com",
    msg='''Subject: The Newsletter - Thank you for subscribing!
    \n\n
    Dear [Subscriber's Name],

    Thank you for subscribing to The Newsletter! We're excited to have you on board. Here are a few details to keep in mind:

    Subscription Email: Subscriber's Email Address
    Subscription Date: Date of Subscription

    As a subscriber, you'll receive regular updates and valuable content straight to your inbox. We aim to provide you with insightful articles, industry news, and exclusive offers. We appreciate your interest and look forward to sharing valuable information with you.
    If you ever wish to unsubscribe, simply click on the "Unsubscribe" link at the bottom of any email you receive from us.
    Thank you once again for joining our newsletter community!

    Best regards,
    Your Name
    Your Organization''')

connection.close()
