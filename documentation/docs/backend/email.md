# Email

### Development

MailHog is being used to test the sending of emails for free in a development environment. It is an email-testing tool with a fake SMTP server underneath. To view the emails which have been sent, open `http://localhost:8025/` in your browser, which will open the MailHog user interface.

If you haven't got it installed already, Mailhog should automatically install when you run `docker compose up`.

### Production

Sendgrid is used to send and receive emails in the production version of the application. The Community Spirit Foundation email account has been added as the sender. The Sendgrid account is made under Coders For Causes credentials and will allow for 100 free emails per day, anything over will cost $20 per month.

Password reset emails will be sent from the Community Spirit Foundation email address to the user email that requests the change.

Everytime a new user has created an account the Community Spirit Foundation email address will receive an email to let admin know.
