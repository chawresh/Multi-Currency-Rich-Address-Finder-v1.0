"""
Multi Currency Rich Address Finder v1.0

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
                                            LTC ltc_p2wsh            : ltc1q47rduwq76v4fteqvxm8p9axq39nq25kurgwlyaefmyqz3nhyc8rsmce759
                                            LTC ltc_p2wpkh           : ltc1q2l29nc6puvuk0rn449wf6l8rm62wuxst6qkkpv


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

import os
import logging
import traceback
from hdwallet import HDWallet
from hdwallet.symbols import BTC, ETH, TRX, DOGE, BCH, DASH, ZEC, LTC
import random
import time
from concurrent.futures import ProcessPoolExecutor
import sqlite3
from queue import Queue
from logging.handlers import QueueHandler, QueueListener
from threading import local, Lock, Thread
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.traceback import install


install()



author = ("""[gold1 on grey15]\
                                             ██████╗██╗  ██╗ █████╗ ██╗    ██╗██████╗ ███████╗███████╗██╗  ██╗
                                            ██╔════╝██║  ██║██╔══██╗██║    ██║██╔══██╗██╔════╝██╔════╝██║  ██║
                                            ██║     ███████║███████║██║ █╗ ██║██████╔╝█████╗  ███████╗███████║
                                            ██║     ██╔══██║██╔══██║██║███╗██║██╔══██╗██╔══╝  ╚════██║██╔══██║
                                            ╚██████╗██║  ██║██║  ██║╚███╔███╔╝██║  ██║███████╗███████║██║  ██║
                                             ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝
                                            AUTHOR : Mustafa AKBAL e-mail: mstf.akbal@gmail.com 
                                            Telegram: @chawresho   Instagram: mstf.akbal
                                             ================= DONATE ADDRESSES ========================
                                            Compressed Address: 191QB72rS77vP8NC1EC11wWqKtkfbm5SM8
                                            UnCompressed Address: 1HTZrCDM9Qsp7aztvbeSo5cP7u9dbwn6Qr
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
                                            LTC ltc_p2wsh            : ltc1q47rduwq76v4fteqvxm8p9axq39nq25kurgwlyaefmyqz3nhyc8rsmce759
                                            LTC ltc_p2wpkh           : ltc1q2l29nc6puvuk0rn449wf6l8rm62wuxst6qkkpv[/]""")

app_path = os.path.dirname(os.path.abspath(__file__))

# Global variables
_thread_local = local()
address_count = 0
win = 0
console = Console()
style = "bold on grey11"

log_file = os.path.join(app_path, "app_log.log")
sqlite_db_filename = os.path.join(app_path, 'PubKeys.db')
found_addresses_filename = os.path.join(app_path, 'found.txt')
addresses_file_path = os.path.join(app_path, 'newaddresses.txt')



# Set logging level
logging.basicConfig(level=logging.INFO)
log_queue = Queue()
handler = logging.FileHandler(log_file)
queue_handler = QueueHandler(log_queue)
listener = QueueListener(log_queue, handler)
listener.start()

# Add a Formatter for colored logging.
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Variables to store address types of Bitcoin and other cryptocurrencies.
p2pkh_btc, p2wpkh_btc, p2wpkh_in_p2sh_btc, p2wsh_in_p2sh_btc, p2sh_btc, p2wsh_btc, ethaddr, trxadd, dgaddr, bch_p2pkh, bch_p2sh, dash_p2pkh, dash_p2sh, zec_p2pkh, zec_p2sh, ltc_p2pkh, ltc_p2sh, ltc_p2wsh, ltc_p2wpkh = [None] * 19
def create_table(cursor):
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS DataBase (
                PubKeys TEXT NOT NULL UNIQUE
            )
        """)
        cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_pubkeys ON DataBase (PubKeys)")
    except sqlite3.Error as e:
        logging.error(f'SQLite Error: {e}\n{traceback.format_exc()}')

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_connection(db_filename):
    try:
        conn = sqlite3.connect(db_filename)
        cursor = conn.cursor()
        return conn, cursor
    except sqlite3.Error as e:
        logging.error(f'SQLite Connection Error: {e}\n{traceback.format_exc()}')
        return None, None

