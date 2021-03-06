# -*- coding: utf-8 -*-
"""brailleWord.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jDwVJGFHVH1xMnAHqMxJbhGrIV8m93B8
"""

# coding: utf-8
# '‍্'

import os
import sys
from os.path import join

symbolToKar = {
    "অ": "", "আ": "া",
    "ই": "ি", "ঈ": "ী",
    "উ": "ু", "ঊ": "ূ",
    "এ": "ে", "ঐ": "ৈ",
    "ও": "ো", "ঔ": "ৌ", "ঋ": "ৃ"
}
# print(symbolToKar)

vol_spe = {
    "010100": "ই",
    "101001": "উ",
    "101010": "ও"
}

volume = {
    "100000": "অ", "001110": "আ",
    "001010": "ঈ", "110011": "ঊ",
    '000010111010': 'ঋ', "100010": "এ",
    "001100": "ঐ", "010101": "ঔ",
}

numbers = {
    '010110': '০', '100000': '১',
    '110000': '২', '100100': '৩',
    '100110': '৪', '100010': '৫',
    '110100': '৬', '110110': '৭',
    '110010': '৮', '010100': '৯',
}

english_numbers = {
    '010110': '0', '100000': '1',
    '110000': '2', '100100': '3',
    '100110': '4', '100010': '5',
    '110100': '6', '110110': '7',
    '110010': '8', '010100': '9',
}

punctuation = {
    '001001': '-', '010011': '|', '000001011001': '‘', '001011001000': '’',
    '000001011011': '[', '011000': ';', '011010': '!', '000011011011': '=',
    '001010001010': '*', '011011001000': ']', '010010': ':', '001011': '"',
    '011001': '“', '011011': '(', '010000': ',', '001100': '/', '000010': '$'

}

operator = {
'001001': '-', '001001': '-', '000011011011': '=', '001010001010': '*', '001110': '>', '110001': '<',
'010000': ',', '001100': '/', '011011': '(', '001101': '+', '100101': '%', '000110': '^', '010000': '.'
}

hosonto = {
    '011001': '?', '011011': ')', '001011': '্'
}

dot = {
    '010000': '.'
}

consonant = {
    "101000": "ক", "101101": "খ", "110110": "গ", "110001": "ঘ", "001101": "ঙ",
    "100100": "চ", "100001": "ছ", "010110": "জ", "101011": "ঝ", "010010": "ঞ",
    "011111": "ট", "010111": "ঠ", "110101": "ড", "111111": "ঢ", "001111": "ণ",
    "011110": "ত", "100111": "থ", "100110": "দ", "011101": "ধ", "101110": "ন",
    "111100": "প", "110100": "ফ", "110000": "ব", "111001": "ভ", "101100": "ম",
    "101111": "য", "111010": "র", "111000": "ল",
    "100101": "শ", "011100": "স", "111101": "ষ", "110010": "হ", "111110": "ক্ষ",
    "100011": "জ্ঞ", "110111": "ড়", "111011": "ঢ়", "010001": "য়", '010000011110': 'ৎ',
    "000100": "্‌", "000011": "ং", "000001": "ঃ", "001000": "ঁ",
}

twelveDots = {
    '000011011011': '=', '001010001010': '*', '000001011011': '[', '000001011001': '‘', '001011001000': '’', '011011001000': ']',
    '000010111010': 'ঋ', '010000011110': 'ৎ'
}

double_mapping = {
    '011001': '?', '001011': '"', "011011": '(', '010000': ','
}


