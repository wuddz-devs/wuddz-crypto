"""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░██████╗░████████╗░█████╗░░░░░░░░█████╗░██╗░░██╗░█████╗░██╗███╗░░██╗░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░██╔══██╗╚══██╔══╝██╔══██╗░░░░░░██╔══██╗██║░░██║██╔══██╗██║████╗░██║░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░██████╦╝░░░██║░░░██║░░╚═╝█████╗██║░░╚═╝███████║███████║██║██╔██╗██║░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░██╔══██╗░░░██║░░░██║░░██╗╚════╝██║░░██╗██╔══██║██╔══██║██║██║╚████║░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░██████╦╝░░░██║░░░╚█████╔╝░░░░░░╚█████╔╝██║░░██║██║░░██║██║██║░╚███║░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░╚═════╝░░░░╚═╝░░░░╚════╝░░░░░░░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

 [*]Descr:     INTERACT WITH BTC MAINNET & TESTNET BLOCKCHAINS TO MAKE TRANSACTIONS & CHECK BALANCES 
 [*]Email:     wuddz_devs@protonmail.com                                                             
 [*]Github:    https://github.com/wuddz-devs                                                         
 [*]Donation:                                                                                        
     BTC   ->  bc1qa7ssx0e4l6lytqawrnceu6hf5990x4r2uwuead                                            
     ERC20 ->  0xbF4d5309Bc633d95B6a8fe60E6AF490F11ed2Dd1                                            
     LTC   ->  LdbcFiQVUMTfc9eJdc5Gw2nZgyo6WjKCj7                                                    
     TRON  ->  TY6e3dWGpqyn2wUgnA5q63c88PJzfDmQAD                                                    
     DOGE  ->  DFwLwtcam7n2JreSpq1r2rtkA48Vos5Hgm                                                    
"""
import docs, re, json, main, wallet
from blockcypher import get_address_overview, get_transaction_details, from_base_unit
from bit import Key, PrivateKeyTestnet, SUPPORTED_CURRENCIES
from bit.network import NetworkAPI
from bit.transaction import calc_txid
from getpass import getpass
from os import system
from time import sleep
system('')


