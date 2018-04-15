#!/usr/bin/env python3
# setup.py
import json

from os import path

def saveSecrets(file='secrets/secrets.json'):
    if not path.exists(file):
        if not path.isdir('secrets'):
            subprocess.call(['mkdir', '-p', 'secrets'])
        if input("Create `secrets.json` now? (Y/n) ") in ['Y', 'y']:
            secrets = {}
            secrets['TELEGRAM_BOT_TOKEN'] = str(input("Your Telegram Bot Token: "))
            with open(file, 'w') as sf:
                json.dump(secrets, sf, indent=4)
        else:
            exit()
    else:
        print("{} already exists. Quitting.".format(file))

def main():
    welcome = """
Welcome to the BeanBot setup script. Very simply, this setup script asks you a
question and saves your answers in JSON format.
    """
    print(welcome)

    saveSecrets()

if __name__ == '__main__':
    main()