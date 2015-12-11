# Import global context
from flask.ext.mail import Mail, Message

# Import core libraries
from lib.decorators import async_threaded


mail = None
sender = None


def init(app):
    global mail, sender

    mail = Mail(app)
    sender = app.config['MAIL_USERNAME']


@async_threaded
def send_email(app, recipient, email, params):
    message = Message(email['subject'], sender=sender, recipients=[recipient])
    message.body = email['text']
    message.html = email['html'][params['html']]

    message.html += email['footer']

    with app.app_context():
        mail.send(message)
