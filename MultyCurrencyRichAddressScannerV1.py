"""
Multi Currency Rich Address Finder V1 For Multi Currency Rich Address Finder v1.0

Developed by Mustafa AKBAL 
                                             ██████╗██╗  ██╗ █████╗ ██╗    ██╗██████╗ ███████╗███████╗██╗  ██╗
                                            ██╔════╝██║  ██║██╔══██╗██║    ██║██╔══██╗██╔════╝██╔════╝██║  ██║
                                            ██║     ███████║███████║██║ █╗ ██║██████╔╝█████╗  ███████╗███████║
                                            ██║     ██╔══██║██╔══██║██║███╗██║██╔══██╗██╔══╝  ╚════██║██╔══██║
                                            ╚██████╗██║  ██║██║  ██║╚███╔███╔╝██║  ██║███████╗███████║██║  ██║
                                             ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝
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

License: MIT License  
Note: This application is the result of hard work and dedication. Please do not distribute it without permission and respect the effort put into its development.

Legal Disclaimer and Warning for Unlawful Use

THE USE OF THIS SOFTWARE FOR ANY ILLEGAL ACTIVITY IS STRICTLY PROHIBITED. THE AUTHORS AND COPYRIGHT HOLDERS OF THIS SOFTWARE DISCLAIM ANY LEGAL RESPONSIBILITY FOR UNLAWFUL USE OR ENGAGEMENT IN ILLEGAL ACTIVITIES USING THIS SOFTWARE.

USERS ARE SOLELY RESPONSIBLE FOR ENSURING THAT THEIR USE OF THIS SOFTWARE COMPLIES WITH APPLICABLE LAWS AND REGULATIONS. ANY UNLAWFUL ACTIVITIES UNDERTAKEN USING THIS SOFTWARE ARE AT THE USER'S OWN RISK.

THIS SOFTWARE IS INTENDED FOR LEGAL AND ETHICAL USE ONLY. ANY USE CONTRARY TO LOCAL, NATIONAL, OR INTERNATIONAL LAWS IS EXPRESSLY PROHIBITED. THE AUTHORS AND COPYRIGHT HOLDERS DO NOT SUPPORT OR CONDONE ILLEGAL ACTIVITIES.

BY USING THIS SOFTWARE, YOU ACKNOWLEDGE AND AGREE THAT UNLAWFUL USE MAY RESULT IN LEGAL CONSEQUENCES, INCLUDING BUT NOT LIMITED TO CRIMINAL PROSECUTION AND CIVIL LIABILITY.

IF YOU ENGAGE IN ILLEGAL ACTIVITIES, YOU DO SO AT YOUR OWN PERIL, AND THE AUTHORS AND COPYRIGHT HOLDERS SHALL NOT BE HELD LIABLE FOR ANY SUCH ACTIONS.

IT IS STRONGLY ADVISED TO USE THIS SOFTWARE RESPONSIBLY AND LEGALLY. IF YOU CANNOT COMPLY WITH THESE TERMS, YOU SHOULD IMMEDIATELY CEASE THE USE OF THIS SOFTWARE.


Disclaimer of Liability

THE USE OF THIS SOFTWARE AND ANY ACTIONS RESULTING FROM IT ARE THE SOLE RESPONSIBILITY OF THE USER. THE AUTHORS AND COPYRIGHT HOLDERS OF THIS SOFTWARE ARE NOT LIABLE FOR ANY DAMAGES, LOSSES, OR RESPONSIBILITIES ARISING OUT OF THE USE OF THIS SOFTWARE.

THIS SOFTWARE IS PROVIDED "AS IS," WITHOUT ANY WARRANTIES, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. NO WARRANTIES ARE PROVIDED FOR THE USE OF THIS SOFTWARE.

THE USE OF THIS SOFTWARE MAY INVOLVE RISKS OF DAMAGE TO COMPUTER SYSTEMS OR DATA. USERS SHOULD TAKE NECESSARY SECURITY PRECAUTIONS BEFORE USING THE SOFTWARE AND SHOULD BE SURE TO BACK UP THEIR DATA BEFORE CONTINUING TO USE THE SOFTWARE.

THE USE OF THE SOFTWARE IMPLIES THAT YOU UNDERSTAND AND ACCEPT THIS DISCLAIMER OF LIABILITY IN ITS ENTIRETY. IF YOU DO NOT AGREE TO THESE TERMS, YOU SHOULD NOT USE THE SOFTWARE.


"""

from web3 import Web3
import sqlite3
import os
import sys
from colorama import Fore, Style
import asyncio
import concurrent.futures
from rich.traceback import install
install()


appPath = os.path.dirname(os.path.abspath(__file__))

ethereum_node_url = 'https://eth.drpc.org'
bsc_node_url = 'https://bsc-dataseed.binance.org'
avax_node_url = 'https://avalanche.drpc.org'
polygon_node_url = 'https://polygon.drpc.org'

web3 = Web3(Web3.HTTPProvider(ethereum_node_url))
web3_bsc = Web3(Web3.HTTPProvider(bsc_node_url))
web3_avax = Web3(Web3.HTTPProvider(avax_node_url))
web3_polygon = Web3(Web3.HTTPProvider(polygon_node_url))

new_addresses = []
new_addresses_file = os.path.join(appPath, 'newaddresses.txt')

db_path = os.path.join(appPath, 'PubKeys.db')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS DataBase (
        PubKeys TEXT PRIMARY KEY
    )
