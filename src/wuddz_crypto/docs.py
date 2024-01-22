"""MODULE CONTAINING ALL WUDDZ_CRYPTO MENU BANNERS AS VARIABLES"""

mm="""
 [*]Menu:                                                                                               
    1    =>    Btc-Chain                                                                                
    2    =>    Trx-Chain                                                                                
    l    =>    Save Crypto Wallet Account Token(s) Info From Mnemonic, Entropy, Private Key Or Wif      
    w    =>    Create Multi-Account & Multi-Address Crypto Wallet                                       
    d    =>    Decode Base64 String                                                                     
    p    =>    Crypto Price & Conversion                                                                
    e    =>    Exit Program                                                                             
"""

cm="""
 [*]Menu:                                                                                            
    1    =>    Check Address Balance                                                                 
    2    =>    Send/Deposit To An Address                                                            
    3    =>    Get Address & Balance(s) From Mnemonic, Entropy, Private Key Or Wif                   
    4    =>    Get Transaction Hash Attributes                                                       
    s    =>    Broadcast Signed Transaction To Blockchain                                            
    d    =>    Decode Base64 String                                                                  
    p    =>    Crypto Price & Conversion                                                             
    b    =>    Back To Main Menu                                                                     
    e    =>    Exit Program                                                                          
"""

bc=""" [*]APPROVE, SIGN & BROADCAST OR SAVE SIGNED TRANSACTION:
    
    y1  =>  Approve, Sign Online & Broadcast Immediately (Default).
    y2  =>  Approve, Sign Offline Or Online & Write Signed Transaction To Output File "broadcast_tx.txt",
            Prefixed With Index(e.g 1=), To Broadcast Before Expiration.
    n   =>  No Transaction
    """

ds=""" [*]DECODE BASE64 STRING:
    
    string    =>    Base64 String Output Is UTF-8 Decoded String
    b         =>    Back To Previous Screen
    e         =>    Exit Program
    """

cp=""" [*]CRYPTO PRICE & CONVERSION:                                   
                                                                 
    Amount    =  1.2 | 5 | 1004                                  
    TokenName =  Ethereum | bitcoin | binancecoin                
                                                                 
    Formats:                                                     
    Amount TokenName                                             
    Amount From(TokenName) To(TokenName)                         
                                                                 
    Examples:                                                    
    1.2 ethereum               Price Of 1.2 Ethereum In USD
    100 binancecoin bitcoin    Bitcoin Value Of 100 BNB    
                                                                 
    Format  =>  To Get Required Price/Value                
    s       =>  Search For Id Of Token                     
    b       =>  Back To Previous Screen
    e       =>  Exit Program
    """

st=""" [*]SEARCH FOR TOKEN & COPY TOKENID TO USE FOR PRICE & CONVERSION:                                                            
                                                                                                                              
    String = Name Of Token (Outputs List Matching String => "Id: TokenId,  Name: TokenName, Symbol: TokenSymbol" On Each Line)
                                                                                                                              
    String  =>  [e.g bitcoin Outputs List Matching "bitcoin" => "Id: bitcoin  Name: bitcoin Symbol: BTC "]              
    b       =>  Back To Previous Screen
    e       =>  Exit Program
    """

lw="""{}
    Languages:
    1 = English (Default)    2 = Spanish    3 = French                4 = Italian
    5 = Japanese             6 = Korean     7 = Chinese Simplified    8 = Chinese Traditional
    
    {}
    ak key       (ath) =>  [key = Private Key Of Wallet]
    aw wif       (ath) =>  [wif = Wif Of Wallet]
    ae ent       (ath) =>  [ent = Entropy Of Wallet]
    am mne       (ath) =>  [mne = Mnemonic String Of Wallet]
    ap pwd       (ath) =>  [pwd = Password Of Encrypted Wallet Data To Retrieve From File]
    
    """

lwa="""{}
    l Language   (lan) =>  [e.g l 2 = Wallet Mnemonic Language To Spanish Or Default To `english`]
    p Passphrase (pwd) =>  [e.g p meherett = Passphrase Of Wallet `meherett`]
    c Account    (aci) =>  [e.g c 0 (default) | 1 = Wallet Account Index
    r Address    (adi) =>  [e.g r 0 (default) | 1 = Wallet Address Index
    h                  =>  Reset Current Arguments To Default                           
    x                  =>  Execute Current Arguments                            
    b                  =>  Back To Previous Screen                          
    e                  =>  Exit Program 
    """

