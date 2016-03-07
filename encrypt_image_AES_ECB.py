import Image, hashlib
from Crypto import Random
from Crypto.Cipher import AES
im = Image.open('heckert_gnu.png')
raw = im.tobytes()
IV = Random.new().read(AES.block_size)
#print raw
#print im
key = hashlib.sha256("password".encode()).digest()

mode = AES.MODE_ECB
encryptor = AES.new(key, mode, IV=IV)

encrypted_bytes = encryptor.encrypt(raw)

im_out = Image.frombytes(im.mode, im.size, encrypted_bytes)
im_out.save('ECB.png')
