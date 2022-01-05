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

html = """
<html>
    <body>
        <p>Olá,<br>
        Como vai você?<br>
        <a href="https://www.youtube.com/watch?v=m1rVsNXeofM">Clique Aqui!!!</a>
        para ver o vídeo!
        </p>
    </body>
<html>
"""

part1 = MIMEText(html, "html")
msg.attach(part1)

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()
s.login(fromaddr, 'kokiuheighimaru2')

text = msg.as_string()

s.sendmail(fromaddr, toaddr, text)
