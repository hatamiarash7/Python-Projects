from Crypto.PublicKey import RSA

print("Generate Key ... ", end=" ")
private_key = RSA.generate(4096)
print("Done !")
key = private_key.exportKey('PEM')
f = open('private.txt', 'w')
print("Writing Private Key ... ", end=" ")
f.write(key.decode("utf-8"))
f.close()
print("Done !")

public_key = private_key.publickey()
key = public_key.exportKey('PEM')
f = open('public.txt', 'w')
print("Writing Public Key ... ", end=" ")
f.write(key.decode("utf-8"))
f.close()
print("Done !")