lwl="""Optional:
    d (enc = False)    =>  Decrypt Wallet Data Output                     
    t (enc = True)     =>  Encrypt Wallet Data Output"""

lwb=""" [*]LOAD & SAVE SPECIFIED TOKEN WALLET INFO (ENCRYPTED/DECRYPTED) TO OUTPUT FILE:
    
"""

lwc=""" [*]WALLET AUTHENTICATION:
"""

lwd="""Required:
    s Symbol     (sym) =>  Formats: (e.g s sym = Save Wallet Info For Symbol Token)
                                    (e.g s sym,sym = Save Wallet Info For Both Symbol Tokens)"""

lwe="""Required:"""

cw=""" [*]CREATE CRYPTO WALLET WITH CHOSEN TOKEN(S):

{}
    Languages:
    1 = English (Default)    2 = Spanish    3 = French                4 = Italian
    5 = Japanese             6 = Korean     7 = Chinese Simplified    8 = Chinese Traditional
    
    Mnemonic String Length (Strength):
    12 = 128 (Default)    15 = 160    18 = 192    21 = 224    24 = 256
    
    Required:
    s Symbol     (sym) =>  Formats:  (s sym = Creates 1 Address)
                                     (s sym-2 (max is 20) = Creates 2 Addresses Indexed 0 & 1)
                           Examples: [s btc-3,eth-2 = Creates Wallet Account Containing 3 Bitcoin & 2 Ethereum Addresses]
                                     [s ltc,eth = Creates Wallet Account Containing 1 Litecoin & 1 Ethereum Address]
                                     [s btc = Creates Wallet Account Containing 1 Bitcoin Address]
    
    Optional:
    m Strength   (stn) =>  [e.g m 15 = Create Wallet With 15 Word Mnemonic or Default Used]                
    l Language   (lan) =>  [e.g l 2 = Set Mnemonic Language To Spanish Or Default Used]
    p Passphrase (pwd) =>  [e.g p meherett = Sets Passphrase (i.e Of A Created Wallet) Or 32 Character Passphrase Generated]
    a Auth       (ath) =>  [e.g a Entropy/Mnemonic String Of A Created Wallet = Creates A Multi Crypto Wallet Or Skip]    
    c Account    (aci) =>  [e.g c 0 (default) | 1 = Wallet Account Index (To Create Multi Account Wallet)]    
    r Address    (adi) =>  [e.g r 0 (default) | 1 = Wallet Address Index (To Create Multiple Addresses For A Token In Wallet)]    
    d (enc = False)    =>  Decrypt Wallet Data Output                     
    t (enc = True)     =>  Encrypt Wallet Data Output         
    h                  =>  Reset Current Arguments To Default                           
    x                  =>  Execute Current Arguments                            
    b                  =>  Back To Previous Screen                          
    e                  =>  Exit Program                          
"""

bns=""" [*]CHOOSE BTC NETWORK:
        
    1  =>  Mainnet (Default)
    2  =>  Testnet
    """

tns=""" [*]CHOOSE TRON NETWORK:
        
    1 = Mainnet  
    2 = Nile (Testnet)  
    3 = Shasta (Testnet)  
    4 = Tronex (Testnet)
    5 = Input Private Node Url [e.g http://127.0.0.1:8090]
    """

bd=""" [*]GET ADDRESS BALANCE:
    
    Address  =>  Address To Get Balance For Current Network
    n        =>  Choose Network
    b        =>  Back To Previous Screen
    e        =>  Exit Program
    """

bsb=""" [*]SEND/DEPOSIT BTC AMOUNT TO SPECIFIED ADDRESS (TRANSFERS TO BECH32 NOT FROM BECH32 ADDRESSES):
    
    Bech32 Address e.g `bc1qf9kaqdqe9z2suatg3vn7zwe9nxlpvt4sskeji7`
    
    Currencies:
{}  
    Formats:
    Owner Deposit Amount Currency  Transfer Specified Amount Of Currency From Owner To Deposit Address
    Owner Deposit                  Transfer All BTC From Owner To Deposit Address
    
    Examples:
    18UNHQ2af7LRKm1bv24hRncC31EzB16Sfv 15Ry7usBQHno3Po1GvRzo8eVvsrFCDwJYv 10 usd
    [Transfer 10 usd From Owner To Deposit Address]
    
    18UNHQ2af7LRKm1bv24hRncC31EzB16Sfv bc1qf9kaqdqe9z2suatg3vn7zwe9nxlpvt4sskeji7 100 usd
    [Transfer 100 usd From Owner To Deposit Address (Bech32)]
    
    18UNHQ2af7LRKm1bv24hRncC31EzB16Sfv 15Ry7usBQHno3Po1GvRzo8eVvsrFCDwJYv
    [Transfer All BTC From Owner To Deposit Address]
    
    Owner     =>  Owner Address To Transfer BTC From [e.g 18UNHQ2af7LRKm1bv24hRncC31EzB16Sfv]
    Deposit   =>  Deposit Address To Transfer BTC To [e.g 15Ry7usBQHno3Po1GvRzo8eVvsrFCDwJYv]
    Amount    =>  Amount Of Specified Currency To Transfer [e.g 0.012 | 100]
    Currency  =>  Currency To Tranfer Specified Amount Of BTC [e.g btc | usd]
    n         =>  Choose Network
    b         =>  Back To Previous Screen
    e         =>  Exit Program
    """