twoLetters = {
    'কক': 'ক্ক', 'কট': 'ক্ট', 'কত': 'ক্ত', 'কর': 'ক্র', 'কল': 'ক্ল', 'গধ': 'গ্ধ', 'কস': 'ক্স', 'গন': 'গ্ন', 'গল': 'গ্ল',
    'ঘন': 'ঘ্ন', 'কব': 'ক্ব', 'কম': 'ক্ম',
    'কয': 'ক্য', 'কষ': 'ক্ষ', 'খয': 'খ্য', 'খর': 'খ্র', 'গব': 'গ্ব', 'গম': 'গ্ম', 'গয': 'গ্য', 'গর': 'গ্র', 'ঘয': 'ঘ্য',
    'ঘর': 'ঘ্র', 'ঙক': 'ঙ্ক', 'ঙখ': 'ঙ্খ',
    'ঙগ': 'ঙ্গ', 'ঙঘ': 'ঙ্ঘ', 'ঙ্ম': 'ঙ্ম', 'চচ': 'চ্চ', 'চছ': 'চ্ছ', 'চঞ': 'চ্ঞ', 'চয': 'চ্য', 'জজ': 'জ্জ',
    'জঝ': 'জ্ঝ', 'জঞ': 'জ্ঞ', 'জব': 'জ্ব', 'জয': 'জ্য',
    'জর': 'জ্র', 'ঞচ': 'ঞ্চ', 'ঞছ': 'ঞ্ছ', 'ঞজ': 'ঞ্জ', 'ঞঝ': 'ঞ্ঝ', 'টট': 'ট্ট', 'টয': 'ট্য', 'টর': 'ট্র', 'ডড': 'ড্ড',
    'ডয': 'ড্য', 'ডর': 'ড্র', 'ড়গ': 'ড়্গ',
    'ঢয': 'ঢ্য', 'ণট': 'ণ্ট ', 'ণঠ': 'ণ্ঠ', 'ণড': 'ণ্ড', 'ণঢ': 'ণ্ঢ', 'ণণ': 'ণ্ণ', 'ণব': 'ণ্ব', 'ণম': 'ণ্ম',
    'ণয': 'ণ্য', 'তত': 'ত্ত', 'তথ': 'ত্থ', 'তন': 'ত্ন',
    'তব': 'ত্ব', 'তম': 'ত্ম', 'তয': 'ত্য', 'তর': 'ত্র', 'থব': 'থ্ব', 'থয': 'থ্য', 'থর': 'থ্র', 'দদ': 'দ্দ', 'দধ': 'দ্ধ',
    'দব': 'দ্ব', 'দভ': 'দ্ভ', 'দম': 'দ্ম',
    'দয': 'দ্য', 'দর': 'দ্র', 'ধব': 'ধ্ব', 'ধয': 'ধ্য', 'ধর': 'ধ্র', 'নট': 'ন্ট', 'নঠ': 'ন্ঠ', 'নড': 'ন্ড', 'নত': 'ন্ত',
    'নথ': 'ন্থ', 'নদ': 'ন্দ', 'নধ': 'ন্ধ',
    'নন': 'ন্ন', 'নব': 'ন্ব', 'নম': 'ন্ম', 'নয': 'ন্য', 'প্ট': 'পট', 'পত': 'প্ত', 'পন': 'প্ন', 'পপ': 'প্প', 'পয': 'প্য',
    'পর': 'প্র', 'পল': 'প্ল', 'পস': 'প্স',
    'ফর': 'ফ্র', 'ফল': 'ফ্ল', 'বজ': 'ব্জ', 'বদ': 'ব্দ', 'বধ': 'ব্ধ', 'বব': 'ব্ব', 'বয': 'ব্য', 'বর': 'ব্র', 'বল': 'ব্ল',
    'ভয': 'ভ্য', 'ভর': 'ভ্র', 'মন': 'ম্ন',
    'মপ': 'ম্প', 'মফ': 'ম্ফ', 'মব': 'ম্ব', 'মভ': 'ম্ভ', 'মম': 'ম্ম', 'ময': 'ম্য', 'মর': 'ম্র', 'মল': 'ম্ল', 'যয': 'য্য',
    'রক': 'র্ক', 'রখ': 'র্খ', 'রগ': 'র্গ',
    'রঘ': 'র্ঘ', 'রচ': 'র্চ', 'রছ': 'র্ছ', 'রজ': 'র্জ', 'রঝ': 'র্ঝ', 'রট': 'র্ট', 'রড': 'র্ড', 'রণ': 'র্ণ', 'রত': 'র্ত',
    'রথ': 'র্থ', 'রদ': 'র্দ', 'রন': 'র্ন', 'রপ': 'র্প',
    'রফ': 'র্ফ', 'রব': 'র্ব', 'রভ': 'র্ভ', 'রম': 'র্ম', 'রয': 'র্য', 'রল': 'র্ল', 'রশ': 'র্শ', 'রষ': 'র্ষ', 'রস': 'র্স',
    'রহ': 'র্হ', 'লক': 'ল্ক', 'লগ': 'ল্গ', 'লট': 'ল্ট',
    'লড': 'ল্ড', 'লপ': 'ল্প', 'লব': 'ল্ব', 'লম': 'ল্ম', 'লয': 'ল্য', 'লল': 'ল্ল', 'শচ': 'শ্চ', 'শছ': 'শ্ছ', 'শন': 'শ্ন',
    'শব': 'শ্ব', 'শম': 'শ্ম', 'শয': 'শ্য',
    'শর': 'শ্র', 'শল': 'শ্ল', 'ষক': 'ষ্ক', 'ষট': 'ষ্ট', 'ষঠ': 'ষ্ঠ', 'ষণ': 'ষ্ণ', 'ষপ': 'ষ্প', 'ষফ': 'ষ্ফ', 'ষম': 'ষ্ম',
    'ষয': 'ষ্য', 'সক': 'স্ক', 'সখ': 'স্খ',
    'সট': 'স্ট', 'সত': 'স্ত', 'সথ': 'স্থ', 'সন': 'স্ন', 'সপ': 'স্প', 'সফ': 'স্ফ', 'সব': 'স্ব', 'সম': 'স্ম', 'সয': 'স্য',
    'সর': 'স্র', 'সল': 'স্ল', 'হণ': 'হ্ণ',
    'হন': 'হ্ন', 'হব': 'হ্ব', 'হম': 'হ্ম', 'হয': 'হ্য', 'হর': 'হ্র', 'হল': 'হ্ল'

}

