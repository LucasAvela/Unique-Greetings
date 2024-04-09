import time
import os

alphabet = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'á', 'à', 'â', 'ã', 'ä', 'ç', 'é', 'è', 'ê', 'ë', 'i', 'í', 'ì', 'î', 'ï', 'ó', 'ò', 'ô', 'õ', 'ö', 'ú', 'ù', 'û', 'ü',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', '<', '>', ';', ':','!', '@', '#', '$', '%', '&', '*', '-', '+', '_', '=']

hello_world = "Hello, World!"
hw_list = list(hello_world)

print_list = []

start = str(input("Aperte ENTER para começar"))

for x in hw_list:
    for y in alphabet:
        if x.lower() == y:
            if x.isupper():
                print_list.append(y.upper())
            else:
                print_list.append(y.lower())
            break
        else:
            os.system('cls')
            for i in print_list:
                print(i)
            print(y)
        time.sleep(0.1)

os.system('cls')

for i in print_list:
    print(i)

end = str(input(""))