colors = {
    "red": "赤",
    "blue": "青",
    "green": "緑"
}

print(colors["blue"])

animals ={
    "dog": "犬"
}

animals["cat"]= "猫"
print(animals)

words = {
    "apple": "リンゴ",
    "book": "本",
    "study": "勉強"
}

for key in words:
    print(key, words[key])


items ={}

items["pen"] = "ペン"
items["water"] = "水"

print(items)

scores = {
    "English": 85,
    "math": 72,
    "sciense": 90
}

for subject in scores:
    if scores[subject]>= 80:
        print(scores[subject] )

numbers = {
    "a": 5,
    "b": 12,
    "c": 20,
    "d": 8
}

for key in numbers:
    if numbers[key] >10:
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
print(words["study"])