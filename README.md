 Multi Currency Rich Address Finder v1.0 OFFLINE  and  Multi-Currency Rich Address Scanner v1.0 

 
THE FASTEST WALLET CHECKER


DOWNLOAD DATABASE WITH OVER 131.000.000 RICH ADDRESSES ( ONLY WITH LAST 8 DIGITS TO SCAN FASTER)

IF THE DOWNLOAD LINK DOES NOT WORK, CONTACT ME

DATABASE DOWNLOAD LINK: https://drive.google.com/file/d/1kngLXO0ADuLJJu9xMCNU4yLo_d-w6_vz/view?usp=drive_link

![Alt text](https://github.com/chawresh/Multi-Currency-Rich-Address-Finder-v1.0/blob/efc076f1062ac16ddace7cc0cc3cbe51d453bb1a/screenshot1.png)

"""
Overview:
- Developed by `Mustafa AKBAL`
- Contact: mstf.akbal@gmail.com
- Instagram: `mstf.akbal`
- Ethereum Address for Donations: `0x06aABB3CF9c2F6d74901eD02556D34019b31f5B5`
- License: MIT License

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

"""
Overview:
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

Acknowledgments:
- Thanks to `Mustafa AKBAL` for developing the tool.

These scripts serve as powerful tools for exploring and analyzing rich addresses in various cryptocurrencies. Users are advised to use them responsibly and comply with legal regulations.
"""
