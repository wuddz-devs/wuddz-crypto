"""MODULE CONTAINING ALL WUDDZ_CRYPTO BIP44HDWALLET METHODS"""

import docs, re, main, json, base64
from getpass import getpass
from hdwallet import BIP44HDWallet, symbols
from hdwallet.utils import is_mnemonic, is_entropy, generate_entropy, generate_passphrase
from cryptography.fernet import Fernet


lang={1: 'english', 2: 'spanish', 3: 'french', 4: 'italian', 5: 'japanese', 
      6: 'korean', 7: 'chinese_simplified', 8: 'chinese_traditional'}

def wsym() -> dict:
    """Returns Dictionary Consisting Of All Supported BIP44HDWallet Symbol Keys & Token Name Values."""
    return {s:wobj(s).cryptocurrency() for s in symbols.__all__}

def wobj(sym: str, acc: int=0, chg: bool=False, adr: int=0):
    """
    Returns BIP44 Hierarchical Deterministic Wallet Instance.
    :param sym: Cryptocurrency Symbol e.g `BTC`
    :param acc: Wallet Account Index Default to 0 e.g 1
    :param chg: Change Addresses Default To `False`
    :param adr: Wallet Address Index Default To 0 Maximum 19 (i.e 20 Per Account Index)
    """
    return BIP44HDWallet(symbol=sym.upper(), account=acc, change=chg, address=adr)

def wkey(fn: str, pwd: str, rgx: str) -> str:
    """
    Returns Fernet Decrypted Data From A File As String.
    :param fn:  File Containing Encrypted Data e.g `wallet_enc.txt`
    :param pwd: Fernet Key To Decrypt Encrypted Data e.g 's03fusf'
    :param rgx: Regex String To Retrieve Encrypted Data e.g `adr (.*)`
    """
    with open(fn, 'r', encoding='utf-8') as wr:
        i=re.search(rgx,wr.read()).group(1)
        dec=Fernet(bytes(pwd, 'utf-8'))
        return dec.decrypt(eval(i))

def wenc(op, adr: str, efn: str, kfn: str):
    """
    Write Fernet Encrypted Data To File & Write Identity String & Base64 Encoded Fernet Key To File.
    :param op:  Data To Be Encrypted & Written To File
    :param adr: String To Identify Fernet Key e.g `Token Address`
    :param efn: Output File For Encrypted Data e.g `wallet_enc.txt`
    :param kfn: Output File For Identity String & Base64 Fernet Key e.g `wallet_key.txt`
    """
    with open(efn, 'a', encoding='utf-8') as fw:
        with open(kfn, 'a', encoding='utf-8') as kw:
            k=Fernet.generate_key()
            e=Fernet(k)
            if type(op) is dict:o=bytes(json.dumps(op), 'utf-8')
            else:o=bytes(op, 'utf-8')
            fw.write(str(k)[:10]+"==' "+str(e.encrypt(o))+'\n')
            kw.write(adr+' '*(50-len(adr))+str(base64.urlsafe_b64encode(bytes(str(k),'utf-8')))+"\n")

def wdec(op, dfn: str):
    """
    Write Data To Output File.
    :param op:  Data To Write To File
    :param dfn: Output File e.g `wallet_dec.txt`
    """
    with open(dfn, 'a') as fw:
        if type(op) is dict:fw.write(json.dumps(op, indent=4)+'\n\n')
        else:fw.write(op+'\n')

def wgen(bp, ent: str=None, stn: int=128, lan: str='english', pwd: str=None):
    """
    Returns BIP44HDWallet Object With Created Wallet.
    :param bp:  BIP44HDWallet Instance
    :param ent: Entropy To Create Wallet From, Will Be Generated If None
    :param stn: Strength Of Entropy Default To 128 e.g `128, 160, 192, 224, 256`
    :param lan: Language Of Entropy Default To English,
                e.g `english, spanish, french, italian, japanese, korean, chinese_simplified, chinese_traditional`
    :param pwd: Password Of Entropy If Specified Default To None
    """
    if ent is None:ent=generate_entropy(strength=stn)
    return bp.from_entropy(entropy=ent, language=lan, passphrase=pwd)