english = {
    '100000': 'a', '110000': 'b', '100100': 'c', '100110': 'd', '100010': 'e',
    '110100': 'f', '110110': 'g', '110010': 'h', '010100': 'i', '010110': 'j',
    '101000': 'k', '111000': 'l', '101100': 'm', '101110': 'n', '101010': 'o',
    '111100': 'p', '111110': 'q', '111010': 'r', '011100': 's', '011110': 't',
    '101001': 'u', '111001': 'v', '010111': 'w', '101101': 'x', '101111': 'y',
    '101011': 'z',
}
'''
#print(twoLetters)k
#print(twoLetters.get('দব'))
'''
threeLetters = {
    'কটর': 'ক্ট্র', 'কষণ': 'ক্ষ্ণ', 'কষম': 'ক্ষ্ম', 'কষয': 'ক্ষ্য', 'গধয': 'গ্ধ্য', 'গনয': 'গ্ন্য', 'গরয': 'গ্র্য',
    'ঙকত': 'ঙ্‌ক্ত', 'ঙকয': 'ঙ্ক্য', 'ঙকষ': 'ঙ্ক্ষ',
    'ঙখয': 'ঙ্খ্য', 'ঙগয': 'ঙ্গ্য', 'ঙঘয': 'ঙ্ঘ্য', 'চছব': 'চ্ছ্ব', 'জজব': 'জ্জ্ব', 'ণঠয': 'ণ্ঠ্য',
    'ণডয': 'ণ্ড্য', 'ণডর': 'ণ্ড্র', 'ততব': 'ত্ত্ব',
    'ততয': 'ত্ত্য', 'তময': 'ত্ম্য', 'তরয': 'ত্র্য', 'দদব': 'দ্দ্ব', 'দভর': 'দ্ভ্র', 'দরয': 'দ্র্য', 'নটর': 'ন্ট্র',
    'নডর': 'ন্ড্র', 'নতব': 'ন্ত্ব', 'নতয': 'ন্ত্য', 'নতর': 'ন্ত্র',
    'নদয': 'ন্দ্য', 'নদব': 'ন্দ্ব', 'নদর': 'ন্দ্র', 'নধয': 'ন্ধ্য', 'নধর': 'ন্ধ্র', 'পরয': 'প্র্য', 'মপর': 'ম্প্র',
    'মভর': 'ম্ভ্র', 'রকয': 'র্ক্য', 'রগয': 'র্গ্য', 'রঘয': 'র্ঘ্য',
    'রচয': 'র্চ্য', 'রজয': 'র্জ্য', 'রজঞ': 'র্জ্ঞ', 'রণয': 'র্ণ্য', 'রতয': 'র্ত্য', 'রথয': 'র্থ্য', 'রবয': 'র্ব্য',
    'রময': 'র্ম্য', 'রশয': 'র্শ্য', 'রষয': 'র্ষ্য', 'রহয': 'র্হ্য',
    'রগর': 'র্গ্র', 'রতম': 'র্ত্ম', 'রতর': 'র্ত্র', 'রতস': 'র্ৎস', 'রদব': 'দ্ব', 'রদর': 'র্দ্র', 'রধব': 'র্ধ্ব',
    'রশব': 'র্শ্ব', 'ষকর': 'ষ্ক্র', 'ষটয': 'ষ্ট্য',
    'ষটর': 'ষ্ট্র', 'ষঠয': 'ষ্ঠ্য', 'ষপর': 'ষ্প্র', 'সতয': 'স্ত্য', 'সতর': 'স্ত্র', 'সথয': 'স্থ্য', 'সপর': 'স্প্র'
}