class Btc:
    def __init__(self):
        """Connect & Interact Wtih Bitcoin Mainnet/Testnet Blockchains."""
        self.nw='Mainnet'
        self.ba='\n\033[1;34;40mAddress: {}\nBalance: {} {}\nUSD: ${}\nTx_Count: {}\nTotal_Received: {}\nTotal_Sent: {}\033[0m'
        self.ds={'Mainnet': 'btc', 'Testnet': 'btc-testnet'}
        self.bb={'Mainnet': 'BTC', 'Testnet': 'BTCTEST'}
    
    def get_network(self):
        """Loads Menu To Choose BTC Network."""
        main.clear_screen()
        nd={'1': 'Mainnet', '2': 'Testnet'}
        nc=input(f'\033[1;32;40m{docs.bns}\n\033[0mInput Network Choice=> ') or '1'
        if nd.get(nc):self.nw=nd[nc]
    
    def get_balance(self):
        """Loads Menu To Get Address Balance."""
        while True:
            try:
                main.clear_screen()
                bs=input(f'\033[1;32;40m{docs.bd}{main.ns.format(self.nw)}\n\033[0mInput Address=> ') or None
                if bs=='b':break
                elif bs=='n':self.get_network()
                elif bs=='e':main.pexit()
                elif bs:
                    st=self.bal_values(bs, s=self.ds[self.nw])
                    main.get_menu(st)
            except:pass
    
    def bal_values(self, a: str, s: str='btc'):
        """
        Returns String Containing Address Info From Blockcypher API Json Response.
        :param a: Address To Get API Balance Response For
        :param s: Symbol Defaults To btc e.g `btc-testnet`
        """
        try:
            b=get_address_overview(a,s)
            bal=from_base_unit(int(b['balance']),'btc')
            tc=b['n_tx']
            tr=from_base_unit(int(b['total_received']),'btc')
            ts=from_base_unit(int(b['total_sent']),'btc')
            bu="{:,.2f}".format(float(main.get_price())*float(bal))
            return self.ba.format(a,bal,'BTC',bu,tc,tr,ts)
        except:return '\n\033[1;31;40m*Error Occurred*'
    
    def transfer_btc(self):
        """Loads Menu To Transfer/Deposit BTC."""
        ds=main.doc_create(dict(SUPPORTED_CURRENCIES), s='{} = {}')
        while True:
            try:
                main.clear_screen()
                a=docs.bsb.format(ds)+main.ns.format(self.nw)
                bt=input(f'\033[1;32;40m{a}\n\033[0mInput Deposit Format => ') or None
                if bt=='b':break
                elif bt=='e':main.pexit()
                elif bt=='n':self.get_network()
                elif bt:
                    v=bt.split()
                    if len(v)==4 and SUPPORTED_CURRENCIES.get(v[3]):
                        self.transfer_exec(v[0], v[1], v[2], v[3]) # Transfer Specified Amount From Owner To Deposit Address
                    elif len(v)==2:
                        bb=self.token_bal(v[0],self.ds[self.nw]) # Get Balance Of Address Internet Connection Required
                        self.transfer_exec(v[0], v[1], bb, 'BTC', ta='a') # Transfer All BTC From Owner To Deposit Address
                    else:raise ValueError
            except:main.get_menu('e')
    
    def transfer_exec(self, own: str, dpa: str, amt: str, cur: str, ta: str=None) -> str:
        """
        Loads A Prompt To Verify & Specify Transaction Signing On Or Offline Before Execution.
        :param own: Owner Address To Transfer From
        :param dpa: Deposit Address To Transfer To
        :param amt: Amount To Transfer e.g `0.01`
        :param cur: Currency Of Specified Amount To Transfer e.g `satoshi`
        :param ta:  String To Specify Type Of BTC Transfer e.g `all` = Transfer All BTC
        """
        main.clear_screen()
        ti='No Transaction occurred'
        ts=main.vs.format(amt, cur.upper(), own, dpa)
        et=input(f'\033[1;32;40m{docs.bc}\n\033[1;34;40mCurrent Network: {self.nw}'+ts) or 'n'
        if et in ['y1','y2']:
            try:
                bn=self.bit_nkey(self.nw[0])
                if ta:tx=self.btc_prep_all(bn, own, dpa) # Build Transaction To Transfer All BTC Internet Connection Required.
                else:tx=self.btc_prep_tx(bn, own, dpa, amt, cur) # Build Transaction To Transfer BTC Internet Connection Required.
                if et=='y2':
                    main.get_menu('\n\033[1;34;40mDisconnect Internet Connection Now To Sign Transaction Offline')
                    bk=self.bit_authenticate() # Authenticated Bit Instance To Sign Transaction No Internet Connection Required.
                    if not bk:return
                    hx=bk.sign_transaction(tx) # Signed Transaction Hexadecimal Result No Internet Connection Required.
                    i=main.bindex()
                    wallet.wdec('{}={}'.format(str(i), hx), main.btx)
                    main.get_menu(f'\n\033[1;34;40mTransaction Data Index {i} Saved To {main.btx} Successfully')
                else:
                    bk=self.bit_authenticate()
                    if not bk:return
                    hx=bk.sign_transaction(tx)
                    ti=self.broadcast_tx(hx, n=self.nw[0]) # Broadcast Transaction Internet Connection Required.
                    if 'Error' in ti:raise ValueError
                    sleep(5)
                    self.tx_hash(ti)
                    main.get_menu(main.ts.format(own,dpa,amt,cur,ti))
            except:main.get_menu(f'\033[1;31;40m*Error {ti}*')
    
    def balance_fkey(self):
        """Loads Menu To Print Address & Balance Of Private Key/Entropy/Mnemonic/Wif."""
        self.get_network()
        bk=self.bit_authenticate()
        if not bk:return
        st=self.bal_values(bk.address, self.ds[self.nw])
        main.get_menu(st)
    
    def tx_sub(self):
        """Loads Menu To Print Transaction Hash Info To Screen."""
        while True:
            try:
                main.clear_screen()
                th=input(f'\033[1;32;40m{docs.ts}{main.ns.format(self.nw)}\n\033[0mInput Hash=> ') or None
                if th=='b':break
                elif th=='e':main.pexit()
                elif th=='n':self.get_network()
                elif len(th)==64:self.tx_hash(th,o='p')
            except:pass
    
    def tx_hash(self, h: str, o: str=None, n: str=None):
        """
        Write Transaction Hash Api Response To File Or Print To Screen.
        :param h: Transaction Hash
        :param o: Optional If Specified Prints Output To Screen
        :param n: Optional Network String Defaults To Currently Set Network e.g `btc | btc-testnet`
        """
        if not n:n=self.ds[self.nw]
        txd=self.btc_hash(h,n)
        if o:
            main.clear_screen()
            main.get_menu('\n\033[1;32;40m[*]TRANSACTION HASH INFO:\n\033[1;34;40m'+json.dumps(txd, indent=2, sort_keys=True, default=str))
        else:
            with open(main.txr, 'a', encoding='utf-8') as fw:
                fw.write(f'\nBTC {self.nw.upper()}:\n\n'+json.dumps(txd, indent=4, sort_keys=True, default=str)+'\n'+'-'*164)
    
    def broadcast_sub(self):
        """Loads Menu To Broadcast Signed Transaction."""
        while True:
            try:
                main.clear_screen()
                bc=input(f'\033[1;32;40m{docs.bbs}{main.ns.format(self.nw)}\n\033[0mInput Choice=> ')
                if bc=='b':break
                elif bc=='n':self.get_network()
                elif bc=='e':main.pexit()
                elif bc:
                    l=[]
                    if len(bc)>200:l=[bc]
                    else:
                        with open(main.btx, 'r') as r:
                            if bc=='a':l=re.findall('\d+=(.*)',r.read())
                            elif str(bc).isdigit():l=[re.search(f'{bc}=(.*)',r.read()).group(1)]
                    if l:
                        hl=self.broadcast_iter(l)
                        if hl:main.get_menu(hl)
            except:main.get_menu('e')
    
    def broadcast_iter(self, l: list) -> str:
        """
        Broadcast Transactions In List & Return Calculated Tx Hash As String.
        :param l: List Containing Hex Coded Transactions
        """
        hl=''
        for i in l:
            try:
                b=self.broadcast_tx(i, n=self.nw[0])
                if 'Error' in b:hl+=b
                else:
                    hl+=main.hs.format(b)
                    sleep(5)
                    self.tx_hash(b)
            except:pass
        return hl
    
    def broadcast_tx(self, h: str, n: str='m') -> str:
        """
        Returns Transaction Hash Of Broadcasted Transaction Or Raised Exception.
        :param d: Transaction Hex
        :param n: Blockchain Network As String e.g 'nile'
        """
        try:
            if n.lower()=='m':NetworkAPI.broadcast_tx(h)
            elif n.lower()=='t':NetworkAPI.broadcast_tx_testnet(h)
            return calc_txid(h)
        except Exception as e:
            b=f'\033[1;31;40mError {e}'
            return b
    
    def bit_authenticate(self):
        """Loads Menu To Return BIt Instance From Private Key/Mnemonic/Entropy/Wif/File."""
        bp=wallet.wauth(self.bb[self.nw])
        if bp:return self.bit_pkey(bp.private_key(), nw=self.nw[0])
    
    def bit_nkey(self, nw: str='m'):
        """
        Returns Bit Instance With Generated Private Key.
        :param nw: Network e.g `m = Mainnet | T= Testnet`
        """
        if nw.lower()=='m':return Key()
        elif nw.lower()=='t':return PrivateKeyTestnet()
    
    def bit_pkey(self, pk: str, nw: str='m'):
        """
        Returns Bit Instance From Private Key.
        :param pk: Private Key
        :param nw: Network e.g `m = Mainnet | T= Testnet`
        """
        if nw.lower()=='m':return Key.from_hex(pk)
        elif nw.lower()=='t':return PrivateKeyTestnet.from_hex(pk)
    
    def btc_all(self, bk, adr: str) -> str:
        """
        Returns BTC Transaction Hash For Transferral Of All BTC In Account To Address.
        :param bk:  Bit Instance
        :param adr: Address To Transfer To
        """
        return bk.send([], leftover=adr)
    
    def btc_tx(self, bk, adr: str, amt: str, cur: str) -> str:
        """
        Returns BTC Transaction Hash For Normal Transaction.
        :param bk:  Bit Instance From Private Key
        :param adr: Address To Transfer To
        :param amt: Amount To Transfer
        :param cur: Currency Of Specified Amount To Transfer 
        """
        return bk.send([(adr, amt, cur)])
    
    def btc_prep_all(self, bk, adr: str) -> str:
        """
        Returns Unsigned BTC Transaction Dictionary As String For Transferral Of All BTC In Account To Address.
        :param bk:  Bit Instance
        :param adr: Address To Transfer To
        """
        return bk.prepare_transaction([], leftover=adr)
    
    def btc_prep_tx(self, bk, own: str, adr: str, amt: str, cur: str) -> str:
        """
        Returns Unsigned BTC Transaction Dictionary As String For The Transaction.
        :param bk:  Bit Instance From Private Key
        :param own: Owner Address To Transfer From
        :param adr: Deposit Address To Transfer To
        :param amt: Amount To Transfer
        :param cur: Currency Of Specified Amount To Transfer 
        """
        return bk.prepare_transaction(own, [(adr, amt, cur)])
    
    def btc_hash(self, h: str, s: str) -> dict:
        """
        Returns Transaction Hash Api Response As Json Dictionary.
        :param h: Transaction Hash
        :param s: Symbol Of Transaction Hash Token
        """
        return get_transaction_details(h, s)
    
    def token_bal(self, a: str, s: str='btc') -> str:
        """
        Returns Balance Of BTC Address As String.
        :param a: BTC Address To Get Balance
        :param s: Symbol Of Token Defaults To btc e.g `btc-testnet`
        """
        o=int(get_address_overview(a,s)['balance'])
        return from_base_unit(o,'btc')
    
    def menu(self):
        """Loads Btc-Chain Menu."""
        while True:
            try:
                main.clear_screen()
                main.slow_print(__doc__+docs.cm, sp=0.0001)
                mc=input("\033[0m\nInput Choice=> ")
                if mc=='b':break
                elif mc=='1':self.get_balance()
                elif mc=='2':self.transfer_btc()
                elif mc=='3':self.balance_fkey()
                elif mc=='4':self.tx_sub()
                elif mc=='d':main.decode_bsf()
                elif mc=='e':main.pexit()
                elif mc=='p':main.crypto_price()
                elif mc=='s':self.broadcast_sub()
            except:pass

def cli_main():
    """Btc-Chain Entry Point Launches Btc-Chain CLI Menu."""
    btm=Btc()
    btm.menu()
    main.clear_screen()
