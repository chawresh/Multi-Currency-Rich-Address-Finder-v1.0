 Multi Currency Rich Address Finder v1.0 OFFLINE  and  Multi-Currency Rich Address Scanner v1.0 

 
THE FASTEST WALLET CHECKER


NOT:

ADD YOUR RICH ADDRESSES INTO THE newaddresses.txt FILE. IT WILL CREATE THE DATABASE BY ITSELF 

RICH ADDRESSES DOWNLOAD LINK https://github.com/Pymmdrza/Rich-Address-Wallet


Developed by Mustafa AKBAL 



              AUTHOR : Mustafa AKBAL e-mail: mstf.akbal@gmail.com 
              Telegram: @chawresho   Instagram: mstf.akbal
               ================= DONATE ADDRESSES ========================
              BTC p2pkh                : 191QB72rS77vP8NC1EC11wWqKtkfbm5SM8
              BTC p2wpkh               : bc1q2l29nc6puvuk0rn449wf6l8rm62wuxst7uvjeu
              BTC p2wpkh_in_p2sh       : 3AkjfoQn494K5FBdqMrnQRr4UsWji7Az62
              BTC p2wsh_in_p2sh        : 3Cf3J2jw4xx8DVuwHDiQuVrsRoroUgzd7M
              BTC p2sh                 : 3LPo8JHFdXZxvyZDQiWxiWCvPYU4oUhyHz
              BTC p2wsh                : bc1q47rduwq76v4fteqvxm8p9axq39nq25kurgwlyaefmyqz3nhyc8rscuhwwq
              ETH/BSC/AVAX/POLYGON     : 0x279f020A74BfE5Ba6a539B0f523D491A4122d18D
              TRX                      : TDahqcDTkM2qnfoCPfed1YhcB5Eocc2Cwe
              DOGE                     : DD9ViMyVjX2Cv8YnjpBZZhgSD2Uy1NQVbk
              DASH dash_p2pkh          : XihF1MgkPpLWY4xms7WDsUCdAELMiBXCFZ
              ZEC zec_p2pkh            : t1Rt1BSSzQRuWymR5wf189kckaYwkSSQAb1
              LTC ltc_p2pkh            : LTEMSKLgWmMydw4MBNBJHxabY77wp1zyZ6
              LTC ltc_p2sh             : MSbwSBhDaeRPjUq7WbWJY9TKiF4WpZbBd8

Legal Disclaimer and Warning:
- Strict prohibition on illegal activities.
- User responsibility for compliance with laws.
- Intended for legal and ethical use only.
- Consequences of unlawful use.

Features:
1. Key Generation:
   - Generates random private keys and addresses for various cryptocurrencies (BTC, ETH, BNB, AVAX, MATIC, TRX, DOGE, BCH, DASH, ZEC, LTC).
   
2. Address Matching:
   - Checks if generated addresses match known "rich" addresses in the database

3. Logging and Information:
   - Logs information about found addresses.

Getting Started:
- Prerequisites:
  - Python 3.x
  - Additional dependencies (hdwallet, rich, rich, sqlite, ).

Run the code:
python3 Multi-Currency-Rich-Address-Finder-v1.0


- Configuration:
  - Parameters include log_file, sqlite_db_filename, found_addresses_filename, and addresses_file_path.
"""

# Multi-Currency Rich Address Scanner v1.0


- Multi-currency rich address finder for Ethereum, Binance Smart Chain, Avalanche, and Polygon blockchains.
- Checks for new addresses and their balances, storing results in `newaddresses.txt` and  Multi Currency Rich Address Finder v1.0 OFFLINE will add the new rich addresses into the `PubKeys.db` every 25000 scans

Features:
1. Blockchain Support:
   - Supports Ethereum (ETH), Binance Smart Chain (BSC), Avalanche (AVAX), and Polygon (MATIC).

2. Database Usage:
   - Utilizes SQLite to store Ethereum , POLYGON MATIC, AVALANCHE, BINANCE SMART CHAIN addresses.

3. File Management:
   - `newaddresses.txt`: Tracks newly discovered addresses.
   - `block.txt`: Stores the last processed block number.

4. Asynchronous Processing:
   - Asynchronously processes multiple blocks.

5. Resumable Processing:
   - Writes the last processed block number to resume from the same point.

Usage:
- Set the initial block number in the `block.txt` file.
- Asynchronously processes blocks, checks balances, and records new addresses with non-zero balances.
- Updates the `block.txt` file with the latest processed block number.

Contributing:
- Contributions are welcome. Open an issue first to discuss major changes.

License:
- Licensed under the MIT License.



These scripts serve as powerful tools for exploring and analyzing rich addresses in various cryptocurrencies. Users are advised to use them responsibly and comply with legal regulations.
"""
