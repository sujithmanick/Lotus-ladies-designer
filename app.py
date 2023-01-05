from flask import Flask,render_template,request,session
import smtplib
from email.mime.text import MIMEText
app = Flask(__name__)
app.secret_key = "@78#45SjApp"
def send_email(message):
    try:
        smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
        smtp_ssl_port = 465
        username = 'lotusladiesdesigners@gmail.com'
        password = 'PASSWORD'
        sender = 'lotusladiesdesigners@gmail.com'
        targets = 'MAIL_ID'
        msg = MIMEText('Message : {}'.format(message))
        msg['Subject'] = 'User Message'
        msg['From'] = sender
        msg['To'] = targets

        server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
        server.login(username,password)
        server.sendmail(sender,targets,msg.as_string())
        server.quit()
    except Exception as e:
        print(e)


def send_email_cl(name,email):
    try:
        smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
        smtp_ssl_port = 465
        username = 'lotusladiesdesigners@gmail.com'
        password = 'PASSWORD'
        sender = 'lotusladiesdesigners@gmail.com'
        targets = email
        msg = MIMEText('Thanks, {} For Choosing us...'.format(name))
        msg['Subject'] = 'User Message'
        msg['From'] = sender
        msg['To'] = targets

        server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
        server.login(username,password)
        server.sendmail(sender,targets,msg.as_string())
        server.quit()
    except Exception as e:
        print(e)

@app.route("/",methods=['GET','POST'] )
def home():
    if request.method == 'GET':
        return render_template("index.html")
    elif request.method == 'POST':
        session['DATA'] = request.form
        name = session['DATA']['name']
        email=session['DATA']['email']
        st=''
        for k,v in dict(session['DATA']).items():
            st+=str(k).capitalize()+" : "+str(v)+"\n"
        send_email(st)
        send_email_cl(name,email)

        
        return render_template("index.html")
if __name__ == '__main__':
    
    app.run(debug=True)   
