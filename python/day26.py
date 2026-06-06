import json

FILE_NAME = "words.json"
BUCKUP_FILE_NAME = "words_backup.json"

def show_title():
    print("My vocabulary book")

def show_menu():
    print("1: Search word")
    print("2: Add word")
    print("3: Show all words")
    print("4: Delete word")
    print("5: Update word")
    print("6: Search by prefix")
    print("7: Backup words")
    print("8: Exit")

def main():
    words=load_words()
    show_title()

    while True:
        show_menu()
        choice = input("Choose a number: ").strip()

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
            search_by_prefix(words)
        elif choice == "7":
            buckup_words(words)
            print("Backup saved.")
        elif choice == "8":
            save_words(words)
            print("Saved. Good bye!")
            break
        else:
            print("Error")

def search_word(words):
    word = input("Enter a word: ").strip()

    if word == "":
        print("Please enter a word.")
        return
    if word in words:
        print("Found:",word, "=", words[word])
    else:
        print("Not found.")


def add_word(words):
    word = input("Enter a word: ").strip()

    if word == "":
        print("Word cannot be empty.")
        return

    if word in words:
        print("Already exists:", word, "=", words[word])
        return

    meaning = input("Tell me the meaning of the word: ").strip()

    if meaning == "":
        print("Meaning cannot be empty.")
        return

    words[word] = meaning
    save_words(words)
    print("Added:", word, "=", words[word])


def show_all_words(words):
    if len(words) == 0:
        print("No words.")
    else:
        print("Total words:", len(words))
        for key in sorted(words):
            print("- ", key, ":", words[key])

def delete_word(words):
    word = input("Enter a word: ").strip()
    if word == "":
        print("Please enter a word.")
        return
    if word in words:
        del words[word]
        save_words(words)
        print("Deleted:", word)
    else:
        print("Not found.")

def update_word(words):
    word=input("Enter a word:").strip()
    if word == "":
        print("Please enter a word.")
        return
    if word in words:
        meaning = input("Tell me the meaning of the word: ").strip()
        if meaning == "":
            print("Please enter a meaning.")
            return
        words[word]=meaning
        save_words(words)
        print("Updated", word, words[word])
    else:
        print("Not found.")

def search_by_prefix(words):
    prefix = input("Enter a prefix: ").strip()
    if prefix == "":
        print("Please enter a prefix.")
        return
    found = False

    for key in sorted(words):
        if key.startswith(prefix):
            print(key,":",words[key])
            found = True
    
    if found == False:
        print("Not found.")

def save_words(words):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(words, file, ensure_ascii=False, indent=4)

def buckup_words(words):
    with open(BUCKUP_FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(words, file, ensure_ascii=False, indent=4)

def load_words():

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return{
            "apple": "りんご",
            "book": "本"
        }
    

if __name__ == "__main__":
    main()