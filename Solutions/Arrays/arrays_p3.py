# Create a list of all odd numbers between 1 and a max number, which is something to be taken from a user.
max = int(input("Insert a number "))
odd_nums = []

for n in range(1, max):
    if n%2 == 1:
        odd_nums.append(n)

print(odd_nums)