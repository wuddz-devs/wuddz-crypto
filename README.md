<h1 align="center">Wuddz Crypto</h1>

## Description
 - Multi Blockchain Cryptocurrency App, Create HD (Hierarchical Deterministic) Wallet Containing Multiple Tokens From Many     
 - Blockchains, Check Balances, Make Transactions, Get Transaction Hash Data, Get Current Crypto Prices, Get Value Of Token
 - In Other Cryptocurrencies & Decode Base64 String.

## Prerequisites
 - Python : 3.7

## Installation
Install using [PyPI](https://pypi.org/project/wuddz-crypto):
```
$ pip install wuddz-crypto
```
Install locally by cloning or downloading and extracting the repo, then cd into 'dist' directory and execute:
```
$ pip install wuddz_crypto-1.0.1.tar.gz
```
Then to run it, execute the following in the terminal:
```
$ wudz-crypto
```

### Library
Get Current Price Of Bitcoin In USD.
```
>>> from wuddz_crypto import main
>>> main.get_price('bitcoin')
26741
```
Get All Supported Wallet Symbols & Names.
```
>>> from wuddz_crypto import wallet
>>> sym_names=wallet.wsym()
>>> sym_names
{'ANON': 'Anon', 'AGM': 'Argoneum', 'XAX': 'Artax', 'AYA': 'Aryacoin', 'AC': 'Asiacoin', 'ATOM': 'Atom', 'AUR': 'Auroracoin', 'AXE': 'Axe', 'BTA': 'Bata', 'BEET': 'Beetle Coin', 'BELA': 'Bela Coin', 'BTDX': 'Bit Cloud', 'BSD': 'Bit Send', 'BCH': 'Bitcoin Cash', 'BTG': 'Bitcoin Gold', 'BTC': 'Bitcoin', 'BTCTEST': 'Bitcoin', 'XBC': 'Bitcoin Plus', 'BSV': 'Bitcoin SV', 'BTCZ': 'BitcoinZ', 'BTX': 'Bitcore', 'BLK': 'Blackcoin', 'BST': 'Block Stamp', 'BND': 'Blocknode', 'BNDTEST': 'Blocknode', 'BOLI': 'Bolivarcoin', 'BRIT': 'Brit Coin', 'CPU': 'CPU Chain', 'CDN': 'Canada eCoin', 'CCN': 'Cannacoin', 'CLAM': 'Clams', 'CLUB': 'Club Coin', 'CMP': 'Compcoin', 'CRP': 'Crane Pay', 'CRAVE': 'Crave', 'DASH': 'Dash', 'DASHTEST': 'Dash', 'ONION': 'Deep Onion', 'DFC': 'Defcoin', 'DNR': 'Denarius', 'DMD': 'Diamond', 'DGB': 'Digi Byte', 'DGC': 'Digitalcoin', 'DOGE': 'Dogecoin', 'DOGETEST': 'Dogecoin', 'EDRC': 'EDR Coin', 'ECN': 'Ecoin', 'EMC2': 'Einsteinium', 'ELA': 'Elastos', 'NRG': 'Energi', 'ETH': 'Ethereum', 'ERC': 'Europe Coin', 'EXCL': 'Exclusive Coin', 'FIX': 'FIX', 'FIXTEST': 'FIX', 'FLUX': 'Flux', 'FTC': 'Feathercoin', 'FRST': 'Firstcoin', 'FLASH': 'Flashcoin', 'FJC': 'Fuji Coin', 'GCR': 'GCR Coin', 'GAME': 'Game Credits', 'GBX': 'Go Byte', 'GRC': 'Gridcoin', 'GRS': 'Groestl Coin', 'GRSTEST': 'Groestl Coin', 'NLG': 'Gulden', 'HNC': 'Helleniccoin', 'THC': 'Hempcoin', 'HUSH': 'Hush', 'IXC': 'IX Coin', 'INSN': 'Insane Coin', 'IOP': 'Internet Of People', 'JBS': 'Jumbucks', 'KOBO': 'Kobocoin', 'KMD': 'Komodo', 'LBC': 'LBRY Credits', 'LINX': 'Linx', 'LCC': 'Litecoin Cash', 'LTC': 'Litecoin', 'LTCTEST': 'Litecoin', 'LTZ': 'LitecoinZ', 'LKR': 'Lkrcoin', 'LYNX': 'Lynx', 'MZC': 'Mazacoin', 'MEC': 'Megacoin', 'MNX': 'Minexcoin', 'MONA': 'Monacoin', 'MONK': 'Monkey Project', 'XMY': 'Myriadcoin', 'NIX': 'NIX', 'NMC': 'Namecoin', 'NAV': 'Navcoin', 'NEBL': 'Neblio', 'NEOS': 'Neoscoin', 'NRO': 'Neurocoin', 'NYC': 'New York Coin', 'NVC': 'Novacoin', 'NBT': 'NuBits', 'NSR': 'NuShares', 'OK': 'OK Cash', 'OMNI': 'Omni', 'OMNITEST': 'Omni', 'ONX': 'Onix Coin', 'PPC': 'Peercoin', 'PSB': 'Pesobit', 'PHR': 'Phore', 'PINK': 'Pinkcoin', 'PIVX': 'Pivx', 'PIVXTEST': 'Pivx', 'POSW': 'Posw Coin', 'POT': 'Potcoin', 'PRJ': 'Project Coin', 'PUT': 'Putincoin', 'QTUM': 'Qtum', 'QTUMTEST': 'Qtum', 'RBTC': 'RSK', 'RBTCTEST': 'RSK', 'RPD': 'Rapids', 'RVN': 'Ravencoin', 'RDD': 'Reddcoin', 'RBY': 'Rubycoin', 'SAFE': 'Safecoin', 'SLS': 'Saluscoin', 'SCRIBE': 'Scribe', 'SDC': 'Shadow Cash', 'SDCTEST': 'Shadow Cash', 'SLM': 'Slimcoin', 'SLMTEST': 'Slimcoin', 'SMLY': 'Smileycoin', 'SLR': 'Solarcoin', 'STASH': 'Stash', 'STRAT': 'Stratis', 'STRATTEST': 'Stratis', 'SUGAR': 'Sugarchain', 'SUGARTEST': 'Sugarchain', 'SYS': 'Syscoin', 'TOA': 'TOA Coin', 'THT': 'Thought AI', 'TRX': 'Tron', 'TWINS': 'Twins', 'TWINSTEST': 'Twins', 'USC': 'Ultimate Secure Cash', 'UNO': 'Unobtanium', 'VASH': 'Virtual Cash', 'VC': 'Vcash', 'XVG': 'Verge Currency', 'VTC': 'Vertcoin', 'VIA': 'Viacoin', 'VIATEST': 'Viacoin', 'VIVO': 'Vivo', 'XWC': 'Whitecoin', 'WC': 'Wincoin', 'XUEZ': 'XUEZ', 'XDC': 'XinFin', 'YEC': 'Ycash', 'ZCL': 'ZClassic', 'ZEC': 'Zcash', 'ZECTEST': 'Zcash', 'ZEN': 'Zencash'}
```
Create A Bitcoin Testnet Wallet.
```
>>> from wuddz_crypto import wallet
>>> bp=wallet.wobj('BTCTEST')
>>> hd=wallet.wgen(bp)
>>> hd.dumps()
{'cryptocurrency': 'Bitcoin', 'symbol': 'BTCTEST', 'network': 'testnet', 'strength': 128, 'entropy': '658830d2645976e29e10c4bf99d51866', 'mnemonic': 'grain dose cruel silly number image joke blush sauce solid ecology soccer', 'language': 'english', 'passphrase': None, 'seed': '73149ba9e37fe0bf56a66c903a81679cd5c19e6703f56831f95649ce61e5703bce6d8fb20951977186464ed82e2a55423ec040b1ea61764c48e702e9049a44a5', 'root_xprivate_key': 'tprv8ZgxMBicQKsPeAFJU9N9J7PtmqtJdnAMq3zqu35vd6RvKBiFUMAyVTdCoZZ7CWaDoBWyUiADa45YH8hVNxpKobziUSHceKhazDhdARKd1oj', 'root_xpublic_key': 'tpubD6NzVbkrYhZ4XdH6Mo2jhX41LsQEo7MGQMbdBZ8E3NEK9fy26jzZfxF4ygPahkPknSfycugb5z6wHQZEXRu6qfh8evf3KugtgMBWqu5SUnj', 'xprivate_key': 'tprv8kTUVCuEeZKdWqxJ9f1fZrNHrPWeegSeP4pa2FYpBZC2gVQrMavM6xF8fuYiwo5imRe8jFjoMEMNd4ND2qZTC2EUCDbweZBN3JB2HJyYzix', 'xpublic_key': 'tpubDH9WdcwUnw1JQJz63JgFyG2QRR2ap1dYxNRMJmb7bpzRWyfcyyjwHSrzqzccEUJLYcA43CuVDDehMkAknqayWeKcsduoQ3b48KLaBhVKXiK', 'uncompressed': '01f30e8e3ae610a793b5db612a7cbcffb60fa1c975818738b9f12d2b52c6e0c3e2ed3d037dc80f7d22b85ded7bf1e0e067f84f8d67f6ab335c34852fdfe030ca', 'compressed': '0201f30e8e3ae610a793b5db612a7cbcffb60fa1c975818738b9f12d2b52c6e0c3', 'chain_code': 'b19becd6485399d7ef74251af55a00529f4baa232e7e21777087daca3c52e3c8', 'private_key': 'f97941ea760e264b0a13c0292c9c7caa8667f24491280801b9627d0085ba8c8c', 'public_key': '0201f30e8e3ae610a793b5db612a7cbcffb60fa1c975818738b9f12d2b52c6e0c3', 'wif': 'cVweQriigSrewNBp1eP7x1dvPBDQhJBfSbEoAvoawehqsH1AEhJh', 'finger_print': 'b0c9a1a4', 'semantic': 'p2pkh', 'path': "m/44'/1'/0'/0/0", 'hash': 'b0c9a1a4eba9ba0f82d1379c64c9ca1fe88599ad', 'addresses': {'p2pkh': 'mwdimQuh44DCoDXD76Q6Ju36iVvHfqhwZJ', 'p2sh': '2Mz59nFMJQUqyGWWXW9QSCdWiWeKgbBacYe', 'p2wpkh': 'tb1qkry6rf8t4xaqlqk3x7wxfjw2rl5gtxddck5rem', 'p2wpkh_in_p2sh': '2MsKNqnu9RPeDVtwmLMWB4EhvEoqkSShjjD', 'p2wsh': 'tb1qs3qxaq3j7u8u3f9lqeynywjuyllztw05ymazdxu2rgwvwxesx3js3u662a', 'p2wsh_in_p2sh': '2NCWJpLG2gTZnyr7oUrqz3XMHQQdHDX9PLu'}}
```
Transfer 5000 Satoshi On BTC Testnet.
```
>>> from wuddz_crypto import btc_chain as bc
>>> bm=bc.Btc()
>>> bk=bm.bit_pkey('f97941ea760e264b0a13c0292c9c7caa8667f24491280801b9627d0085ba8c8c', 't')
>>> hash=bm.btc_tx(bk, 'mfjypqRp95QKHxDUYg5QqcqcTucWWGohJD', '5000', 'satoshi')
>>> hash
'650df5a8ae9be7c6084f806d3bf1370f4701405c4ff359e15eae0eaa94e87158'
https://blockstream.info/testnet/tx/650df5a8ae9be7c6084f806d3bf1370f4701405c4ff359e15eae0eaa94e87158
```

## Contact Info:
 - Email:     wuddz_devs@protonmail.com                                                              
 - Github:    https://github.com/wuddz-devs                                                          
 - Telegram:  https://t.me/wuddz_devs
 - Youtube:   https://youtube.com/@wuddz-devs
 - Reddit:    https://reddit.com/user/wuddz-devs

### Support Would Be Humbly & Gratefully Appreciated.
 
 - BTC_______bc1qa7ssx0e4l6lytqawrnceu6hf5990x4r2uwuead
 - ERC20_____0xbF4d5309Bc633d95B6a8fe60E6AF490F11ed2Dd1
 - LTC_______LdbcFiQVUMTfc9eJdc5Gw2nZgyo6WjKCj7
 - DOGE______DFwLwtcam7n2JreSpq1r2rtkA48Vos5Hgm
 - TRC10/20__TY6e3dWGpqyn2wUgnA5q63c88PJzfDmQAD

#### Peace & Love Always!!
