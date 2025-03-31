def add(a,b):
  return a+b

def sub(a,b):
  return a-b

def mul(a,b):
  return a*b

def div(a,b):
  return a/b


whlie Ture:
  c=input("which one calculate do u want to choice("1-add,2-subtract,3-multiply,4-divide

if c in (1,2,3,4)
     try:
            num1 = float(input("Enter the first num: "))
            num2 = float(input("Enter the second num: "))
        except ValueError:
            print("Invalid input.Try again")
            continue

if c==1:
print(add(num1,num2))
elif c==2:
print(sub(num1,num2))
elif c==3:
print(mul(num1,num2)) 
elif c==4:
print(div(num1,num2))
 next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")

