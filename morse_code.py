
#answer = "Hey Jude"

def decode(morse_code):
    MORSE_CODE_DICT = { 'A':'.-',     'B':'-...',
                        'C':'-.-.',   'D':'-..',      'E':'.',
                        'F':'..-.',   'G':'--.',      'H':'....',
                        'I':'..',     'J':'.---',     'K':'-.-',
                        'L':'.-..',   'M':'--',       'N':'-.',
                        'O':'---',    'P':'.--.',     'Q':'--.-',
                        'R':'.-.',    'S':'...',      'T':'-',
                        'U':'..-',    'V':'...-',     'W':'.--',
                        'X':'-..-',   'Y':'-.--',     'Z':'--..',
                        '1':'.----',  '2':'..---',    '3':'...--',
                        '4':'....-',  '5':'.....',    '6':'-....',
                        '7':'--...',  '8':'---..',    '9':'----.',
                        '0':'-----',  ', ':'--..--',  '.':'.-.-.-',
                        '?':'..--..', '/':'-..-.',    '-':'-....-',
                        '(':'-.--.',  ')':'-.--.-'}

    letter = morse_code.split()
    #sentence = '···· · −·−−   ·−−− ··− −·· ·'
    keys = list(MORSE_CODE_DICT.keys())
    vals = list(MORSE_CODE_DICT.values())

    # print(keys[vals.index('....')], " See it works here") # h
    # print(vals.index('....')) # 7
    # print(keys[7], " last call")

    for l in letter:
        print(keys[vals.index(l)])





# decode('···· · −·−−   ·−−− ··− −·· ·')


MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
   'C':'-.-.', 'D':'-..', 'E':'.',
   'F':'..-.', 'G':'--.', 'H':'....',
   'I':'..', 'J':'.---', 'K':'-.-',
   'L':'.-..', 'M':'--', 'N':'-.',
   'O':'---', 'P':'.--.', 'Q':'--.-',
   'R':'.-.', 'S':'...', 'T':'-',
   'U':'..-', 'V':'...-', 'W':'.--',
   'X':'-..-', 'Y':'-.--', 'Z':'--..',
   '1':'.----', '2':'..---', '3':'...--',
   '4':'....-', '5':'.....', '6':'-....',
   '7':'--...', '8':'---..', '9':'----.',
   '0':'-----', ', ':'--..--', '.':'.-.-.-',
   '?':'..--..', '/':'-..-.', '-':'-....-',
   '(':'-.--.', ')':'-.--.-'
}
def encryption(message):
   my_cipher = ''
   for myletter in message:
      if myletter != ' ':
         my_cipher += MORSE_CODE_DICT[myletter] + ' '
      else:
         my_cipher += ' '
      return my_cipher
# This function is used to decrypt
# Morse code to English


def decryption(message):
   message += ' '
   decipher = ''
   mycitext = ''
   for myletter in message:
      # checks for space
      if (myletter != ' '):
         i = 0
         mycitext += myletter
      else:
         i += 1
         if i == 2 :
            decipher += ' '
         else:
            decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(mycitext)]
            mycitext = ''
   return decipher

decryption('···· · −·−−   ·−−− ··− −·· ·')
