# Find the way with Maps :- 

lst = []
len = int(input("Enter length of the list : "))

for i in range(len):
    ele = int(input("Enter elements of the list : "))
    lst.append(ele)

print("The given List is :",lst)

def tripplet(lst):
    return lst * 3

data = list(map(tripplet,lst))
print("List containing tripplets of elements :",data)