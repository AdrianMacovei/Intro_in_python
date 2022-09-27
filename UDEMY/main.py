alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1  # in decoding facem valoarea negativa pentru a se scadea inapoi la valoarea initiala a indexului
  for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char # this will help when user input a symbol/space/number
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

import art #code for import module
print(art.logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
if shift > 25:
    shift %= 25  # this code line will help when shift value is bigger than 25
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

restart = input('Do you want to start again the program (Y = yes) or (N = no):\n')
while restart == "Y" or restart == "y": # this will help to repeat infinitely when user type yes
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    restart = input('Do you want to start again the program (Y = yes) or (N = no):\n')