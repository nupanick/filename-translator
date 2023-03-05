import sys
import translators as ts # uses bing by default

def main(argv):
    text_in = 'バニーラクス＆ミーアで Mister'
    text_out = ts.translate_text(text_in, from_language='ja', to_language='en')
    print(text_out) # 'Bunny Lux & Mia by Mister'

if __name__ == '__main__': 
    main(sys.argv)
