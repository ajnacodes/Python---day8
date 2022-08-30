from caesar_art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
characters = [' ', '!', '?', '.', ',', '_', '1', '2', '3', '4', '5', '6', '7','8','9','0','-','+','*','%','$','"',"'",';',':','(',')','@','$','&','/','>','<',
              '[',']','{','}','=','#','|']
reload_program = True
def alphabet_length(alphabet, shift):
    while len(alphabet) < shift:
        alphabet += alphabet


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1

    for letter in start_text:
        if letter in characters:
            position = characters.index(letter)
            end_text += characters[position]
        elif letter in alphabet:    
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position]

    print(f"The {cipher_direction}d text is: {end_text}")
    
while reload_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    alphabet_length(alphabet, shift)
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)


    reload = input("Do you want to restart the cipher program? Type 'yes' or 'no': ")
    if reload == "no":
        reload_program = False
        print("Goodbye!")

