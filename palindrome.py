def is_palindrome(word):
    return word == word[::-1]

n = int(input())

words = []
for _ in range(n):
    word = input()
    words.append(word)

palindrome = [word for word in words if is_palindrome(word)]

print(len(palindrome))
print(palindrome)