fourLetters = {
    'কষময': 'ক্ষ্ম্য', 'নতরয': 'ন্ত্র্য',
}

bracket_count = 0
numeral_sign = '001111'
capital_sign = '000001'

from collections import defaultdict

dd = defaultdict(list)

for d in (vol_spe, volume, punctuation, consonant, hosonto, dot):  # you can list as many input dicts as you want here
    for key, value in d.items():
        dd[key].append(value)




def getCharFromDoubbleMap(letters, position):
    char = letters[position]
    length = len(letters)
    global bracket_count

    if char == '011001':
        if position+1 == length:
            return '?'
        else:
            return '“'
    elif char == '001011':
        if position+1 == length or letters[i+1] in punctuation.keys():
            return '"'
        else:
            return '্'
    elif char == '011011':
        if bracket_count == 1:
            bracket_count = 0
            return ')'
        else:
            bracket_count += 1
            return '('

    elif char == '010000':
        if position + 1 == length or length > 3:
            return ','
        else:
            return '.'



def englishTextProcess(letters):
    length = len(letters)
    num = False
    toUpper = False
    i = 0
    text = ''

    while i < length:
        if letters[i] == numeral_sign:
            num = True
        elif num == True and letters[i] in english_numbers:
            text += english_numbers.get(letters[i])[0]

        elif letters[i] == capital_sign and i+1 < length and letters[i+1] == capital_sign:
            num = False
            toUpper = True
            i += 1
        elif letters[i] == capital_sign and i+1 < length:
            num = False
            text += english.get(letters[i+1])[0]

        elif letters[i] in operator:
            text += operator.get(letters[i])[0]
        elif letters[i] in punctuation:
            text += operator.get(letters[i])[0]

        elif i+1 < length and letters[i] + letters[i+1] in twelveDots:
            text += twelveDots.get(letters[i] + letters[i+1])[0]

        else:
            text += letters[i]

        i += 1

    text += ' '
    if toUpper == True:
        text.upper()

    return text









