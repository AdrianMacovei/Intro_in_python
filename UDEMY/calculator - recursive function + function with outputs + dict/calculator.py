from replit import clear
from art import logo
# am creat cate o fuctie pentru fiecare operatie
def add(n1, n2):
  return n1 + n2
    
def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2
# am creat un dictioanr cu toate operatiile matematice
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
# for loop va printa simbolurile-operatiile pe care userul le poate folosi
  for symbol in operations:
    print(symbol)v
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    # asa chemam functia specifica operatiei
    calculation_function = operations[operation_symbol]
    # dam argumentele functiei specifice operatiei alese
    answer = calculation_function(num1, num2) 
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    # adaugam conditia pentru a putea repeta calculul cu raspunsul deja aflat
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()
# recursion of a function - a chema o functie in propiul sau corp - creeaza un loop unde functia se ruleaza la infinit- like while loop
calculator()
