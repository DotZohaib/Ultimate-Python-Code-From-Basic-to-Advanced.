# Numbers (immutable)
x = 10
print("Initial x:", x, "ID:", id(x))
x = x + 1  # This creates a new object since integers are immutable
print("Modified x:", x, "ID:", id(x))

# Strings (immutable)
s = "hello"
print("Initial s:", s, "ID:", id(s))
s = s + " world"  # This creates a new string object
print("Modified s:", s, "ID:", id(s))


# Lists (mutable)
my_list = [1, 2, 3]
print("Initial list:", my_list, "ID:", id(my_list))
my_list.append(4)  # Changes the same list object
print("Modified list:", my_list, "ID:", id(my_list))



a = "i am zohaib and i am a software engineer"
print("Who is a software engineer : ", a)
z = a.replace("zohaib", "iqra")
print("Who is a software engineer : ", z)



name = str(input("Enter your name: "))
date = int(input("Enter date: "))

print(f'''
      Hello Good Evening {name} and Date is {date}
      ''')


value = "i am zohaib and i am a software engineer and  my original name is zohaib"
print(value.find("zohaib"))
print(value.rfind("zohaib"))


# String are immutable and list are mutable

        