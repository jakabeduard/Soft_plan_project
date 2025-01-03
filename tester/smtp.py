import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Email configuration
smtp_server = "edu.mailserver.ro"  # Replace with your SMTP server
smtp_port = 587  # Standard port for STARTTLS
sender_email = "janos@edutus.mailserver.ro"
sender_password = "012345"
recipient_email = "janoska@edutus.mailserver.ro"

# Create email content
subject = "Test Emailke"
body = "This is a test email sent from Pythonnnfvsdjfgnsdfjklnsdjkfgnsdfnkgsdjkfngksdfngjkadfnjksndfjksgdf."

# Setting up MIME
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))


file_path = "D:/IMG_20241026_200124_7.jpg"  # Replace with the actual file path
try:
    with open(file_path, "rb") as attachment:
        # Add file as application/octet-stream
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters for email
    encoders.encode_base64(part)

    # Add header for file attachment
    part.add_header(
        "Content-Disposition",
        f"attachment; filename={file_path.split('/')[-1]}"  # Extracts the file name
    )

    # Attach the file to the message
    message.attach(part)

    # Send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Upgrade the connection to secure
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())
        print("Email with attachment sent successfully!")
except Exception as e:
    print(f"Error: {e}")