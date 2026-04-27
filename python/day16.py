import json


def search_word(words):
    word = input("Enter a word: ")
    if word in words:
        print(word, words[word])
    else:
        print("Not found.")


def add_word(words):
    word = input("Enter a word: ")
    if word in words:
        print("Already exists.")
        print(word, words[word])
    else:
        meaning = input("Tell me the meaning of the word: ")
        words[word] = meaning
        save_words(words)
        print("Added", word, words[word])


def show_all_words(words):
    for key in words:
        print(key, words[key])


def delete_word(words):
    word = input("Enter a word: ")
    if word in words:
        del words[word]
        save_words(words)
        print("Deleted", word)
    else:
        print("Not found.")

def update_word(words):
    word=input("Enter a word:")
    if word in words:
        meaning = input("Tell me the meaning of the word:")
        words[word]=meaning
        save_words(words)
        print("Updated", word, words[word])
    else:
        print("Not found.")

def save_words(words):
    with open("words.json", "w", encoding="utf-8") as file:
        json.dump(words, file, ensure_ascii=False, indent=4)


try:
    with open("words.json", "r", encoding="utf-8") as file:
        words = json.load(file)
except FileNotFoundError:
    words = {
        "apple": "りんご",
        "book": "本"
    }


while True:
    print()
    print("1: Search word")
    print("2: Add word")
    print("3: Show all words")
    print("4: Delete word")
    print("5: Update word")
    print("6: Exit")

    choice = input("Choose a number: ")

    if choice == "1":
        search_word(words)
    elif choice == "2":
        add_word(words)
    elif choice == "3":
        show_all_words(words)
    elif choice == "4":
        delete_word(words)
    elif choice == "5":
        update_word(words)
    elif choice == "6":
        save_words(words)
        print("Saved. Good bye!")
        break
    else:
        print("Error")