tsb=""" [*]SEND/DEPOSIT CHOSEN TRC-20 TOKEN & AMOUNT TO ADDRESS:
    
    Mainnet Tokens:
    1 = USDT (Tether USD)        6 = WTRX (Wrapped TRX)          11 = USDJ (JUST Stablecoin)     16 = WIN (WINkLink)
    2 = TRON (TRX)               7 = USDD (Decentralized USD)    12 = JST (JUST)                 17 = HT (HuobiToken)
    3 = BTC (Bitcoin)            8 = USDC (USD Coin)             13 = SUNOLD (SUNOLD)            18 = ETH (Ethereum)
    4 = TUSD (TrueUSD)           9 = BTT (BitTorrent)            14 = SUN (SUN)                  19 = ETHOLD (EthereumOLD)
    5 = stUSDT (Staked USDT)    10 = NFT (APENFT)                15 = BTTOLD (BitTorrent Old)    20 = DOGE (Dogecoin)
    
    Testnet Tokens:
    21 = USDT (Shasta Testnet)  22 = USDT (Nile Testnet)
    
    Formats:
    ca = Contract Address/Token Id [e.g TN3W4H6rK2ce4vX9YnFQHwKENnHjoxb3m9 | 1002000]
    ad = Owner Address | Deposit Address [e.g TKDWFx7JhsPFtByHLm1eSs8FRhKbN5BFg3]
    tk = Amount Of Token To Transfer [e.g 100]
    
    t 1  (tkn)  =>  Mainnet/Testnet Token Selection Value Above e.g 1 = Transfer USDT
    t ca (tok)  =>  Transfer Specified Contract Address Or TokenID Token
    p 18 (dec)  =>  18 Decimal Precision For Chosen Token
    o ad (own)  =>  Owner Address
    d ad (dpa)  =>  Deposit Address
    a tk (amt)  =>  Transfer Amount (Will Be Converted Using Token Decimal Precision)
    s           =>  Search For Token Name & Retrieve Token ID
    x           =>  Execute Transaction With Arguments Specified
    n           =>  Choose Network
    b           =>  Back To Previous Screen
    e           =>  Exit Program
    """

tst=""" [*]SEARCH FOR TOKEN:
        
    token name  =>  [e.g BitTorrent Old = Searches & Retrieves Token Info]
    token id    =>  [e.g 1002000 = Searches & Retrieves Token Info]
    b           =>  Back To Previous Screen
    e           =>  Exit Program
    """

ts=""" [*]GET TRANSACTION HASH INFO:
        
    hash   =>   Print Transaction Hash Info
    n      =>   Choose Network
    b      =>   Back To Previous Screen
    e      =>   Exit Program
    """
    
bbs=""" [*]BROADCAST SIGNED TRANSACTION HEX TO BLOCKCHAIN:
    
    Hex    =>  Signed Transaction Hex To Broadcast
    Index  =>  Prefixed Number Of Transaction In File "broadcast_tx.txt" To Broadcast e.g 0 | 1
    a      =>  Broadcast All Transactions In File (broadcast_tx.txt) e.g a
    n      =>  Choose Network
    b      =>  Back To Previous Screen
    e      =>  Exit Program
    """

tbs=""" [*]BROADCAST SIGNED TRANSACTION DICTIONARY TO BLOCKCHAIN:
    
    Dictionary  =>  Signed Transaction Dictionary To Broadcast e.g {transaction dictionary}
    Index       =>  Prefixed Number Of Transaction In File "broadcast_tx.txt" To Broadcast e.g 0 | 1
    a           =>  Broadcast All Transactions In File (broadcast_tx.txt) e.g a
    n           =>  Choose Network
    b           =>  Back To Previous Screen
    e           =>  Exit Program
    """
