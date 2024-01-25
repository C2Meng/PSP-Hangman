import random

categories_dict = {
    "easy_categories": ["animals", "fruits", "colors", "numbers"],
    "intermediate_categories": ["countries", "occupations", "sports", "food"],
    "difficult_categories": ["python", "html", "css"],
    "expert_categories": ["data science", "cybersecurity", "software engineering", "game development"]
}

# Dictionary of lists for each category
categories_lists = {
    "animals": ["hippopotamus", "rhinoceros", "penguin", "elephant", "giraffe", "flamingo"],
    "fruits": ["pineapple", "raspberry", "watermelon", "blackberry", "kiwi", "guava"],
    "colors": ["red", "orange", "yellow", "green", "blue", "indigo", "violet"],
    "numbers": ["twelve", "three", "eleven", "nine", "ten", "fifteen"],
    "countries": ["MALAYSIA", "SINGAPORE", "PHILIPPINES", "BRUNEI", "THAILAND", "VIETNAM"],
    "occupations": ["DENTIST", "NURSE", "PHARMACIST", "PHYSICIAN", "ENGINEER", "THERAPIST"],
    "sports": ["SKIING", "VOLLEYBALL", "ARCHERY", "SNOOKER", "ICE HOCKEY", "MARTIAL ARTS"],
    "food": ["CHOCOLATE MOUSSE", "DIM SUM", "ICE CREAM", "HOT DOG", "FRENCH FRIES", "ROTI CANAI"],
    "python": ["Problem solving", "Programming", "Strings", "Lists", "Tuples", "Dictionaries"],
    "html": ["HyperText Markup Language", "Web development", "World wide web", "headings", "paragraph", "hyperlink"],
    "css": ["Cascading style sheets", "layout", "appearance", "styles", "fonts", "colors"],
    "data science": ["Machine Learning", "Deep Learning", "Data management", "Database", "Data Visualization", "Data Mining"],
    "cybersecurity": ["Cryptography", "Firewall", "Hacking", "Cloud Security", "Encryption And Decryption", "Blockchain"],
    "software engineering": ["Software Development Life Cycle", "Debugging", "Software Architecture", "Software Maintenance", "User Interface And User Experience", "Quality Assurance"],
    "game development": ["Graphics and Animation", "Virtual Reality", "Augmented Reality", "Multiplayer", "Three Dimensions", "Game Physics"]
}


def choose_category(categories_list):
    while True:
        chosen_category = input(f"Please choose a category from {categories_list}: ").lower()

        if chosen_category in categories_list:
            break
        else:
            print("Invalid category, please choose from the list given.")

    return chosen_category


def random_word(category):
    return random.choice(categories_lists[category])


def guess_word(word):
    chosen_word = ["_" if letter.isalpha() else " " for letter in word]

    while "_" in chosen_word:
        print("\nYour word is:\n", " ".join(chosen_word))

        while True:
            guessed_letter = input("Enter a letter from a-z: ").lower()

            if len(guessed_letter) == 1 and guessed_letter.isalpha():
                break
            else:
                print("\nInvalid input. Please enter a single alphabetical character.\n")

        if guessed_letter in word:
            for i in range(len(word)):
                if word[i] == guessed_letter:
                    chosen_word[i] = guessed_letter

            print("\nGood guess")
        else:
            print("\nIncorrect guess. Try again.")

    print(" ".join(chosen_word))
    print("\nHi, nice to meet you. You are my best friend now >.0\n")


def continue_game():
    while True:
        cont = input("Would you like to continue to be my friend and try to confess to me? Enter yes/no: \n").lower()

        if cont == "yes":
            print("You are qualified to pursue me now, show me your effort!\n")
            break
        elif cont == "no":
            print("You can't deny to be my friend, syntax error!\n")
        else:
            print("Invalid command bruhhh.\n")

    return cont


def main():
    global cat1
    cat1 = choose_category(categories_dict["easy_categories"])
    word1 = random_word(cat1)
    guess_word(word1)
    global cont1
    cont1 = continue_game()


def choose_category2():
    if cont1 == "yes":
        category2 = choose_category(categories_dict["intermediate_categories"])
        return category2


def random_word2(category2):
    return random.choice(categories_lists[category2])


