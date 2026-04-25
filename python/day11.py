words = {
        "apple":"りんご",
        "book":"本"
    }

while True:
  
    print("1:search word")
    print("2:add word")
    print("3:show all words")
    print("4:Exit")

    choice = input("choose a number:")

    if choice == "1":
        word = input("Enter a word:")
        if word in words:
            print(word, words[word])
        else:
            print("Not found.")

    elif choice == "2":
        word = input("Enter a word:")
        if word in words:
            print("Already exists.")
            print(word, words[word])
        else:
            meaning = input("Tell me the meaning of the word")
            words[word]=meaning
            print("added", word, words[word])

    elif choice == "3":
        for key in words:
            print(key, words[key])
                    
    elif choice == "4":
        print("GOOD BYE!")
        break