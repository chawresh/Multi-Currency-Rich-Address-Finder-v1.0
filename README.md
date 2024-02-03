Multi Currency Rich Address Finder v1.0


Overview

Developed by Mustafa AKBAL
Contact: mstf.akbal@gmail.com
Ethereum Address for Donations: 0x06aABB3CF9c2F6d74901eD02556D34019b31f5B5
License: MIT License

Legal Disclaimer and Warning
Strict prohibition on illegal activities.
User responsibility for compliance with laws.
Intended for legal and ethical use only.
Consequences of unlawful use.

Features
Generates random private keys and addresses for various cryptocurrencies (BTC, ETH, TRX, DOGE, BCH, DASH, ZEC, LTC).
Checks if generated addresses match known "rich" addresses in the database.
Logs information about found addresses.
Provides information on addresses and balances.

Getting Started
Prerequisites: Python 3.x, additional dependencies (hdwallet, rich).


Configuration parameters include log_file, sqlite_db_filename, found_addresses_filename, and addresses_file_path.

Multi-Currency Rich Address Scanner v1.0

Overview
Multi-currency rich address finder for Ethereum, Binance Smart Chain, Avalanche, and Polygon blockchains.
Checks for new addresses and their balances, storing results in a SQLite database.

Features
Supports Ethereum (ETH), Binance Smart Chain (BSC), Avalanche (AVAX), and Polygon (MATIC).

Utilizes SQLite to store Ethereum addresses.

Manages files: newaddresses.txt tracks newly discovered addresses, and block.txt stores the last processed block number

Asynchronously processes multiple blocks.
Writes the last processed block number to resume from the same point.

Usage
Set the initial block number in the block.txt file.

Asynchronously processes blocks, checks balances, and records new addresses with non-zero balances.

Updates the block.txt file with the latest processed block number.

Contributing
Contributions are welcome. Open an issue first to discuss major changes.

License
Licensed under the MIT License.

Acknowledgments
Thanks to Mustafa AKBAL for developing the tool.
These scripts seem to be powerful tools for exploring and analyzing rich addresses in various cryptocurrencies. Users are advised to use them responsibly and comply with legal regulations. If you have any specific questions or if there's anything else you'd like assistance with, feel free to ask!
