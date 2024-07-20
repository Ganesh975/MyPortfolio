# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# def send_email(subject, body, to_email):
#     from_email = 'missionimpossible4546@gmail.com'
#     from_password = 'lemluekcftaaolcj'

#     # Create the email headers and set up the MIME
#     msg = MIMEMultipart()
#     msg['From'] = from_email
#     msg['To'] = to_email
#     msg['Subject'] = subject

#     # Attach the body with the msg instance
#     msg.attach(MIMEText(body, 'plain'))

#     try:
#         # Create the server connection
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()  # Start TLS (Transport Layer Security)
#         server.login(from_email, from_password)  # Login to the email server
#         text = msg.as_string()  # Convert the message to a string
#         server.sendmail(from_email, to_email, text)  # Send the email
#         server.quit()  # Logout from the email server

#         print(f'Email sent to {to_email}')
#     except Exception as e:
#         print(f'Failed to send email. Error: {str(e)}')

# if __name__ == "__main__":
#     subject = "Test Email"
#     body = "This is a test email sent from a simple Python script."
#     to_email = "ganeshyarrampati999@gmail.com"

#     send_email(subject, body, to_email)


from flask import Flask, request, render_template, jsonify
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configuration for Flask-Mail
EMAIL = 'missionimpossible4546@gmail.com'  # Your email
PASSWORD = 'lemluekcftaaolcj'  # Your app password (generated from Google)

def send_email(subject, body, to_email):
    from_email = EMAIL
    from_password = PASSWORD

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print(f'Email sent to {to_email}')
    except Exception as e:
        print(f'Failed to send email. Error: {str(e)}')

@app.route('/')
def index():
    return render_template('contact.html')

@app.route('/send_email', methods=['POST'])
def handle_contact_form():
    try:
        data = request.json
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']

        full_subject = f"Contact From Portfolio: {subject}"
        full_message = f"From: {name} <{email}>\n\n{message}"

        send_email(full_subject, full_message, 'ganeshyarrampati999@gmail.com')
        return jsonify({"message": "Email sent successfully!"}), 200
    except KeyError as e:
        return jsonify({"message": f"Missing key in request data: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"message": f"Failed to send email. Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
