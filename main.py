from encyption import encrypt, decrypt

while True:
    '''This is main function which executes both encryption and decryption'''
    encrypt()
    decrypt()
    user = input("\nDo you want to continue?(Y/N) : ").lower()
    if user == 'y':
        continue
    else:
        exit()
