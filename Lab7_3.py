def gen_key(keyword, message):
    keyword = keyword.replace(" ", "")
    key = ""
    message_length = len(message)
    key_len = len(keyword)
    for i in range(message_length):
        key += keyword[i % key_len]
    return key

def vig_enc(message, key):
    enc = ""
    for i in range(len(message)):
        char = message[i]
        if char.isalpha():
            shift = ord(key[i].upper()) - ord('А')
            if char.islower():
                enc_char = chr(((ord(char) - ord('а') + shift) % 32) + ord('а'))
            else:
                enc_char = chr(((ord(char) - ord('А') + shift) % 32) + ord('А'))
            enc += enc_char
        else:
            enc += char
    return enc

def vig_dec(enc, key):
    dec_text = ""
    for i in range(len(enc)):
        char = enc[i]
        if char.isalpha():
            shift = ord(key[i].upper()) - ord('А')
            if char.islower():
                dec_char = chr(((ord(char) - ord('а') - shift + 32) % 32) + ord('а'))
            else:
                dec_char = chr(((ord(char) - ord('А') - shift + 32) % 32) + ord('А'))
            dec_text += dec_char
        else:
            dec_text += char
    return dec_text

keyword = "Гжегож Бженьшченьшчикевич"
message = "Хчоншчмжевошице повет венколоды"

key = gen_key(keyword, message)

enc_mes = vig_enc(message, key)
print("Зашифрованное сообщение:", enc_mes)

dec_mes = vig_dec(enc_mes, key)
print("Расшифрованное сообщение:", dec_mes)