def generate_wallet():
    with ProcessPoolExecutor(max_workers=4) as executor:
        try:
            # Creat a Random Private Key
            private_key = "".join(random.choice("1111111") for _ in range(64))

            # Create HD Wallets
            hd_btc = HDWallet(BTC)
            hd_eth = HDWallet(ETH)
            hd_trx = HDWallet(TRX)
            hd_doge = HDWallet(DOGE)
            hd_bch = HDWallet(BCH)
            hd_dash = HDWallet(DASH)
            hd_zec = HDWallet(ZEC)
            hd_ltc = HDWallet(LTC)

            # Load the private key for each wallet separately.
            hd_btc.from_private_key(private_key)
            hd_eth.from_private_key(private_key)
            hd_trx.from_private_key(private_key)
            hd_doge.from_private_key(private_key)
            hd_bch.from_private_key(private_key)
            hd_dash.from_private_key(private_key)
            hd_zec.from_private_key(private_key)
            hd_ltc.from_private_key(private_key)

            # Bitcoin addresses types
            global p2pkh_btc, p2wpkh_btc, p2wpkh_in_p2sh_btc, p2wsh_in_p2sh_btc, p2sh_btc, p2wsh_btc
            p2pkh_btc = hd_btc.p2pkh_address()
            p2wpkh_btc = hd_btc.p2wpkh_address()
            p2wpkh_in_p2sh_btc = hd_btc.p2wpkh_in_p2sh_address()
            p2wsh_in_p2sh_btc = hd_btc.p2wsh_in_p2sh_address()
            p2sh_btc = hd_btc.p2sh_address()
            p2wsh_btc = hd_btc.p2wsh_address()

            # Ethereum address type
            global ethaddr
            ethaddr = hd_eth.p2pkh_address()

            # Tron address type
            global trxadd
            trxadd = hd_trx.p2pkh_address()

            # Dogecoin address type
            global dgaddr
            dgaddr = hd_doge.p2pkh_address()

            # Bitcoin Cash addresses types
            global bch_p2pkh, bch_p2sh
            bch_p2pkh = hd_bch.p2pkh_address()
            bch_p2sh = hd_bch.p2sh_address()

            # Dash aaddresses types
            global dash_p2pkh, dash_p2sh
            dash_p2pkh = hd_dash.p2pkh_address()
            dash_p2sh = hd_dash.p2sh_address()

            # Zcash addresses types
            global zec_p2pkh, zec_p2sh
            zec_p2pkh = hd_zec.p2pkh_address()
            zec_p2sh = hd_zec.p2sh_address()

            # Litecoin addresses types
            global ltc_p2pkh, ltc_p2sh, ltc_p2wsh, ltc_p2wpkh
            ltc_p2pkh = hd_ltc.p2pkh_address()
            ltc_p2sh = hd_ltc.p2sh_address()
            ltc_p2wsh = hd_ltc.p2wsh_address()
            ltc_p2wpkh = hd_ltc.p2wpkh_address()

            # Add all addresses to a list.
            global addresses
            addresses = [p2pkh_btc, p2wpkh_btc, p2wpkh_in_p2sh_btc, p2wsh_in_p2sh_btc, p2sh_btc, p2wsh_btc,
                         ethaddr, trxadd, dgaddr, bch_p2pkh, bch_p2sh, dash_p2pkh, dash_p2sh, zec_p2pkh, zec_p2sh, ltc_p2pkh, ltc_p2sh, ltc_p2wsh, ltc_p2wpkh]

            return private_key, addresses
        except Exception as e:
            logging.error(f'Creating Wallet Error: {e}\n{traceback.format_exc()}')
            return None, None, None