''')
conn.commit()

start_block_file = os.path.join(appPath, 'block.txt')
start_block = 0

if os.path.exists(start_block_file):
    with open(start_block_file, 'r') as start_block_file_reader:
        start_block_content = start_block_file_reader.read().strip()
        try:
            if start_block_content:
                start_block = int(start_block_content)
        except ValueError:
            print("Error: Invalid content in block.txt file. Using default start_block value.")
else:
    print("Warning: block.txt not found. Using default start_block value.")

def load_addresses_from_file():
    with open(new_addresses_file, 'r') as file:
        addresses = file.read().splitlines()
        new_addresses.extend(addresses)
        print(
            f"{Fore.CYAN}TOTAL {len(new_addresses)} NEW ADDRESSES FOUND \n"
        )
    return addresses

async def get_latest_block_number():
    return web3.eth.block_number

async def get_transactions_in_block(block_number):
    block = web3.eth.get_block(block_number, full_transactions=True)
    return block['transactions'] if block else []

async def check_address_balance(address):
    try:
        balance_wei = web3.eth.get_balance(address)
        eth_balance = web3.from_wei(balance_wei, 'ether')

        try:
            balance_wei_bsc = web3_bsc.eth.get_balance(address)
            bsc_balance = web3_bsc.from_wei(balance_wei_bsc, 'ether')
        except Exception as e_bsc:
            print(f'BSC Balance Error ({address}): {str(e_bsc)}')
            bsc_balance = 0

        try:
            balance_wei_avax = web3_avax.eth.get_balance(address)
            avax_balance = web3_avax.from_wei(balance_wei_avax, 'ether')
        except Exception as e_avax:
            print(f'AVAX Balance Error ({address}): {str(e_avax)}')
            avax_balance = 0

        try:
            balance_wei_polygon = web3_polygon.eth.get_balance(address)
            polygon_balance = web3_polygon.from_wei(balance_wei_polygon, 'ether')
        except Exception as e_polygon:
            print(f'Polygon Balance Error ({address}): {str(e_polygon)}')
            polygon_balance = 0

        return {'eth_balance': eth_balance, 'bsc_balance': bsc_balance, 'avax_balance': avax_balance, 'polygon_balance': polygon_balance}
    
    except Exception as e:
        print(f'General error while checking address balance ({address}): {str(e)}')
        return {'eth_balance': 0, 'bsc_balance': 0, 'avax_balance': 0, 'polygon_balance': 0}

async def write_to_new_addresses_file(address):
    try:
        with open(new_addresses_file, 'a') as file:
            file.write(f"{address}\n")
    except Exception as e:
        print(f'Error while writing to new addresses file: {str(e)}')

async def check_addresses_in_database(address):
    try:
        query = 'SELECT COUNT(*) FROM DataBase WHERE PubKeys = ?'
        cursor.execute(query, (address,))
        count = cursor.fetchone()[0]

        return count > 0

    except Exception as e:
        print(f'Error while checking address in database: {str(e)}')
        return False

def clear_terminal():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

async def process_block(block_number, latest_block_number):
    transactions = await get_transactions_in_block(block_number)

    for tx in transactions:
        sender = tx['from']
        receiver = tx['to']

        try:
            if sender is not None and receiver is not None:
                await process_address(sender, block_number, latest_block_number)
                await process_address(receiver, block_number, latest_block_number)

        except Exception as e:
            print(f'Transaction error: {str(e)}')

async def process_address(address, block_number, latest_block_number):
    global new_addresses
    try:
        if await check_addresses_in_database(address[-8:]):
            return

        balances = await check_address_balance(address)

        if balances['eth_balance'] > 0.00001 or balances['avax_balance'] > 0.00001 or balances['polygon_balance'] > 0.00001 or balances['bsc_balance'] > 0.00001:
            new_addresses.append(address)
            await write_to_new_addresses_file(address)
            clear_terminal()
            load_addresses_from_file()
            print(
                f"{Fore.GREEN}TOTAL NEW ADDRESSES: {len(new_addresses)}{Style.RESET_ALL}\n"
                f"{Fore.YELLOW}PROCESSED BLOCK: {block_number}/{latest_block_number}\n"
                f"{Fore.RED}RELATED ADDRESS: {address}\n"
                f"{Fore.YELLOW}ETH BALANCE: {balances['eth_balance']:.6f} ETH\n"
                f"{Fore.RED}AVAX BALANCE: {balances['avax_balance']:.6f} AVAX\n"
                f"{Fore.GREEN}POLYGON BALANCE: {balances['polygon_balance']:.6f} MATIC\n"
                f"{Fore.YELLOW}BNB BALANCE: {balances['bsc_balance']:.6f} BNB\n"
                f"{Fore.CYAN}------------------------{Style.RESET_ALL}\n"
            )

            new_addresses = []

    except Exception as error:
        print(f'Address processing error ({address}): {str(error)}')

    try:
        with open(start_block_file, 'w') as start_block_file_writer:
            start_block_file_writer.write(str(block_number))
    except Exception as error:
        print(f'Error: Failed to write to block.txt file: {str(error)}')

async def process_blocks(start_block, end_block):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        loop = asyncio.get_event_loop()
        tasks = []
        for block_number in range(start_block + 1, end_block + 1):
            tasks.append(await loop.run_in_executor(executor, process_block, block_number, end_block))
        await asyncio.gather(*tasks)


async def main():
    try:
        current_block_number = start_block
        latest_block_number = await get_latest_block_number()
        chunk_size = 10

        for chunk_start in range(current_block_number, latest_block_number, chunk_size):
            chunk_end = min(chunk_start + chunk_size, latest_block_number)
            await process_blocks(chunk_start, chunk_end)

    except Exception as e:
        print(f'Main process error: {str(e)}')
    finally:
        conn.close()
        print(f'{Fore.CYAN}SQLite database connection closed successfully.{Style.RESET_ALL}')

if __name__ == "__main__":
    load_addresses_from_file()
    asyncio.run(main())
