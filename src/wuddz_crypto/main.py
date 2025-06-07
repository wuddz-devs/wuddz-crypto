"""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░██╗░░░░░░░██╗██╗░░░██╗██████╗░██████╗░███████╗░░░░░░░█████╗░██████╗░██╗░░░██╗██████╗░████████╗░█████╗░░
░██║░░██╗░░██║██║░░░██║██╔══██╗██╔══██╗╚════██║░░░░░░██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝██╔══██╗░
░╚██╗████╗██╔╝██║░░░██║██║░░██║██║░░██║░░███╔═╝█████╗██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░██║░░██║░
░░████╔═████║░██║░░░██║██║░░██║██║░░██║██╔══╝░░╚════╝██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░██║░░██║░
░░╚██╔╝░╚██╔╝░╚██████╔╝██████╔╝██████╔╝███████╗░░░░░░╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░╚█████╔╝░
░░░╚═╝░░░╚═╝░░░╚═════╝░╚═════╝░╚═════╝░╚══════╝░░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░░╚════╝░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

 [*]Descr:     MULTI BLOCKCHAIN CRYPTOCURRENCY APP, CREATE WALLET WITH MULTIPLE TOKENS FROM VARIOUS     
               BLOCKCHAINS, CHECK BALANCES, MAKE TRANSACTIONS, GET TRANSACTION HASH DATA, GET CURRENT   
               CRYPTO PRICES, GET VALUE OF TOKEN IN OTHER CRYPTOCURRENCIES & DECODE BASE64 STRING       
 [*]Coder:     Wuddz_Devs                                                                               
 [*]Email:     wuddz_devs@protonmail.com                                                                
 [*]Github:    https://github.com/wuddz-devs                                                            
 [*]Reddit:    https://reddit.com/users/wuddz-devs                                                      
 [*]Telegram:  https://t.me/wuddz_devs                                                                  
 [*]Videos:    https://mega.nz/folder/IWVAXTqS#FoZAje2NukIcIrEXXKTo0w                                   
 [*]Youtube:   https://youtube.com/@wuddz-devs                                                          
 [*]Donation:                                                                                           
     BTC   ->  bc1qa7ssx0e4l6lytqawrnceu6hf5990x4r2uwuead                                               
     ERC20 ->  0xbF4d5309Bc633d95B6a8fe60E6AF490F11ed2Dd1                                               
     LTC   ->  LdbcFiQVUMTfc9eJdc5Gw2nZgyo6WjKCj7                                                       
     TRON  ->  TY6e3dWGpqyn2wUgnA5q63c88PJzfDmQAD                                                       
     DOGE  ->  DFwLwtcam7n2JreSpq1r2rtkA48Vos5Hgm                                                       
"""

import re, requests, base64, sys, docs, wallet
from pycoingecko import CoinGeckoAPI
from os import mkdir, name, path, system, _exit
from time import sleep
requests.packages.urllib3.disable_warnings()
system('')

# CoinGeckoAPI Instance
cg=CoinGeckoAPI()

# Create `CRYPTO` Output Directory In User's Desktop Directory
pkg=path.join(path.expanduser('~'),'Desktop','CRYPTO')
if not path.exists(pkg):mkdir(pkg)

# Output Files For Wuddz_Crypto
wec=path.join(pkg, 'wallet_enc.txt')   # Wallet Encrypted Data File
wdc=path.join(pkg, 'wallet_dec.txt')   # Wallet Decrypted Data File
wky=path.join(pkg, 'wallet_key.txt')   # Wallet Base64 Encoded Fernet Key File
txr=path.join(pkg, 'tx_receipts.txt')  # Tranaction Hash Details File
btx=path.join(pkg, 'broadcast_tx.txt') # Tranactions To Be Broadcasted File

# Common Strings
hs='\n\033[1;34;40mTx_Hash: {}\n'
ns='\n\033[1;34;40m    Current Network: {}\n'
vs='\n\033[1;34;40mTransfer Amount: {} {}\nTransfer From: {}\nTransfer To: \
{}\n\n\033[1;32;40mDo You Approve This Transaction? Input y1 | y2 or n=> \033[0m'
ts='\n\033[1;34;40mOwner Address: {}\nDeposit Address: {}\nDeposit Amount: \
{} {}\nTx Hash: {}\n'+'\033[1;32;40m-'*164+'\n'

def pexit():
    """Clear CLI Screen & Exit Program."""
    clear_screen()
    _exit(0)

def clear_screen():
    """Clear Command Line Screen."""
    if name=='nt':system('cls')
    else:system('clear')

def get_menu(m: str=''):
    """
    Print Output To Screen & Wait For User Input.
    :param m: Optional String To Print To Screen, If String Is `e` Prints `*Error Occurred*`
    """
    clear_screen()
    if m=='e':m='\n\033[1;31;40m*Error Occurred*'
    a=input('\033[1;32;40m[*]OUTPUT:\n'+m+'\n\n\033[1;32;40m...Hit Enter|Return Key To Continue....\033[0m\n') or None

