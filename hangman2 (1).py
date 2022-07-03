word=input("enter a word")
number_of_guesses=5
def replace_letter_with_underscore(word):
    num_of_letters=len(word)
    x=""
    for number in range(num_of_letters):
        x+="_"
    return x
guess_word=replace_letter_with_underscore(word)
print(guess_word)

def check_letter_exists_in_word(inputted_letter):
#    print(inputted_letter)
    for letter in word:
#        print("letter "+letter)
        if letter==inputted_letter:
#            print("True")
            return True
    global number_of_guesses
    number_of_guesses-=1
    return False
#print(check_letter_exists_in_word(letter))
def replace_underscore_with_inputted_letter(inputted_letter):
    for index, letter in enumerate(word):
        if letter==inputted_letter:
            global guess_word
            guess_word_as_a_list=list(guess_word)
            guess_word_as_a_list[index]=inputted_letter
            guess_word=''.join(guess_word_as_a_list)
            return guess_word
            
            
while number_of_guesses!=0:
    inputted_letter=input("Please enter a letter: ")
#    inputted_letter="t"
#    print("the letter e")
    if check_letter_exists_in_word(inputted_letter):
        print(replace_underscore_with_inputted_letter(inputted_letter))
    else:
        print("you have "+str(number_of_guesses)+" guesses left")
    if guess_word==word:
        print("you have won")
        break
    if number_of_guesses==0:
        print("You have lost")
