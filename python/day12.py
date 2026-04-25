def search_word(words):
    word = input("Enter a word")
    if word in words:
        print(word, words[word])
    else:
        print("Not found")

def add_word(words):
    word = input("Enter a word")
    if word in words:
        print("Already exists.")
        print(word, words[word])
    else:
        meaning = input("Tell me the meaning of the word:")
        words[word]=meaning
        print("Added", word, words[word])

def show_all_words(words):
    for key in words:
        print(key, words[key])

def delete_word(words):
    word = input("Enter a word")
    if word in words:
        del words[word]
        print("Deleted", word)
    else:
        print("Not found")

words = {
    "apple":"りんご",
    "book":"本"
}

while True:
    print("1:search word")
    print("2:add word")
    print("3:show all words")
    print("4:delete word")
    print("5:Exit")

    choice = input("choose a number:")

    if choice == "1":
        search_word(words)
    elif choice == "2":
        add_word(words)
    elif choice == "3":
        show_all_words(words)
    elif choice == "4":
        delete_word(words)
    elif choice == "5":
        print("Good bye!")
        break