def guess_word2(word2):
    chosen_word2 = ["_" if letter.isalpha() else " " for letter in word2]

    while "_" in chosen_word2:
        print("\nYour word is:\n", " ".join(chosen_word2))

        while True:
            guessed_letter2 = input("Enter a letter from a-z: ").upper()

            if len(guessed_letter2) == 1 and guessed_letter2.isalpha():
                break
            else:
                print("\nInvalid input. Please enter a single alphabetical character.\n")

        if guessed_letter2 in word2:
            for i in range(len(word2)):
                if word2[i] == guessed_letter2:
                    chosen_word2[i] = guessed_letter2

            print("\nGood guess!\n")
        else:
            print("\nIncorrect guess. Try again.")

    print(" ".join(chosen_word2))
    print("You are my partner now, and I am looking forward to the engagement >.<\n")


def continue_game2():
    while True:
        cont2 = input("Would you like to continue our relationship and give me a promise? Enter yes/no: \n").lower()
        if cont2 == "yes":
            break
        elif cont2 == "no":
            print("You can't reject to make a proposal of marriage, syntax error!\n")
        else:
            print("Invalid command bruhhhhhhhhhh.\n")

    return cont2


def main2():
    global cat2, cont2
    cat2 = choose_category2()
    word2 = random_word2(cat2)
    guess_word2(word2)
    cont2 = continue_game2()


def choose_category3():
    if cont2 == "yes":
        category3 = choose_category(categories_dict["difficult_categories"])
        return category3


def random_word3(category3):
    return random.choice(categories_lists[category3])


def guess_word3(word3):
    chosen_word3 = ["_" if letter.isalpha() else " " for letter in word3]

    while "_" in chosen_word3:
        print("\nYour word is:\n", " ".join(chosen_word3))

        while True:
            guessed_letter3a = input("Enter a letter from a-z: ").capitalize()
            guessed_letter3 = input("Retype your letter, don't ask why: ").lower()

            if len(guessed_letter3a) == 1 and guessed_letter3a.isalpha() and len(guessed_letter3) == 1 and guessed_letter3.isalpha():
                break
            else:
                print("\nInvalid input. Please enter a single alphabetical character.\n")

        if guessed_letter3a in word3 or guessed_letter3 in word3:
            for i in range(len(word3)):
                if word3[i] == guessed_letter3a:
                    chosen_word3[i] = guessed_letter3a
                elif word3[i] == guessed_letter3:
                    chosen_word3[i] = guessed_letter3

            print("\nGood guess")
        else:
            print("\nIncorrect guess. Try again.")

    print(" ".join(chosen_word3))
    print("\nYes! I do! Please love me forever ^ 3^\n")


def continue_game3():
    while True:
        cont3 = input("Would you like to continue your entire life with me? Enter yes/no: \n").lower()
        if cont3 == "yes":
            break
        elif cont3 == "no":
            print("You can't deny the opportunity to stay with me till we died, syntax error!\n")
        else:
            print("Invalid command bruhhhhhhhhhh.\n")

    return cont3


def main3():
    global cat3, cont3
    cat3 = choose_category3()
    word3 = random_word3(cat3)
    guess_word3(word3)
    cont3 = continue_game3()


def choose_category4():
    if cont3 == "yes":
        category4 = choose_category(categories_dict["expert_categories"])
        return category4


def random_word4(category4):
    return random.choice(categories_lists[category4])


def guess_word4(word4):
    chosen_word4 = ["_" if letter.isalpha() else " " for letter in word4]

    while "_" in chosen_word4:
        print("\nYour word is:\n", " ".join(chosen_word4))

        while True:
            guessed_letter4a = input("Enter a letter from a-z: ").capitalize()
            guessed_letter4 = input("Retype your letter, don't ask why: ").lower()

            if len(guessed_letter4a) == 1 and guessed_letter4a.isalpha() and len(guessed_letter4) == 1 and guessed_letter4.isalpha():
                break
            else:
                print("\nInvalid input. Please enter a single alphabetical character.\n")

        if guessed_letter4a in word4 or guessed_letter4 in word4:
            for i in range(len(word4)):
                if word4[i] == guessed_letter4a:
                    chosen_word4[i] = guessed_letter4a
                elif word4[i] == guessed_letter4:
                    chosen_word4[i] = guessed_letter4

            print("\nGood guess")
        else:
            print("\nIncorrect guess. Try again.")
    print("\n\I LOVE YOU 3000, WE FINALLY WENT TO HEAVEN HAND BY HAND.\n")


def main4():
    global cat4, cont4
    cat4 = choose_category4()
    word4 = random_word4(cat4)
    guess_word4(word4)


# Run the main functions for advanced levels
def main1():
  main()
  main2()
  main3()
  main4()

main1()

print("THE MORAL OF THE STORY: \n WHY ARE YOU STILL SINGLE?")
