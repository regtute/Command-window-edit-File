from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad

def check_normal_start():

    check_normal = b'tuyiweii'

    with open('.\\DataBase\\Support.db', 'rb') as file:
        return_text = file.read()
        # print(return_text)

    decipher = DES.new(check_normal, DES.MODE_ECB)

    plain_text = decipher.decrypt(return_text)

    unpadded_text = unpad(plain_text, DES.block_size)

    return(unpadded_text.decode('utf-8'))[::-1]
def errors():
    check_normal = b'tuyiweii'

    with open('.\\DataBase\\Support.db', 'rb') as file:
        return_text = file.read()
        # print(return_text)

    decipher = DES.new(check_normal, DES.MODE_ECB)

    plain_text = decipher.decrypt(return_text)

    unpadded_text = unpad(plain_text, DES.block_size)

    return((unpadded_text.decode('utf-8'))[::-1]).replace('ekam','')