import json
from nltk.util import trigrams
import collections
import re


def get_letters ():

    data_rinat = open('letters_rinat.json')
    data_vladimir = open('letters_vladimir.json')

    root_data = json.loads(data_rinat.readlines()[0]) + json.loads(data_vladimir.readlines()[0])
    # print (data)
    root_letters = list()
    root_trigrams = dict()
    for i in root_data:
        # current_index = i.index(root_data)
        get_clean_text = (re.split('\W+',((i['coverLetter']))))    #очистить текст
        # temp.append(list(trigrams(get_clean_text)))                #составить триграммы и добавить их в список
        # print(temp)

        for grams in list(trigrams(get_clean_text)):
            root_letters.append(' '.join(grams))

    return collections.Counter(root_letters)


def process_trigrams():
    sorted_list = get_letters()
    generated_letter = list()

    generated_letter.append('Hi')
    generated_letter.append("I")
    generated_letter.append("m")



    print (generated_letter)

    for i in range(150):
        maxFreq = 0;
        champion = None;
        print ('candidats: ')
        for j in sorted_list:
            trigram = j.split()

            # print (trigram)
            # print (trigram[0], " ", trigram[1])
            # print (trigram[0], ' ', generated_letter[-1])

            if ((trigram[1] == generated_letter[-1]) and (trigram[0] == generated_letter[-2])):
                # print (j)
                if (sorted_list[j] > maxFreq):
                    maxFreq = sorted_list[j]
                    champion = j
                    print ("\t",champion)

            # if not champion:
            #     print ('Can not processed.')
            #     break
        if not champion:
            print('Can not process')
            break
        else:
            print("\tchampion: " ," ", champion)
            # print((champion.split())[-1])
            generated_letter.append(champion.split()[-1])

        # print (" ".join(generated_letter))
                # print('\tchampion: ', (champion.split())[0])
                # print (type(champion[1]))
                # generated_letter.append(trigram[-1])

                # print(j)
            #     if (()()):

if __name__ == "__main__":
    process_trigrams()
