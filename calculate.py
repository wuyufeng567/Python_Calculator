#Author: Wu Yufeng
#Date: 25/3/30
print("Select operation:") 
print("1.Add") 
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
a=int(input("Please enter the choice:"))
b=int(input("Please enter the first number:"))
c=int(input("Please enter the second number:"))
d=int(1)
if(a==1):
	d=b+c
elif(a==2):
	d=b-c
elif(a==3):
	d=b*c
else:
	d=b/c
print("The result is:")
print(d)
