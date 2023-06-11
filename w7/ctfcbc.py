import requests
from bs4 import BeautifulSoup

def get_ciphertext(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.find_all('pre')[0].get_text().split('\n')
    ciphertext = [line for line in data if len(line) == 32] 
    return ciphertext

def find_first_byte():
    url = "http://skidctf.reloaded.live/chals/crypto/prefix/?prefix="

    prefix = 'A' * 15
    target_url = url + prefix
    target_ciphertext = get_ciphertext(target_url)[0]

    for i in range(256):
        test_prefix = prefix + chr(i)
        test_url = url + test_prefix
        test_ciphertext = get_ciphertext(test_url)[0]
        if test_ciphertext == target_ciphertext:
            return chr(i)
    return None

first_byte = find_first_byte()
if first_byte:
    print("First byte of the secret: " + first_byte)
else:
    print("Could not find the first byte of the secret.")
