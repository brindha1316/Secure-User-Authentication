import smtplib
from email.mime.text import MIMEText

def send_otp_email(receiver, otp):
    sender = "noreply@secureauth.com"
    msg = MIMEText(f"Your OTP is: {otp}")
    msg['Subject'] = "Secure Authentication OTP"
    msg['From'] = sender
    msg['To'] = receiver

    print(f"Sending OTP {otp} to {receiver}")  # Placeholder
    # smtp = smtplib.SMTP('smtp.gmail.com', 587)
    # smtp.starttls()
    # smtp.login(sender, "password")
    # smtp.sendmail(sender, receiver, msg.as_string())
    # smtp.quit()
