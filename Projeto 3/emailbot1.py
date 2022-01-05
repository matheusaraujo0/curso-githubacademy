import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "l.matheusrk@gmail.com"
toaddr = "l.matheusrk@gmail.com"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Olá, tudo bem?"

body = """Inauguração da nossa escola de programação, hoje a noite às 20hrs"""

msg.attach(MIMEText(body, 'plain'))

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()
s.login(fromaddr, 'kokiuheighimaru2')

text = msg.as_string()

s.sendmail(fromaddr, toaddr, text)
