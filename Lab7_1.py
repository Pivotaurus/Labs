#Реализовать программу кодирования и декодирования Методом Цезаря(ключ = порядковый номер студента по списку группы, фраза для шифрования = любое словосочетание);
def caesar(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr(
                    (ord(char) + key - 1040) % 32 + 1040)
            else:
                result += chr(
                    (ord(char) + key - 1072) % 32 + 1072)
        else:
            result += char
    return result
text = input("Введите текст: ")
key = 5
encoded = caesar(text, key)
print("Зашифрованный текст:", encoded)

def decaesar(text, key):
    return caesar(text, -key)

decoded = decaesar(encoded, key)
print('Расшифрованный текст: ', decoded)