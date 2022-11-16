stack = []

string = "3.5 2 + 4.25 4 x - 15 20"
string_repace = string.replace("x","*")


operations = ["+", "-","*","/" ]

def push(number):
  stack.insert(0,number)
  
def pop():
  return stack.pop(0)
list_str = string_repace.split()
# print(list_str)
for i in list_str:
  if i not in operations:
    push(i)
  else:
    number_1 = pop()
    number_2 = pop()
    total = eval(str(number_2) + i + str(number_1))
    push(total)
  print(stack)
 
print(stack)