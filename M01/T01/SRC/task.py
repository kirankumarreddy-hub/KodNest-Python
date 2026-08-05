'''n = int(input("enter the value"))

counter = 1
total = 0

while counter <= n:
    total += counter
    counter +=1

print("total:", total)'''

n = int(input("Enter a number"))
word = input("Enter a word")

for i in range(1,n+1):
    print(i)
for ch in word:
    print(ch)   