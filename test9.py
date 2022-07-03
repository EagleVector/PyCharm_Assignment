#Q9.Write a code to send a mail to your friend.

import os
import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login('datadummy09876@gmail.com', '1234@#$_')

server.sendmail('datadummy09876@gmail.com', 'kumarsubhambili3@gmail.com', 'Python demo Mail')
print('Mail Sent')