def wauth(s: str=None):
    """
    Loads Menu To Return Bip44HDWallet Instance From Private Key/Mnemonic/Entropy/Wif.
    :param s: Symbol Of Token & Signifies Menu Type e.g `btc = Wallet Authentication For BTC`
    """
    bl=[]
    ec=True
    kd={'e ': 'ent', 'p ': 'pass', 'w ': 'wif', 'k ': 'key', 'm ': 'seed'}
    ad={'l ': 'lan', 'p ': 'pwd', 'a': 'ath', 'c ': 'aci', 'r ': 'adi'}
    od={'sym': s, 'lan': 1, 'aci': 0, 'adi': 0, 'pwd': None, 'ath': None}
    vd={'sym': s, 'lan': 1, 'aci': 0, 'adi': 0, 'pwd': None, 'ath': None}
    dc=docs.lw.format(docs.lwc,docs.lwe)+docs.lwa.format('Optional:')
    if not s:
        ad['s ']='sym'
        od['enc']=True
        vd.update(od)
        cl=wsym()
        dc=docs.lw.format(docs.lwb+main.doc_create(cl,s='{} = {}'),docs.lwd)+docs.lwa.format(docs.lwl)
    while True:
        try:
            main.clear_screen()
            arg=input('\033[1;32;40m'+dc+'\033[1;34;40m\n'+' '*4+'Current Arguments:\n'+' '*4+str(vd)+'\n\033[0m\nInput Argument=> ')
            if arg=='b':
                bl=['']
                break
            elif arg=='e':main.pexit()
            elif arg=='h':vd.update(od)
            elif arg=='d' and not s:vd['enc']=False
            elif arg=='t' and not s:vd['enc']=True
            elif arg[0]=='a':vd['ath']=arg[1:]
            elif ad.get(arg[:2]):vd[ad.get(arg[:2])]=arg[2:]
            elif arg=='x' and vd['ath']:
                vd['lan']=lang[int(vd['lan'])]
                for i in sorted(set(vd['sym'].split(','))):
                    bp=wobj(i, acc=int(vd['aci']), adr=int(vd['adi']))
                    a=kd[vd['ath'][:2]]
                    v=vd['ath'][2:]
                    if a in ['wif','key','pass']:
                        if a=='pass':
                            p=json.loads(wkey(main.wec,v,"b'"+v[:8]+"==' (.*)"))
                            v=p['private_key']
                        if len(v)==64:bp.from_private_key(v)
                        else:bp.from_wif(v)
                    elif a in ['ent','seed']:
                        if is_mnemonic(v):bp.from_mnemonic(v, language=vd['lan'], passphrase=vd['pwd'])
                        elif is_entropy(v):bp.from_entropy(v, language=vd['lan'], passphrase=vd['pwd'])
                    if not s:ec=vd['enc']
                    bl.append(bp)
                break
        except:
            vd.update(od)
            main.get_menu('e')
    if not s:return bl,ec
    return bl[0]

def wload():
    """Loads Menu To Save Bip44HDWallet Cryptocurrency Wallet Dictionary To Output File From Private Key/Mnemonic/Entropy/Wif."""
    wss=''
    ec='\033[1;34;40m{} \033[1;32;40m(Encrypted Info Saved To {})\n'
    dc='\033[1;34;40m{} \033[1;32;40m(Decrypted Info Saved To {})\n'
    bp,enc=wauth()
    if not bp[0]:return
    for b in bp:
        w=f'{b.symbol()} => {b.address()}'
        if enc:
            wenc(b.dumps(), b.address(), main.wec, main.wky)
            wss+=ec.format(w, main.wky)
        else:
            wdec(b.dumps(), main.wdc)
            wss+=dc.format(w, main.wdc)
    if wss:main.get_menu(f'\n{wss}')

def wcreate():
    """Loads Menu To Create Bip44HDWallet Cryptocurrency Wallet."""
    ad={'s ': 'sym', 'm ': 'stn', 'l ': 'lan', 'p ': 'pwd', 'a ': 'ath', 'c ': 'aci', 'r ': 'adi'}
    od={'sym': None, 'stn': 12, 'lan': 1, 'pwd': None, 'ath': None, 'aci': 0, 'adi': 0, 'enc': True}
    vd={'sym': None, 'stn': 12, 'lan': 1, 'pwd': None, 'ath': None, 'aci': 0, 'adi': 0, 'enc': True}
    cl=wsym()
    dc=main.doc_create(cl,s='{} = {}')
    mns={12: 128, 15: 160, 18: 192, 21: 224, 24: 256}
    while True:
        try:
            wss=''
            main.clear_screen()
            arg=input('\033[1;32;40m'+docs.cw.format(dc)+'\033[1;34;40m\n'+' '*4+'Current Arguments:\n'+' '*4+str(vd)+'\n\033[0m\nInput Argument=> ')
            if arg=='b':break
            elif arg=='d':vd['enc']=False
            elif arg=='e':main.pexit()
            elif arg=='h':vd.update(od)
            elif arg=='t':vd['enc']=True
            elif ad.get(arg[:2]):vd[ad.get(arg[:2])]=arg[2:]
            elif arg=='x':
                vd['lan']=lang[int(vd['lan'])]
                vd['stn']=mns[int(vd['stn'])]
                if vd.get('ath'):
                    if is_mnemonic(vd['ath']):vd['ath']: str = mnemonic_to_entropy(mnemonic=vd['ath'], language=vd['lan'])
                    assert is_entropy(vd['ath'])
                else:vd['ath']: str = generate_entropy(strength=vd['stn'])
                if vd.get('pwd') is None:vd['pwd']=str(generate_passphrase(32))
                for i in vd['sym'].split(','):
                    a=i.split('-')
                    s=a[0].upper()
                    if cl.get(s):
                        b=1
                        if len(a)==2:b=int(a[1])
                        if b>20:raise ValueError
                        for x in range(b):
                            bp=wobj(s, acc=int(vd['aci']), adr=x)
                            bp=wgen(bp, ent=vd['ath'], lan=vd['lan'], pwd=vd['pwd'])
                            wss+=f'{s} => {bp.address()}\n'
                            if vd['enc']:wenc(bp.dumps(), bp.address(), main.wec, main.wky)
                            else:wdec(bp.dumps(), main.wdc)
                if wss:main.get_menu(f'\n\033[1;34;40m{wss}\033[0m')
                vd.update(od)
        except:
            vd.update(od)
            main.get_menu('e')
