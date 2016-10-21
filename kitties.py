import smtplib, os, urllib2, urllib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

url = "http://thecatapi.com/api/images/get"
# Change these variables
#################################
gmail = 'gmailAddress@gmail.com'
passw = 'yourPassword'
users = [
    {'name': "NameIfYouWant", 'number': "5555555555", 'carrier': "c_map_key"},   
]
#################################
c_map = {
    'ATT': 'mms.att.net',
    'Alltel': 'mms.alltelwireless.com',
    'Boost': 'myboostmobile.com',
    'Cricket': 'mms.mycricket.com',
    'Sprint': 'pm.sprint.com',
    'T-Mobile': 'tmomail.net',
    'Us Cellular': 'mms.uscc.net',
    'Verizon': 'vzwpix.com',
    'Virgin Mobile': 'vmpix.com',
}

def SendMail(fle, pictype, num, c_url):
    img_data = open(fle, "rb").read()
    msg = MIMEMultipart()
    msg['Subject'] = ''
    msg['From'] = gmail
    msg['To'] = num+"@"+c_url
    text = MIMEText("Daily dose of the cats!!")
    msg.attach(text)
    image = MIMEImage(img_data, _subtype=pictype, name=os.path.basename(fle))
    msg.attach(image)
    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(gmail, passw)
    server.sendmail(gmail, num+"@"+c_url, msg.as_string())
    server.quit()

def GetRandomKitty():
    res = urllib2.urlopen(url)
    ct = res.info().getheader('Content-Type')
    pictype = ct[ct.index("/")+1:]
    fle = "kitty."+ct[ct.index("/")+1:]
    f = open(fle, "wb")
    f.write(res.read())
    f.close()
    return [fle, pictype]

def DeletePic(fle):
    os.remove(fle)

if __name__ == '__main__':
    res = GetRandomKitty()
    for user in user:
        SendMail(res[0], res[1], user['number'], c_map[user['carrier']])
    DeletePic(res[0])
