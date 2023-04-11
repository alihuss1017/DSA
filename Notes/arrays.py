expenses = [2200, 2350, 2600, 2130, 2190]

# In Feb, how many dollars you spent extra compare to January?
print(expenses[1] - expenses[0])

#Total expense in first three months
print(expenses[0] + expenses[1] + expenses[2])

#Find out if you spent exaactly 2000 dollars in any month

for n in expenses:
    if n == 2000:
        print("True")
    else:
        print("False")

#June just finished and expense is $1980. Add it to the list.
expenses.append(1980)
print(expenses)

#You returned an item that you bought in a month of April and got a refund of $200. Make a correction to the expense list.
expenses[3] -= 200
print(expenses)