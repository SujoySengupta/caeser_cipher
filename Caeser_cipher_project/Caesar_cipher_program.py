import art

not_complete = True 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# the function 'caeser' takes the arguments text, shift, and direction to give the resultant output. 
def caeser(text_input, shift_input, direction_input):
    split_text =list(text_input)
    output_word = ''
    for letter in split_text:
        if letter in alphabet:
            index_pos = alphabet.index(letter)
            if direction == 'encrypt' or direction_input  == 'e':
                caser_word = alphabet[(index_pos + shift_input) % 26] #the '% 26' makes the list wrap around itself.
                output_word += caser_word
            elif direction == "decrypt" or direction_input  == 'd':
                caser_word = alphabet[(index_pos - shift_input) % 26] #the '% 26' makes the list wrap around itself.
                output_word += caser_word
            else:
                print('Wrong input detected.')
                
        else:
            output_word += letter
    print(f'The resultant output is \'{output_word}\'.', end="")

print(art.logo)
while not_complete:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(text, shift, direction)
    consent = input("\nDo you want to restart the program? (Y/N): ").lower()
    if consent == "n":
        not_complete = False
        print("\nThank you for using the program. Goodbye!\n")
