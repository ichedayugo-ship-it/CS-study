# 1. 1から5まで表示
for i in range(1, 6):
    print(i)

# 2. 1から10までの偶数
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# 3. 1から10までの奇数
for i in range(1, 11):
    if i % 2 != 0:
        print(i)

# 4. 1から20までの3の倍数
for i in range(1, 21):
    if i % 3 == 0:
        print(i)

# 5. 1から10までの合計
total = 0
for i in range(1, 11):
    total = total + i
print(total)