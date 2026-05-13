# Even or odd
n=10
if n%2==0:
  print("Even")
else:
  print("Odd")
    
# Positive, negative, or zero
n=10
if n>0:
  print("Positive")
elif n==0:
  print("Zero")
else:
  print("Negative")
  
# Largest of 2 numbers
a,b=10,11
if a<b:
  print(b,"is Largest Number")
else:
  print(a,"is Largest Number")
  
# Largest of 3 numbers
a,b,c=10,4,12
if a>b and a>c:
  print(a,"Largest Number")
elif b>c and b>a:
  print(b, "Largest Number")
else:
  print(c, "Largest Number")
  
# Smallest of 3 numbers
a,b,c=10,4,12
if a<b and a<c:
  print(a,"Smallest Number")
elif b<c and b<a:
  print(b, "Smallest Number")
else:
  print(c, "Smallest Number")

# Divisible by 5 and 11
n=10
if n%5!=0 and n%11==0:
  print(n, "Not Divisible by 5 but Divisible by 11")
elif  n%5==0 and n%11!=0:
  print(n, "Divisible by 5 but not Divisible by 11")
else:
  print(n, "Divisible by 5 and 11")
  
# Leap year
n=2028
if (n%400==0) or (n%4==0 and n%100!=0):
  print("Leap Year")
else:
  print("Not Leap Year")
  
# Vowel or consonant
n="a"
vowels="aeiouAEIOU"
if n in vowels:
  print("vowel")
else:
  print("consonant")

# Alphabet, digit, or special character
n="@#"
if n.isalpha():
  print("Alphabet")
elif n.isdigit():
  print("Numbers")
else:
  print("special characters")

# Electricity bill calculation
'''
Write a Python program to calculate the electricity bill based on the number of units consumed.
The electricity charges are calculated according to the following slab rates:
Units Consumed	            Rate per Unit
First 100 units	            ₹1.5 per unit
Next 100 units (101–200)	₹2.5 per unit
Next 100 units (201–300)	₹4 per unit
Above 300 units	            ₹6 per unit
'''
units=int(input())
bill=0
if units<=100:
    bill=units*1.5
elif units<=200:
    bill=(100*1.5)+((units-100)*2.5)
elif units<=300:
    bill=(100*1.5)+(100*2.5)+((units-200)*4)
else:
    bill=(100+1.5)+(100*2.5)+(100*4)+((units-300)*6)
print(bill)

'''
Write a program to calculate the grade of a student based on marks entered by the user.
'''
n=70
if n>=90:
  print("A")
elif n>=80 and n<=89:
  print("B")
elif n>=70 and n<=79:
  print("C")
elif n>=60 and n<=69:
  print("D")
else:
  print("Fail")
  
  
'''Calculator Using Operators'''
num1=10
num2=5
operator=input()
match operator:
  case "+":
    print(num1+num2)
  case "-":
    print(num1-num2)
  case "*":
    print(num1*num2)
  case "/":
    if num2!=0:
      print(num1/num2)
  case "_":
    print("Invalid")
  
# Write a program to determine whether there is profit or loss based on cost price and selling price.
Cost_Price=500
Selling_price=650
if Selling_price>Cost_Price:
  print("Profit: ",Selling_price-Cost_Price)
elif Selling_price<Cost_Price:
  print("Loss: ",Selling_price-Cost_Price)
else:
  print("Neutral")