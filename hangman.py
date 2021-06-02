import os
import random


def read():
    words = []
    with open ('random_word.txt', 'r') as f:
        for line in f:
            words.append(str(line))
    return words


def choose_a_word(words_before):
    lenght = len(words_before)
    word_to_play_number = random.randrange(lenght)
    word_to_play = words_before[word_to_play_number]
    return word_to_play
    
def analyze_word(word_to_play):
        #Turning the word into a list so we can take off line spaces
        word_to_play_list =[]
        letters_in_word_to_play = []
        for letter in word_to_play:
                word_to_play_list.append(letter)
        word_to_play_list.pop()
        #We get a list without all repeated letters
        for letter in word_to_play_list:
            if letter not in letters_in_word_to_play:
                letters_in_word_to_play.append(letter)
        #We get the lenght of the list without all repeated letters
        letters_in_word_to_play_lenght = int(len(letters_in_word_to_play))

        return word_to_play_list, letters_in_word_to_play, letters_in_word_to_play_lenght

def displaying(full_word, word, len):
    #Creating list to display
    word_to_display = []
    for char in full_word:
        word_to_display.append("*")
    checkout = []
    while(len>0):
        letter = str(input("Escribe una letra... "))
        if letter in full_word and letter not in checkout:
            
            checkout.append(letter)
            len = len-1
            for index, eachchar in enumerate(full_word):
                if eachchar == letter:
                    word_to_display[index] = letter


        else:
            pass

        print("Let's play some Hangman!!\n")
        print(word_to_display)
        print("\nLetras restantes: " + str(len) + "\n")
        os.system("clear")


def run():
    words = read()
    word_to_play = choose_a_word(words)
    word_to_play_list, letters_in_word_to_play, letters_in_word_to_play_lenght = analyze_word(word_to_play)
    play = displaying(word_to_play_list,letters_in_word_to_play,letters_in_word_to_play_lenght)


if __name__ == '__main__':
    run()