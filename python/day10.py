words={
    "apple":"りんご",
    "book":"本",
}

print("1:search word")
print("2:add word")
print("3:show all words")

choose = input("choose a number:")

if choose == "1":
    word = input("Enter a word:")
    if word in words:
        print(word, words[word])
    else:print("Not found.")

if choose == "2":
    word = input("Enter a word")
    if word in words:
        print("Already exists.")
        print(word,words[word])
    else:
        meaning = input("Tell me the meaning of the word")
        words[word] = meaning
        print("Added", word, words[word])

if choose == "3":
    for key in words:
        print(key, words[key])
