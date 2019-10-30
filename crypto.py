# Transposition Cipher

# original: this_is_a_secret_message_that_i_want_to_transmit
# encrypted:hsi_ertmaesta_att_rnmt
# ti_sasce_esg_htiwn_otasi


def scramble2Encrypt(plainText):
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plainText:
        if charCount % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
        charCount = charCount + 1
    cipherText = oddChars + evenChars
    return cipherText


def scramble2Decrypt(cipherText):
    halfLength = len(cipherText) // 2
    evenChars = cipherText[halfLength:]
    oddChars = cipherText[:halfLength]
    plainText = ""

    for i in range(halfLength):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]

    if len(oddChars) < len(evenChars):
        plainText = plainText + evenChars[-1]

    return plainText


def encryptMessage():
    msg = input("Enter the message to encrypt")
    cipherText = scramble2Encrypt(msg)
    print()

# write a stripSpaces(text) function here


#  write a caesarEncrypt(plainText, shift)
#  write a caesarDecrypt(cipherText, shift)


def caesarEncrypt(plainText, shift):
    result = ""

    for i in range(len(plainText)):
        char = plainText[i]

        if char.isupper():



















