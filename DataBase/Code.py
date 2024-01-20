from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

# 设置密钥，DES要求密钥长度为8字节
key = b'tuyiweii'

# 创建DES加密器
cipher = DES.new(key, DES.MODE_ECB)

# 要加密的数据
data = b'Regtute make'

# 对数据进行填充
padded_data = pad(data, DES.block_size)

# 加密填充后的数据
cipher_text = cipher.encrypt(padded_data)

# 将加密后的数据写入文件
with open('Support.db', 'wb') as file:
    file.write(cipher_text)