import time
import os

alphabet = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'á', 'à', 'â', 'ã', 'ä', 'ç', 'é', 'è', 'ê', 'ë', 'i', 'í', 'ì', 'î', 'ï', 'ó', 'ò', 'ô', 'õ', 'ö', 'ú', 'ù', 'û', 'ü',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', '<', '>', ';', ':','!', '@', '#', '$', '%', '&', '*', '-', '+', '_', '=']

hello_world = "Hello, World!"
hw_list = list(hello_world)

print_list = []
for x in hw_list:
    print_list.append('*')

start = str(input("Aperte ENTER para começar"))

for ix, x in enumerate(hw_list):
    for y in alphabet:
        print_list[ix] = y
        print_list_str = ''.join(print_list)
        os.system('cls')
        print(print_list_str)
        
        if hw_list[ix].lower() == y:
            if hw_list[ix].isupper():
                print_list[ix] = y.upper()
            break
        
        time.sleep(0.1)
            
end = str(input(""))