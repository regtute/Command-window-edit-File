from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad

# 设置密钥，DES要求密钥长度为8字节
key = b'tuyiweii'

# 从文件中读取加密后的数据
with open('Support.db', 'rb') as file:
    cipher_text = file.read()
    print(cipher_text)

# 创建DES解密器
decipher = DES.new(key, DES.MODE_ECB)

# 解密数据
plain_text = decipher.decrypt(cipher_text)

# 去除填充
unpadded_text = unpad(plain_text, DES.block_size)

# 输出解密后的数据
print("解密后的数据:", unpadded_text.decode('utf-8'))