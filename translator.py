import sys
from translate import Translator

# get args
text_file = sys.argv[1]
language = sys.argv[2]

translator = Translator(to_lang=language)

try:
    with open(f'./{text_file}', encoding="utf8", mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open(f'./{language}-{text_file}', mode='w') as my_file2:
            my_file2.write(translation)
except FileNotFoundError as e:
    print('Check again the file path!')