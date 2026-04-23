animals={
    "dog":"犬",
    "cat":"猫",
    "bird":"鳥"
}
print("cat",animals["cat"])

fruits={
    "apple":"リンゴ"
}

fruits["banana"]="バナナ"
print(fruits)

items={}
items["pen"]="ペン"
items["book"]="本" 

print(items)

words={
    "red":"赤",
    "blue":"青",
    "green":"緑"
}
for key in words:
    print(key, words[key])

subjects={
    "English":"80",
    "math":"70",
    "science":"90"
}
for key in subjects:
    print(subjects[key])

scores={
    "English":85,
    "math":72,
    "science":90
}
for key in scores:
    if scores[key] >=80:
        print(key, scores[key])

numbers={
    "a":5,
    "b":12,
    "c":20,
    "d":8
}
for key in numbers:
    if numbers[key] >=10:
        print(key, numbers[key])

nums = {
    "x": 3,
    "y": 4,
    "z": 7,
    "w": 10
}
for key in nums:
    if nums[key] % 2 == 0:
        print(key, nums[key])

words = {
    "apple": "りんご",
    "book": "本",
    "study": "勉強する"
}
print("study" in words)

words = {
    "apple": "りんご",
    "book": "本",
    "study": "勉強する"
}

word = input("Enter a word")
if word in words:
    print(word, words[word])
else:
    meaning = input("Tell me the meaning of the word")
    words[word]=meaning
   
print(words)

words={}
word = input("Enter a word")
meaning = input("Tell me the meaning of the word")
words[word]=meaning
print(words)