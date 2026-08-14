'''n = int(input("enter the value"))

counter = 1
total = 0

while counter <= n:
    total += counter
    counter +=1

print("total:", total)'''

'''n = int(input("Enter a number"))
word = input("Enter a word")

for i in range(1,n+1):
    print(i)
for ch in word:
    print(ch) 

for i in range(10,0,-1):
    print(i)
print("True"or False)'''

'''def demo():
    print(10)
x = demo()
print(x)''' 

def display_study_hours():
    # Constraints: 1 ≤ study hours per day ≤ 12, 1 ≤ number of study days ≤ 7
    study_hours_per_day = 5   # Example value within range
    number_of_study_days = 6  # Example value within range

    total_hours = study_hours_per_day * number_of_study_days
    print("Total study hours:", total_hours)

# Function must be called exactly once
display_study_hours()
