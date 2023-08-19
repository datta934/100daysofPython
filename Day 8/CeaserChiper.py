alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    new_letter = alphabet[new_position]
    cipher_text += new_letter
  print(f"The encoded text is {cipher_text}")

def decrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    new_letter = alphabet[new_position]
    cipher_text += new_letter
  print(f"The encoded text is {cipher_text}")

if direction == 'encode':
    encrypt(text, shift)
else:
   decrypt(text,shift)

# combine encrypt and decrypt functions - MD
def ceasar_chiper(direction, plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
      position = alphabet.index(letter)
      if direction == 'encode':
        new_position = position + shift_amount
      else:
        new_position = position - shift_amount
      new_letter = alphabet[new_position]
      cipher_text += new_letter
  print(f"The {direction}d text is {cipher_text}")

ceasar_chiper(direction,text,shift)
# Angela -->
def ceasar_chiper(direction, plain_text, shift_amount):
  cipher_text = ""
  if direction == "decode":
     shift_amount *= -1
  for letter in plain_text:
      position = alphabet.index(letter)
      new_position = position + shift_amount
      new_letter = alphabet[new_position]
      cipher_text += new_letter
  print(f"The {direction}d text is {cipher_text}")
