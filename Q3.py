# Find the Squares from the given List :-

lst = []
len = int(input("Enter length of the list : "))

for i in range(len):
    ele = int(input("Enter elements of the list : "))
    lst.append(ele)

print("The given List is :",lst)

def square(lst):
    return lst ** 2

data = list(map(square,lst))
print("List of squares of elements :",data)