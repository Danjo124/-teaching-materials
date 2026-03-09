import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

SENDER_EMAIL = "digitassistantdaniel@gmx.net"
GMX_APP_PASSWORD = "NQKSUQVFNR5XTTB3WRGZ"
SMTP_SERVER = "mail.gmx.net"
SMTP_PORT = 587

def send_email(to_email, subject, body, attachment_paths):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain', 'utf-8'))
    
    for file_path in attachment_paths:
        if not os.path.exists(file_path):
            continue
        filename = os.path.basename(file_path)
        with open(file_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename={filename}")
        msg.attach(part)
    
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SENDER_EMAIL, GMX_APP_PASSWORD)
    server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
    server.quit()

if __name__ == "__main__":
    send_email(
        "tek@biondekgasse.at",
        "Arbeitsblatt: Question Words & Object Pronouns",
        "Hallo Daniel,\n\nhier ist das gewünschte Arbeitsblatt zu den Themen Question Words, Object Pronouns, Irregular Plurals und Possessive 's.\n\nViele Grüße,\nDigit ✍️",
        ["Grammar_Worksheet_Questions_Objects.pdf"]
    )
    print("Email sent.")
