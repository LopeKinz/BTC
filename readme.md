# Bitcoin Wallet Cracker

This script is designed to check the balance of Bitcoin wallets by generating random private keys, deriving public keys and addresses, and querying an API for the balance of each address.

## Prerequisites

Before running the script, make sure you have the following dependencies installed:

- Python 3.x
- `bitcoin` library
- `requests` library
- `colorama` library

You can install the required libraries using the following command:

```
pip install bitcoin requests colorama
```

## Usage

1. Run the script using Python:

```
python start.py
```

2. The script will check the status of the API server. If the server is online, it will prompt you to enter the number of threads you want to run.

3. Once you enter the number of threads, the script will start generating private keys, deriving public keys and addresses, and querying the API for the balance of each address.

4. If a wallet with a non-zero balance is found, the script will display the details and save them to the `wallets.txt` file.

5. If any errors occur during the process, they will be logged in the `logs.txt` file.

## Notes

- The script relies on an API to check the balance of Bitcoin addresses. Make sure the API server is accessible and functioning properly.

- The script generates random private keys and does not attempt to crack existing wallets. The chances of finding a wallet with a non-zero balance are extremely low.

- This script is for educational purposes only. Use it responsibly and do not use it for illegal activities.

## Contributors

- Pinkyhax
- BanHammer Team



i hate read me files.... 
watch this https://www.youtube.com/watch?v=CdIHPwRW4zE


if it crashes!
```
1. uninstall all python versions!
2. download python 3.10 from python.org
3. CHECK Add to PATH !!!!!!!!!!!!!!!!!!!!!!!
4. (Optional) Disable PATH Limit
5. Download python 3.10 from Microsoft Store
6. Run the Install.py
7. try open the run_api.py 
7.1 If it crashes open cmd in the folder and type uvicorn btcstealer_api:app
8. rightclick btc_stealer.py 
9. open with python (Not the Microsoft store version!)
10. Done!
```
