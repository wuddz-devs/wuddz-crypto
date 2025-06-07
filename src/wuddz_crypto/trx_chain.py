"""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░████████╗██████╗░██╗░░██╗░░░░░░░█████╗░██╗░░██╗░█████╗░██╗███╗░░██╗░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░╚══██╔══╝██╔══██╗╚██╗██╔╝░░░░░░██╔══██╗██║░░██║██╔══██╗██║████╗░██║░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░██║░░░██████╔╝░╚███╔╝░█████╗██║░░╚═╝███████║███████║██║██╔██╗██║░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░██║░░░██╔══██╗░██╔██╗░╚════╝██║░░██╗██╔══██║██╔══██║██║██║╚████║░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░██║░░░██║░░██║██╔╝╚██╗░░░░░░╚█████╔╝██║░░██║██║░░██║██║██║░╚███║░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░░░░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

 [*]Descr:     INTERACT WITH TRON MAINNET & TESTNET BLOCKCHAINS TO MAKE TRANSACTIONS & CHECK BALANCES
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
from tronpy import Tron
from tronpy.keys import PrivateKey
from tronpy.tron import Transaction
from tronpy.providers import HTTPProvider
from getpass import getpass
from os import system
system('')


class Trx:
    def __init__(self):
        """Connect & Interact Wtih Tronics Mainnet/Testnet Blockchains."""
        self.client=Tron()
        self.nw='mainnet'
        self.tx='https://apilist.tronscanapi.com/api/transaction-info?hash={}'
        self.ba='https://apilist.tronscanapi.com/api/account/token_asset_overview?address={}'
        self.cn='https://apilist.tronscanapi.com/api/contract?contract={}'
        self.na='https://apilist.tronscanapi.com/api/token?name={}'
        self.ti='https://apilist.tronscanapi.com/api/token?id={}'
        self.cd={
                 '1': {'cnt': 'TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t', 'dec': 6, 'name': 'USDT (Tether USD)'},
                 '2': {'cnt': '', 'dec': 6, 'name': 'TRON (TRX)'},
                 '3': {'cnt': 'TN3W4H6rK2ce4vX9YnFQHwKENnHjoxb3m9', 'dec': 8, 'name': 'BTC (Bitcoin)'},
                 '4': {'cnt': 'TUpMhErZL2fhh4sVNULAbNKLokS4GjC1F4', 'dec': 18, 'name': 'TUSD (TrueUSD)'},
                 '5': {'cnt': 'TThzxNRLrW2Brp9DcTQU8i4Wd9udCWEdZ3', 'dec': 18, 'name': 'stUSDT (Staked USDT)'},
                 '6': {'cnt': 'TNUC9Qb1rRpS5CbWLmNMxXBjyFoydXjWFR', 'dec': 6, 'name': 'WTRX (Wrapped TRX)'},
                 '7': {'cnt': 'TPYmHEhy5n8TCEfYGqW2rPxsghSfzghPDn', 'dec': 18, 'name': 'USDD (Decentralized USD)'},
                 '8': {'cnt': 'TEkxiTehnzSmSe2XqrBj4w32RUN966rdz8', 'dec': 6, 'name': 'USDC (USD Coin)'},
                 '9': {'cnt': 'TAFjULxiVgT4qWk6UZwjqwZXTSaGaqnVp4', 'dec': 18, 'name': 'BTT (BitTorrent)'},
                 '10': {'cnt': 'TFczxzPhnThNSqr5by8tvxsdCFRRz6cPNq', 'dec': 6, 'name': 'NFT (APENFT)'},
                 '11': {'cnt': 'TMwFHYXLJaRUPeW6421aqXL4ZEzPRFGkGT', 'dec': 18, 'name': 'USDJ (JUST Stablecoin)'},
                 '12': {'cnt': 'TCFLL5dx5ZJdKnWuesXxi1VPwjLVmWZZy9', 'dec': 18, 'name': 'JST (JUST)'},
                 '13': {'cnt': 'TKkeiboTkxXKJpbmVFbv4a8ov5rAfRDMf9', 'dec': 18, 'name': 'SUNOLD (SUNOLD)'},
                 '14': {'cnt': 'TSSMHYeV2uE9qYH95DqyoCuNCzEL1NvU3S', 'dec': 18, 'name': 'SUN (SUN)'},
                 '15': {'cnt': '1002000', 'dec': 6, 'name': 'BTTOLD (BitTorrent Old)'},
                 '16': {'cnt': 'TLa2f6VPqDgRE67v1736s7bJ8Ray5wYjU7', 'dec': 6, 'name': 'WIN (WINkLink)'},
                 '17': {'cnt': 'TDyvndWuvX5xTBwHPYJi7J3Yq8pq8yh62h', 'dec': 18, 'name': 'HT (HuobiToken)'},
                 '18': {'cnt': 'TRFe3hT5oYhjSZ6f3ji5FJ7YCfrkWnHRvh', 'dec': 18, 'name': 'ETH (Ethereum)'},
                 '19': {'cnt': 'THb4CqiFdwNHsWsQCs4JhzwjMWys4aqCbF', 'dec': 18, 'name': 'ETHOLD (EthereumOLD)'},
                 '20': {'cnt': 'THbVQp8kMjStKNnf2iCY6NEzThKMK5aBHg', 'dec': 8, 'name': 'DOGE (Dogecoin)'},
                 '21': {'cnt': 'TG3XXyExBkPp9nzdajDZsozEu4BkaSJozs', 'dec': 6, 'name': 'USDT (Shasta Testnet)'},
                 '22': {'cnt': 'TXLAQ63Xg1NAzckPwKHvzw7CSEmLMEqcdj', 'dec': 6, 'name': 'USDT (Nile Testnet)'}
                }
    
    def get_network(self):
        """Loads Menu To Choose Tron Network."""
        main.clear_screen()
        nd={'1': 'mainnet', '2': 'nile', '3': 'shasta', '4': 'tronex'}
        nc=input(f'\033[1;32;40m{docs.tns}\n\033[0mInput Network Choice=> ') or '1'
        if nc=='5':
            main.clear_screen()
            nu=input('Input Private Node Url=> ') or None
            self.nw=f'private {nu}'
            self.client=Tron(HTTPProvider(nu))
        elif nd.get(nc):
            self.nw=nd[nc]
            self.client=Tron(network=self.nw)
    
    def get_balance(self):
        """Loads Menu To Get Address Balance(s)."""
        while True:
            try:
                main.clear_screen()
                ba=input(f'\033[1;32;40m{docs.bd}{main.ns.format(self.nw)}\n\033[0mInput Address=> ') or None
                if ba=='b':break
                elif ba=='e':main.pexit()
                elif ba=='n':self.get_network()
                elif ba:
                    if self.nw=='mainnet':self.balance_sub(main.js_resp(self.ba.format(ba)))
                    else:self.balance_trx(ba)
            except:main.get_menu('e')
    
    def transfer_trc(self):
        """Loads Menu To Transfer/Deposit TRC10/TRC20."""
        ad={'t ': 'tok', 'p ': 'dec', 'd ': 'dpa', 'a ': 'amt', 'o ': 'own'}
        od={'tok': '', 'dec': 6, 'own': None, 'dpa': None, 'amt': None, 'tkn': 'TRON (TRX)'}
        vd={'tok': '', 'dec': 6, 'own': None, 'dpa': None, 'amt': None, 'tkn': 'TRON (TRX)'}
        while True:
            try:
                main.clear_screen()
                ast=docs.tsb+main.ns.format(self.nw)
                arg=input('\033[1;32;40m'+ast+'\033[1;34;40m\n'+' '*4+'Current Arguments:\n'+' '*4+str(vd)+'\n\033[0m\nInput Argument=> ')
                if arg=='b':break
                elif arg=='e':main.pexit()
                elif arg=='s':self.search_token()
                elif arg=='n':self.get_network()
                elif ad.get(arg[:2]):
                    k=arg[:2]
                    v=arg[2:]
                    if ad.get(k)=='tok':
                        if self.cd.get(v):
                            vd.update({'tok': self.cd[v]['cnt'], 'dec': self.cd[v]['dec'], 'tkn': self.cd[v]['name']})
                        elif self.client.is_base58check_address(v) and self.nw=='mainnet':
                            cnd=main.js_resp(self.cn.format(v))['data'][0]['tokenInfo']
                            tkn=str(cnd['tokenAbbr'])+' ('+str(cnd['tokenName'])+')'
                            vd.update({'tok': v, 'dec': int(cnd['tokenDecimal']), 'tkn': tkn})
                        else:
                            tki=self.client.get_asset(int(v))
                            tkn=str(tki['abbr'])+' ('+str(tki['name'])+')'
                            vd.update({'tok': tki['id'], 'dec': int(tki['precision']), 'tkn': tkn})
                    else:vd[ad.get(k)]=v
                elif arg=='x':
                    self.transfer_sub(vd)
                    vd.clear()
                    vd.update(od)
            except:
                vd.clear()
                vd.update(od)
                main.get_menu('e')
    
    def search_token(self):
        """Search For Token Information By Name Or Token Id."""
        while True:
            try:
                main.clear_screen()
                st=input(f'\033[1;32;40m{docs.tst}\n\033[0mInput Token Name/Id=> ') or None
                if st=='b':break
                elif st=='e':main.pexit()
                elif st.isdigit():res=main.js_resp(self.ti.format(st))['data'][0]
                elif st:res=main.js_resp(self.na.format(st))['data'][0]
                if type(res) is dict:
                    s=f'\n\033[1;34;40mAbbr: {res["abbr"]}\nName: {res["name"]}\nDecimal: {res["precision"]}\nId: {res["tokenID"]}'
                    main.get_menu(s)
                elif res:raise ValueError
            except:main.get_menu('e')
    
    def transfer_sub(self, td: dict):
        """
        Verify Execution & Specify Transaction Signing On Or Offline.
        :param td: Dictionary Containing Transaction Arguments
        """
        main.clear_screen()
        ts=main.vs.format(td['amt'], td['tkn'], td['own'], td['dpa'])
        et=input(f'\033[1;32;40m{docs.bc}\n\033[1;34;40mCurrent Network: {self.nw}'+ts) or 'n'
        if et in ['y1','y2']:
            try:
                if not self.client.is_base58check_address(td['dpa']):raise ValueError
                amt=int(float(td['amt']) * 10 ** int(td['dec']))
                txn=self.build_trx(td['own'], td['dpa'], amt, tok=td['tok']) # Build Transaction Internet Connection Required
                if txn is None:raise ValueError
                if et=='y2':
                    main.get_menu('\n\033[1;34;40mDisconnect Internet Connection Now To Sign Transaction Offline')
                    pk=self.tron_authenticate() # Private Key To Sign Transaction No Internet Connection Required
                    if not pk:return
                    txn.sign(pk) # Sign Transaction With Private Key No Internet Connection Required
                    i=main.bindex()
                    wallet.wdec('{}={}'.format(str(i),json.dumps(txn.to_json())),main.btx)
                    main.get_menu(f'\n\033[1;34;40mTransaction Data Index {i} Saved To {main.btx} Successfully')
                else:
                    pk=self.tron_authenticate()
                    if not pk:return
                    txn.sign(pk)
                    tid=txn.txid
                    res=txn.broadcast().wait() # Broadcast Transaction Internet Connection Required
                    self.tx_output(tid, main.txr)
                    main.get_menu(main.ts.format(td['own'],td['dpa'],td['amt'],td['tkn'],tid))
            except:main.get_menu('e')
    
    def build_trx(self, adr: str, dpa: str, amt: int, tok=None):
        """
        Return Transaction Object From Executed Transaction.
        :param adr: Owner Address To Transfer From
        :param dpa: Deposit Address To Transfer To
        :param amt: Integer Amount Of Token To Be Transferred (Using Token Decimal)
        :param tok: Token Name Or Token ID e.g `TUSD (TrueUSD) Or 1002000`
        """
        try:
            if not tok:
                txn=(
                     self.client.trx.transfer(from_=adr, to=dpa, amount=amt)
                       .memo("0")
                       .build()
                    )
            elif str(tok).isdigit():
                txn=(
                     self.client.trx.asset_transfer(from_=adr, to=dpa, amount=amt, token_id=int(tok))
                       .memo("0")
                       .build()
                    )
            elif self.client.is_base58check_address(tok):
                contract=self.client.get_contract(tok)
                txn=(
                     contract.functions.transfer(dpa, amt)
                       .with_owner(adr)
                       .fee_limit(10_000_000)
                       .build()
                    )
            return txn
        except:pass
    
    def tx_output(self, h: str, f: str):
        """
        Write Transaction Info To Output File.
        :param h: Transaction Hash
        :param f: Output Filename
        """
        if self.nw=='mainnet':ti=main.js_resp(self.tx.format(h))
        else:ti=self.client.get_transaction_info(h)
        with open(f, 'a', encoding='utf-8') as fw:
            fw.write('\nTRON {} NETWORK:\n\n'.format(self.nw.upper())+json.dumps(ti, indent=4, sort_keys=True, default=str)+'\n'+'-'*164)
    
    def balance_fkey(self):
        """Print Address & Balance Of Private Key/Entropy/Mnemonic/Wif In BTC & USD."""
        try:
            self.get_network()
            pk=self.tron_authenticate()
            if not pk:return
            ad=pk.public_key.to_base58check_address()
            if self.nw=='mainnet':self.balance_sub(main.js_resp(self.ba.format(ad)))
            else:self.balance_trx(ad)
        except:main.get_menu('e')
    
    def tron_authenticate(self):
        """Loads Menu To Return Private Key From Input Or BIP44HDWallet Instance Using Mnemonic/Entropy/Wif/File."""
        bp=wallet.wauth('TRX')
        if bp:return PrivateKey(bytes.fromhex(bp.private_key()))
    
    def balance_sub(self, jd: dict):
        """
        Format Api Balance Json Response & Print To Screen.
        :param jd: Api Balance Json Response
        """
        try:
            tt="{:.2f}".format(jd['totalAssetInUsd'])
            bd=jd['data']
            for i in range(len(bd)):
                usd="{:.2f}".format(bd[i]['assetInUsd'])
                sym=bd[i]['tokenAbbr']
                dec=int(bd[i]['tokenDecimal'])
                bal=float(bd[i]['balance'])/10**dec
                nam=bd[i]['tokenName']
                typ=bd[i]['tokenType']
                print(f'\n\033[1;34;40m{nam} ({typ}): {bal} {sym} \033[1;32;40m(${usd} USD)')
            main.get_menu(f'\033[1;34;40mTotal Value: \033[1;32;40m${tt} USD')
        except:main.get_menu('e')
    
    def balance_trx(self, ba: str):
        """
        Request Balance From Tronpy Module & Print To Screen.
        :param ba: Address String To Retrieve Balance For
        """
        try:
            b=self.client.get_account_balance(ba)
            main.get_menu(f'\n\033[1;34;40mBalance: {b} TRX')
        except:main.get_menu('e')
    
    def tx_info(self):
        """Loads Menu To Print Transaction Hash Info To Screen."""
        while True:
            try:
                main.clear_screen()
                th=input(f'\033[1;32;40m{docs.ts}{main.ns.format(self.nw)}\n\033[0mInput Hash=> ') or None
                if th=='b':break
                elif th=='e':main.pexit()
                elif th=='n':self.get_network()
                elif th:
                    if self.nw=='mainnet':td=main.js_resp(self.tx.format(th))
                    else:td=self.client.get_transaction_info(th)
                    main.get_menu('\n\033[1;34;40m'+json.dumps(td, indent=4, sort_keys=True, default=str))
            except:main.get_menu('e')
    
    def broadcast_sub(self):
        """Loads Menu To Broadcast Signed Transaction."""
        while True:
            try:
                main.clear_screen()
                bc=input(f'\033[1;32;40m{docs.tbs}{main.ns.format(self.nw)}\n\033[0mInput Choice=> ')
                if bc=='b':break
                elif bc=='n':self.get_network()
                elif bc=='e':main.pexit()
                elif bc:
                    l=[]
                    if len(bc)>700:l=[bc]
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
        Broadcast Transactions In List & Return Tx Hash In String.
        :param l: List Containing Transactions
        """
        hl=''
        for i in l:
            try:
                t=self.broadcast_tx(i, n=self.nw)
                if type(t) is dict:
                    tid=t.get('id')
                    hl+=main.hs.format(tid)
                    self.tx_output(tid, main.txr)
                else:hl+=t
            except:pass
        return hl
    
    def broadcast_tx(self, d: str, n: str='mainnet'):
        """
        Returns Signed Transaction Broadcast Dictionary Output Or Exception.
        :param d: Dictionary As String
        :param n: Blockchain Network As String e.g 'nile'
        """
        try:
            txn=Transaction.from_json(json.loads(d), client=Tron(network=n))
            res=txn.broadcast().wait()
            return res
        except Exception as e:
            b=f'\n\033[1;31;40mError {e}'
            return b
    
    def menu(self):
        """Loads Trx-Chain Menu."""
        while True:
            try:
                main.clear_screen()
                main.slow_print(__doc__+docs.cm,sp=0.0001)
                mc=input("\033[0m\nInput Choice=> ")
                if mc=='b':break
                elif mc=='1':self.get_balance()
                elif mc=='2':self.transfer_trc()
                elif mc=='3':self.balance_fkey()
                elif mc=='4':self.tx_info()
                elif mc=='e':main.pexit()
                elif mc=='d':main.decode_bsf()
                elif mc=='p':main.crypto_price()
                elif mc=='s':self.broadcast_sub()
            except:pass

def cli_main():
    """Trx-Chain Entry Point Launches Trx-Chain CLI Menu."""
    trm=Trx()
    trm.menu()
    main.clear_screen()
