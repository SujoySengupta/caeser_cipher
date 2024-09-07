from flask import Flask, request, render_template

app = Flask(__name__)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def Ceaser(text_input, shift_input, direction_input):
    split_text = list(text_input)
    output_word = ''
    for letter in split_text:
        if letter in alphabet:
            index_pos = alphabet.index(letter)
            if direction_input in ['encode' , 'e']:
                caser_word = alphabet[(index_pos + shift_input) % 26]
            elif direction_input in ['decode' , 'd']:
                caser_word = alphabet[(index_pos - shift_input) % 26]
            output_word += caser_word
        else:
            output_word += letter
    return output_word

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        direction = request.form['direction'].lower()
        text = request.form['text']
        shift = int(request.form['shift'])
        result = Ceaser(text, shift, direction)
        return render_template('Ceaser_cipher.html', result=result)
    return render_template('Ceaser_cipher.html', result='')

if __name__ == '__main__':
    app.run(debug=True)
