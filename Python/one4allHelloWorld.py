import time
import os

alphabet = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'á', 'à', 'â', 'ã', 'ä', 'ç', 'é', 'è', 'ê', 'ë', 'i', 'í', 'ì', 'î', 'ï', 'ó', 'ò', 'ô', 'õ', 'ö', 'ú', 'ù', 'û', 'ü',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', '<', '>', ';', ':','!', '@', '#', '$', '%', '&', '*', '-', '+', '_', '=']

hello_world = "Hello, World!"
hw_list = list(hello_world)

print_list = []
print_list_str = ''

for x in hw_list:
    print_list.append('*')
    
start = str(input("Aperte ENTER para começar"))

for letter in alphabet:
    for indice, x in enumerate(print_list):
        if print_list[indice].lower() != hw_list[indice].lower():
            print_list[indice] = letter
        else:
            if hw_list[indice].isupper():
                print_list[indice] = print_list[indice].upper()
    
    print_list_str = ''.join(print_list)
    
    print(print_list_str)
    time.sleep(0.25)
    
    if print_list_str == hello_world:
        break
    
    os.system('cls')

        
end = str(input(""))