def add_to_database(cursor, conn, addresses_file_path):
    try:
        total = 0
        with open(addresses_file_path, "r") as addresses_file:
            newaddresses = [line.strip()[-8:] for line in addresses_file if line.strip()]
        for address in newaddresses:
            cursor.execute("SELECT COUNT(*) FROM DataBase WHERE PubKeys = ?", (address,))
            count = cursor.fetchone()[0]
            if count == 0:
                cursor.execute("INSERT INTO DataBase (PubKeys) VALUES (?)", (address,))
                total += 1
                print(f'[white]Total: [gold1 on grey15]{total}[gold1 on grey15] {address} [white]Address Is Adding To Database. Total: [gold1 on grey15]{total} [white] Addresses Are Added To Database.[/]', end='\r')
            else:
                print(f'[white]Total: [gold1 on grey15]{total}[gold1 on grey15] {address} [white]Already In Database.[/]', end='\r')
        conn.commit()
        with open(addresses_file_path, 'w') as file:
            file.write("")
            print(f'[white]Total: [gold1 on grey15]{total} [white]Addresses Are Added To Database and Addresses in [gold1 on grey15]newaddresses.txt [white]Are Erased.[/]')
    except sqlite3.Error as hata:
        print(f"SQLite Error: {hata}")
    except FileNotFoundError as hata:
        print(f"File Not Found Error: {hata}")
    except Exception as hata:
        print(f"An unexpected error occurred: {hata}")

def save_to_found_addresses(private_key, addresses, matched_address, found_addresses_filename):
    try:
        with open(found_addresses_filename, 'a') as file:
            file.write(f"Private Key: {private_key}\n")
            file.write("Addresses:\n")
            for address in addresses:
                file.write(f"{address}\n")
            file.write(f"Matched Address in Database: {matched_address}\n\n")

    except IOError as e:
        logging.error(f'Writing File Error: {e}\n{traceback.format_exc()}')

def get_address_count(cursor):
    try:
        cursor.execute("SELECT COUNT(*) FROM DataBase")
        return cursor.fetchone()[0]
    except sqlite3.Error as e:
        logging.error(f'Database Error: {e}\n{traceback.format_exc()}')
        return 0

def show_first_addresses(cursor, limit=10):
    try:
        cursor.execute(f"SELECT * FROM DataBase LIMIT {limit}")
        addresses = cursor.fetchall()
        logging.info(f"First {limit} Address:")
        for address in addresses:
            logging.info(address[0])
    except sqlite3.Error as e:
        logging.error(f'Database Error: {e}\n{traceback.format_exc()}')

def check_database(cursor, address):
    cursor.execute("SELECT COUNT(*) FROM DataBase WHERE PubKeys = ?", (address,))
    return cursor.fetchone()[0] > 0

def process_private_key(args):
    private_key, addresses, found_addresses_filename, db_filename = args
    try:
        conn, cursor = get_connection(db_filename)
        for address in addresses:
            if check_database(cursor, address[-8:]):
                matched_address = address
                save_to_found_addresses(private_key, addresses, matched_address, found_addresses_filename)
                win += 1

    except sqlite3.Error as e:
        logging.error(f'Database Error: {e}\n{traceback.format_exc()}')
    finally:
        win_lock.release()
        if conn:
            conn.close()