def banglaTextProcess(letters):

    length = len(letters)
    num = False
    i = 0
    text = ''
    global bracket_count
    hos = hosonto.get('001011')[0]

    while i < length:
        if num and letters[i] in operator.keys():
            if letters[i] == '011011' and bracket_count == 0:
                text += '('
                bracket_count += 1
            elif letters[i] == '011011' and bracket_count == 1:
                text += ')'
                bracket_count = 0
            else:
                text += operator.get(letters[i])[0]
            #print('num false')

        elif num and letters[i] in numbers.keys():
            text += numbers.get(letters[i])[0]

        elif num and (letters[i] not in operator.keys() or letters[i] in numbers.keys()):
            if i+1 < length and letters[i] == '001010' and letters[i+1] == '001010':
                text += operator.get(letters[i] + letters[i+1])[0]

            elif letters[i] == '000011' and letters[i+1] == '011011':
                text += operator.get(letters[i] + letters[i+1])[0]

            elif letters[i] == '000001' and letters[i+1] == '011011':
                text += '['

            elif letters[i] == '011011' and letters[i+1] == '000001':
                text += ']'

            i += 1
        elif not num:
            if i == 0 and letters[i] == numeral_sign:
                num = True

            elif letters[i] == numeral_sign and (letters[i - 1] in punctuation.keys() or letters[i - 1] == dot):
                num = True


            else:
                if i+1 < length and (letters[i] + letters[i+1]) in twelveDots.keys():
                    text += twelveDots.get(letters[i] + letters[i+1])[0]
                    i += 1
                elif letters[i] in double_mapping.keys():
                    text += getCharFromDoubbleMap(letters, i)
                    i += 1

                elif letters[i] == '000100' and i + 2 < length:

                    text += dd.get(letters[i + 1])[0] + hos + dd.get(letters[i + 2])[0]
                    i += 2
                    #print(2)
                    #print(hos)



                elif letters[i] == '000101' and i + 4 < length:
                    #joint = ''
                    joint = dd.get(letters[i + 1])[0] + dd.get(letters[i + 2])[0] + dd.get(letters[i + 3])[0] + dd.get(
                        letters[i + 4])[0]
                    if joint in fourLetters.keys():
                        for key, value in fourLetters.items():
                            if joint == key:
                                text += dd.get(letters[i + 1])[0] + hos + dd.get(letters[i + 2])[0] + hos + \
                                        dd.get(letters[i + 3])[0] + hos + dd.get(letters[i + 4])[0]
                                i += 4
                                #print('4')
                                break

                    else:
                        # joint = dd.get(letters[i + 1]) + dd.get(letters[i + 2]) + dd.get(letters[i + 3])

                        text += dd.get(letters[i + 1])[0] + hos + dd.get(letters[i + 2])[0] + hos + \
                                dd.get(letters[i + 3])[0]
                        i += 3



                else:

                    for k, v in dd.items():
                        if letters[i] == k:
                            text += v[0]

                            break

                num = False

        i += 1
    text += ' '
    return text


# for f in uploaded.keys():
# file = open(f, 'r')
if __name__ == '__main__':

    path_braille_code = 'G:\\5 th semester\\spl2\\DataFrom Online'
    braille_code = os.listdir(path_braille_code)
    count = 0
    bangla = False
    english = False




    path_out_text = 'G:\\5 th semester\\spl2\\outputOnline'

    lang = input("select language: bangla or english ? ")
    if lang.find('b') != -1:
        bangla = True
    elif lang.find('e') != -1:
        english = True

    else:
        print()
        sys.exit('invalid input')

    for iFile in braille_code:
        file = open(join(path_braille_code, iFile), 'r', )
        if iFile.lower().endswith(('.txt', '.doc', '.docx')):
          pass
        else:
            sys.exit('invalid file type')

        lines = file.readlines()
        text = ''
        for line in lines:
            words = line.split(' space ')
            # print(words)
            for word in words:
                letters = word.split(' ')
                if bangla == True:
                    text += banglaTextProcess(letters)
                elif english == True:
                    text += englishTextProcess(letters)
            text += '\n'


        count += 1
        #print(text)

    #length = len(text)
    # for i in range(length):
        i = 0
        if bangla:
            while i < len(text):
                #print(i, text[i])
                if text[i] in vol_spe.values() and i > 0 and text[i-1] == '100000':
                    text = text[:i-1] + text[i:]
                elif text[i] in symbolToKar.keys() and i > 0 and text[i-1] in consonant.values():
                    text = text[:i] + symbolToKar.get(text[i]) + text[i + 1:]

                i += 1

        out = open('G:\\5 th semester\\spl2\\DataFrom Online\\out' + str(count) + '.txt', 'w', encoding='utf-8', errors='ignore')
        out.write(text)
        out.close()
        file.close()
        print(text)

    output = open('new.txt', 'w')
#print(twoLetters.get('দব'))

we = {1: 'e', 2: 'r', 4: 't'}
q = we.get(2) + we.get(4)
