
# Python3 code to Check for 
# balanced parentheses in an expression
open_list = ["[","{","("]
close_list = ["]","}",")"]
stack = []
  
# Function to check parentheses
def stack_push(open_char):
  stack.insert(0,open_char)

def stack_pop():
  stack.pop(0)
  
def is_valid_parenthesis(string):
  for char in string:
    if char in open_list:
      stack_push(char)
    if char in close_list: 
      if len(stack) == 0:
        return False
      else:
        close_index = close_list.index(char)
        if stack[0] != open_list[close_index]:
          return False
        else:
          stack_pop()
  if len(stack) == 0:
    return True
if __name__ == "__main__":
  result = is_valid_parenthesis("{[]{()}}")
  
  if result:
    print("Balanced")
  else:
    print("Unbalanced")
  