def main():
    global p2pkh_btc, p2wpkh_btc, p2wpkh_in_p2sh_btc, p2wsh_in_p2sh_btc, p2sh_btc, p2wsh_btc, ethaddr, trxadd, dgaddr, bch_p2pkh, bch_p2sh, dash_p2pkh, dash_p2sh, zec_p2pkh, zec_p2sh, ltc_p2pkh, ltc_p2sh, ltc_p2wsh, ltc_p2wpkh
    try:
        conn, cursor = get_connection(sqlite_db_filename)
        create_table(cursor)
        add_to_database(cursor, conn, addresses_file_path)
        global address_count,win
        address_count = get_address_count(cursor)

        private_key_addresses_count = 0
        iteration_count = 0
        iteration_step = 10000
        wait_time = 0.0000001



        with ProcessPoolExecutor(max_workers=6) as executor:
            while True:
                private_key_addresses_count += 22
                private_key, addresses = generate_wallet()

                if not private_key:
                    continue

                iteration_count += 1

                if iteration_count >= iteration_step:
                    iteration_step += 10000
                    with open(addresses_file_path, 'r') as file:
                        if not file.read():
                            print(f"{addresses_file_path} New Rich Addresses Are Not Found.")
                        else:
                            print(f"{addresses_file_path} Some New Rich Addresses Found.")
                            add_to_database(cursor, conn, addresses_file_path)
                            address_count = get_address_count(cursor)

                args = (private_key, addresses, found_addresses_filename, sqlite_db_filename)
                executor.submit(process_private_key, args)


                info_panel = (
                    f"[gold1 on grey15]Total Rich Addresses In Database: [orange_red1]{address_count}[/][gold1 on grey15] "
                    f"[gold1 on grey15]Total Checked : [orange_red1]{private_key_addresses_count} [/]"
                    f"[gold1 on grey15]Win: [white]{win}[/]\n"
                    f"[gold1 on grey15]PRIVATE KEY              : [grey54]{private_key}[/]\n"
                    f"[gold1 on grey15]BTC p2pkh                : [white]{p2pkh_btc}[/]\n"
                    f"[gold1 on grey15]BTC p2wpkh               : [white]{p2wpkh_btc}[/]\n"
                    f"[gold1 on grey15]BTC p2wpkh_in_p2sh       : [white]{p2wpkh_in_p2sh_btc}[/]\n"
                    f"[gold1 on grey15]BTC p2wsh_in_p2sh        : [white]{p2wsh_in_p2sh_btc}[/]\n"
                    f"[gold1 on grey15]BTC p2sh                 : [white]{p2sh_btc}[/]\n"
                    f"[gold1 on grey15]BTC p2wsh                : [white]{p2wsh_btc}[/]\n"
                    f"[gold1 on grey15]ETH/BSC/AVAX/POLYGON     : [white]{ethaddr}[/]\n"
                    f"[gold1 on grey15]TRX                      : [white]{trxadd}[/]\n"
                    f"[gold1 on grey15]DOGE                     : [white]{dgaddr}[/]\n"
                    f"[gold1 on grey15]BCH bch_p2pkh            : [white]{bch_p2pkh}[/]\n"
                    f"[gold1 on grey15]BCH bch_p2sh             : [white]{bch_p2sh}[/]\n"
                    f"[gold1 on grey15]DASH dash_p2pkh          : [white]{dash_p2pkh}[/]\n"
                    f"[gold1 on grey15]DASH dash_p2sh           : [white]{dash_p2sh}[/]\n"
                    f"[gold1 on grey15]ZEC zec_p2pkh            : [white]{zec_p2pkh}[/]\n"
                    f"[gold1 on grey15]ZEC zec_p2sh             : [white]{zec_p2sh}[/]\n"
                    f"[gold1 on grey15]LTC ltc_p2pkh            : [white]{ltc_p2pkh}[/]\n"
                    f"[gold1 on grey15]LTC ltc_p2sh             : [white]{ltc_p2sh}[/]\n"
                    f"[gold1 on grey15]LTC ltc_p2wsh            : [white]{ltc_p2wsh}[/]\n"
                    f"[gold1 on grey15]LTC ltc_p2wpkh           : [white]{ltc_p2wpkh}[/]"
                )

                clear_terminal()
                print(author)
                console.print(
                    Panel(str(info_panel), title="[white]Multi Currency Rich Address Finder OFFLINE[/]",
                          subtitle="[green_yellow] Developed By Mustafa AKBAL contact: mstf.akbal@gmail.com [/]", style="gold1"), style=style, justify="full"
                )
                time.sleep(wait_time)

    except KeyboardInterrupt:
        logging.info("Program is closing. Found wallets are saved...")

        if conn:
            conn.close()
        if cursor:
            cursor.close()
        exit(0)
    except sqlite3.Error as e:
        logging.error(f"SQLite error: {e}\n{traceback.format_exc()}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}\n{traceback.format_exc()}")

if __name__ == "__main__":
    try:
        clear_terminal()
        print(author)
        start_message = "Launching the application... Please wait! Preparing the database may take a few minutes."
        console.print(
            Panel(str(start_message), title="[white]Multi Currency Rich Address Finder[/]",
                subtitle="[green_yellow blink] Developed By Mustafa AKBAL contact: mstf.akbal@gmail.com [/]", style="gold1"), style=style, justify="full"
            )
        main()
    except Exception as e:
        print(f'Main Error: {e}')