def slow_print(doc: str, sp: float=0.0005):
    """
    Print String By Speed In Seconds Less Is Faster.
    :param doc: String To Be Printed
    :param sp:  Speed To Print String `e.g 0.0001 or 0.0005 used`
    """
    for d in doc:
        sys.stdout.write(f"\033[1;32;40m{d}")
        sleep(sp)

def doc_create(d, a: int=5, b: int=29, s: str=None) -> str:
    """
    Returns Docstring Formatted From List Or Dictionary.
    :param d: Iterable To Create Docstring From e.g List or Dictionary
    :param a: Amount Of Columns In Docstring e.g `4 default is 5`
    :param b: Character Length Between Beginning Of Each Column e.g `20 default is 29`
    :param s: String To Be Formatted With Variable(s) i.e Key & Value If Iterable Is Dictionary e.g `{} = {}.format(k,v)`
    """
    sv=''
    dc=0
    for k in d:
        dc+=1
        if s and type(d) is dict:k=s.format(k, d[k])
        if dc==1:sv+=' '*4+k+' '*(b-len(k))
        elif dc==a:
            sv+=k+'\n'
            dc=0
        else:sv+=k+' '*(b-len(k))
    return sv

def js_resp(url: str) -> dict:
    """
    Returns Url Response As Json Dictionary.
    :param url: Url e.g `https://apilist.tronscanapi.com/`
    """
    return requests.get(url, verify=False).json()

def bindex():
    """Returns Index Integer For Broadcast Output File."""
    i=0
    if path.exists(btx):
        with open(btx, 'r') as r:
            b=re.findall('(\d+)=',r.read())
            if b:i=int(b[-1])+1
    return i

def decode_bsf():
    """Loads Menu To Decode Base64 String & Print To Screen."""
    while True:
        clear_screen()
        bss=input(f'\033[1:32;40m{docs.ds}\n\033[0mInput Base64 String=> ') or None
        if bss=='b':break
        elif bss=='e':pexit()
        elif bss:get_menu('\n\033[1;34;40m'+str(base64.b64decode(bss).decode('utf-8'))+'\033[0m')

def get_price(i: str='bitcoin'):
    """
    Return Price Of Token In Usd Using CoinGecko API Token ID.
    :param i: Coingecko Token Id To Get Usd Value Defaults To BTC e.g `bitcoin`
    """
    return cg.get_price(i,'usd')[i]['usd']

def crypto_price():
    """Loads Menu To Get Crypto Price & Conversion Using CoinGecko API."""
    while True:
        try:
            clear_screen()
            cc=input(f'\033[1;32;40m{docs.cp}\n\033[0mInput Choice => ') or None
            if cc=='s':token_id()
            elif cc=='b':break
            elif cc=='e':pexit()
            elif cc:
                ccl=cc.split()
                cd=cg.get_coin_by_id(ccl[1])
                cpa=cg.get_price(cd['id'],'usd')[str(cd['id'])]['usd']
                crp="${:,.2f}".format(float(ccl[0])*float(cpa))
                syma=cd['symbol'].upper()
                if len(ccl)==2:get_menu(f"\n\033[1;34;40m{cc.replace(ccl[1],syma)} => {crp} USD\033[0m")
                elif len(cc.split())==3:
                    cb=cg.get_coin_by_id(ccl[2])
                    symb=cb['symbol'].upper()
                    cpb=cg.get_price(ccl[2],'usd')[str(ccl[2])]['usd']
                    cvv=float(ccl[0])*(float(cpa)/float(cpb))
                    get_menu(f"\n\033[1;34;40m{ccl[0]} {syma} => {cvv} {symb}\nTotal Value => {crp} USD\033[0m")
        except requests.exceptions.ConnectionError:
            get_menu(f'\n\033[1;31;40mNo Connection Error!!\033[0m')
        except:get_menu(f'\n\033[1;31;40m{cc} Not Valid!!\033[0m')

def token_id():
    """Loads Menu To Search For Token Id Using CoinGecko API."""
    while True:
        clear_screen()
        st=input(f"\033[1;32;40m{docs.st}\n\033[0mInput String or b=> ")
        if st=='b':break
        elif st=='e':pexit()
        elif st:
            sd=cg.search(st)['coins']
            print('')
            for i in range(len(sd)):
                print("Id: {},  Name: {},  Symbol: {}".format(sd[i]['id'], sd[i]['name'], sd[i]['api_symbol']))
            input('\n\n\033[1;32;40m...Hit Enter|Return Key To Continue....\033[0m\n') or None

def menu():
    """Wuddz_Crypto Entry Point Loads Wuddz-Crypto Menu."""
    while True:
        try:
            clear_screen()
            slow_print(__doc__+docs.mm)
            mc=input("\033[0m\nInput Choice=> ")
            if mc=='e':pexit()
            elif mc=='1':
                import btc_chain
                btc_chain.cli_main()
            elif mc=='2':
                import trx_chain
                trx_chain.cli_main()
            elif mc=='w':wallet.wcreate()
            elif mc=='l':wallet.wload()
            elif mc=='d':decode_bsf()
            elif mc=='p':crypto_price()
        except:pass
