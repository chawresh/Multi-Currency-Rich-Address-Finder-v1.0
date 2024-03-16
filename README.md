 Multi Currency Rich Address Finder v1.0 OFFLINE  and  Multi-Currency Rich Address Scanner v1.0 

 
THE FASTEST WALLET CHECKER


DOWNLOAD DATABASE WITH OVER `234.263.050`  ADDRESSES WITH BALANCE ( ONLY WITH LAST 8 DIGITS TO SCAN FASTER)

IF THE DOWNLOAD LINK DOES NOT WORK, CONTACT ME

DATABASE DOWNLOAD LINK: https://drive.google.com/file/d/1DPjz1ywSiIonntK_B_IKg3l4Nf7pipmE/view?usp=drive_link

![Alt text](https://github.com/chawresh/Multi-Currency-Rich-Address-Finder-v1.0/blob/fd81b6ff20e870f93960c13290684c81a3df0eef/screenshot.png)


Developed by Mustafa AKBAL 

                            AUTHOR : Mustafa AKBAL e-mail: mstf.akbal@gmail.com 
                            Telegram: @chawresho   Instagram: mstf.akbal
                             ================= DONATE ADDRESSES ========================
                            BTC p2pkh                : 1NWQ4fEprRs6a2WdYKSz45aN7d2pZQLWpj
                            BTC p2wpkh               : bc1qa05lfk02xpp5qrjj9z7nkvel0jxdr6de8flu69
                            BTC p2wpkh_in_p2sh       : 3EHkXJB6tqAnxtFHphvKge3x9jsXxkUfCi
                            BTC p2wsh_in_p2sh        : 381WvfLxoE5TxosjDxH76w4N7WCxuuj8td
                            BTC p2sh                 : 37EZzu8wpmrcK32bi1WtS71wCrjLSZ7NYc
                            BTC p2wsh                : bc1qdja52dqcqy7wf4fz2uqgu0az2xuyrp2qz628fyyelkspq2vzrtms7e4tta
                            ETH/BSC/AVAX/POLYGON     : 0x85b8F14fC0CfB76b82aE5eDaED9CA4CC13A4E0f3
                            TRX                      : TNAGRcQGKQUpweLqwpTP8iALMyTLTDQQH1
                            DOGE                     : DSeVbvBU9qmP72hEGuSYbqjxzkm7uPcrte
                            BCH bch_p2pkh            : CdyHdhatjUqdUAR4E4mudbCPjkFERnznrh
                            BCH bch_p2sh             : HC4gTha2g65GwCudZhB3QVYUEWkME6PdLA
                            DASH dash_p2pkh          : XxCEtutip95giy7DQCmCucG9wxcWZYYiu8
                            DASH dash_p2sh           : 7XxCq6R7dkxFJoZYydBPmV1b8QZiFsnKia
                            ZEC zec_p2pkh            : t1fP14zexpkehAfZXUkG7BtgHNHDuGny4sZ
                            ZEC zec_p2sh             : t3Q7B1EZ5o6eCug5VeSL1Zv7rTWvRD48Gx2
                            LTC ltc_p2pkh            : LgjMKsYew679pqCniTSHL6e8KqQ6ddh4fC
                            LTC ltc_p2sh             : MDSiJnYumti37YJVotWEFkGLXZKnPw3yCH

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
