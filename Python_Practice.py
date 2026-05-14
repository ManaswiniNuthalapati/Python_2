## CONDITIONAL STATEMENTS

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
  
# Write a program to check whether three sides can form a valid triangle.
a=3
b=4
c=5
if a+b>c and b+c>a and a+c>b:
  print("Valid triangle")
else:
  print("Not Valid")
  
# Write a program to determine the type of triangle based on side lengths.
a=4
b=5
c=6
if a==b==c:
  print("Equilateral")
elif a==b!=c or a==c!=b:
  print("Isosceles")
else:
  print("Scalene")
  
# Write a program to simulate ATM withdrawal functionality.
balance=5000
amount=2000
if amount<balance and amount%100==0:
  print("Transaction Successful")
  balance-=amount
  print(balance)
else:
  print("Insufficient balance")

# Write a Python program to perform arithmetic operations using if-elif conditions.
n1=10
n2=20
choice=int(input())
if choice==1:
  print(n1+n2)
elif choice==2:
  print(n1-n2)
elif choice==3:
  print(n1*n2)
elif choice==4:
    print(n1/n2)
else:
  print("Invalid")
  

## LOOPS
# Print 1 to N
n=10
for i in range(1,n):
  print(i,end=" ")
  
# Print N to 1
n=10
for i in range(n,0,-1):
  print(i,end=" ")
  
# Sum of first N numbers
n=5
total=0
for i in range(n):
  total+=i
print(total)

# Sum of even numbers
n=10
even_total=0
odd_total=0
for i in range(n):
  if i%2==0:
    even_total+=i
  else:
    odd_total+=i
print(even_total)
print(odd_total)

# Multiplication table
n=5
table=0
for i in range(1,11):
  table=n*i
  print(table)
  
# Reverse a number
n=12
rev=" "
for i in str(n):
  rev=i+rev
print(int(rev))

# Count digits
n=123456789
count=0
for i in str(n):
  count+=1
print(count)

# Sum digits
n=12345
total=0
for i in str(n):
  total+=int(i)
print(total)

# Palindrome number
n=121
temp=n
rev=0
while n>0:
  digit=n%10
  rev=rev*10+digit
  n=n//10
if rev==temp:
  print("Palindrome")
else:
  print("Not Palindrome")
  
n=121
rev=""
for i in str(n):
  rev=i+rev
if str(n)==rev:
  print("Palindrome")
else:
  print("Not Palindrome")
  
n=121
n_1=str(n)
rev=n_1[::-1]
if n_1==rev:
  print("Palindrome")
else:
  print("Not Palindrome")

# Armstrong number
n=153
temp=n
rev=0
while n>0:
  digit=n%10
  rev=rev+digit**3
  n=n//10
if rev==temp:
  print("Armstrong number")
else:
  print("Not Armstrong Number")
  
# Factorial
n=5
fact=1
for i in range(1,n+1):
  fact*=i
print(fact)

# Prime Number
n=14
for i in range(1,n):
  if n%i==0:
    is_prime="Prime"
  else:
    is_prime="Not Prime"
print(is_prime)

# Fibonacci series
n=20
a,b=0,1
print(a,end=" ")
for i in range(2,n+1):
  a,b=b,a+b
  print(a,end=" ")
  
# HCF
n1=12
n2=18
for i in range(n1,0,-1):
  if n1%i==0 and n2%i==0:
    print(i)
    
# Perfect Number
n=28
total=0
for i in range(1,n):
  if n%i==0:
    total+=i
if n==total:
  print("Perfect Number")
else:
  print("Not Perfect Number")
  
# LCM
n1=4
n2=6
greater=n1
while True:
  if greater%n1==0 and greater%n2==0:
    print(greater)
    break
  greater+=1
    
'''
Star Patterns
*
**
***
****
'''
n=5
for i in range(1,n+1):
  for j in range(i):
    print("*",end=" ")
  print()

'''
****
***
**
*
'''
n=5
for i in range(n,0,-1):
  for j in range(i):
    print("*",end=" ")
  print()

'''
   *
  ***
 *****
*******
'''  

n=5
for i in range(1,n+1):
  for j in range(n-i):
    print(" ",end="")
  for k in range(2*i-1):
    print("*",end="")
  print()
 
   
