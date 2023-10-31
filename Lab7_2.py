#2)	Полибианским квадратом (в начале пишется фамилия и имя студента, фраза для шифрования = любое словосочетание); 
polybius_square = {
    'Г': '11', 'Ж': '12', 'Е': '13', 'Г': '14', 'О': '15', 'Ж': '16', 'К': '21', 'И': '22', 'Б': '23', 'В': '24',
    'С': '25', 'Д': '26', 'У': '31', 'Ё': '32', 'Р': '33', 'З': '34', 'Й': '35', 'М': '36', 'А': '41', 'П': '42',
    'Т': '43', 'Ф': '44', 'Х': '45', 'Ц': '46', 'Ч': '51', 'Ш': '52','Щ': '53' , 'Ь':'54', 'Ы':'55', 'Ъ':'56', 'Э':'61',
    'Ю':'62', 'Я':'63', ' ':' '}

def encode(message):
    encoded_message = ''
    for char in message:
        char = char.upper()
        encoded_message += polybius_square.get(char, '')
    return encoded_message

def decode(encoded_message):
    decoded_message = ''
    num_chars = len(encoded_message)
    i = 0
    while i < num_chars:
        if encoded_message[i] == ' ':
            decoded_message += ' '
            i += 1
        else:
            char = ''
            if i < num_chars - 1:
                char = encoded_message[i:i + 2]
                i += 2
            else:
                char = encoded_message[i]
                i += 1
            for key, value in polybius_square.items():
                if value == char:
                    decoded_message += key
                    break
    return decoded_message

message = input("Введите сообщение для кодирования: ")
encoded_message = encode(message)
print("Закодированное сообщение: ", encoded_message)

decoded_message = decode(encoded_message)
print("Раскодированное сообщение: ", decoded_message)