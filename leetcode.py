# Palindrome Number
x=10
n=0
temp=n
while x>0:
    digit=x%10
    n=n*10+digit
    x=x//10
print(n)
if temp==n:
    print("Palindrome")
else:
    print("Not Palindrome")

# Plus One
digits = [1,2,3]
res=""
for i in digits:
  res+=str(i)
r=int(res)
re=r+1
t=[]
for i in str(re):
  t.append(int(i))
print(t)

# Add Digits
n=38
while n>=10:
  total=0
  while n>0:
    digit=n%10
    total+=digit
    n=n//10
  n=total
print(n)

# Subtract the Product and Sum of Digits of an Integer
n=234
product=0
add=0
while n>0:
  digit=n%10
  product*=digit
  add+=digit
  n=n//10
res=product-add
print(res)

# Max 69 Number
n=6699
n=str(n)
n=n.replace('6','9',1)
print(int(n))

# Power of Two
n=16
if n<=0:
  print(False)
else:
  while n>1:
    if n%2!=0:
      print(False)
    n=n//2
  else:
    print(True)
    
# FizzBuzz
n=3
res=[]
for i in range(1,n+1):
  if i%3==0 and i%5==0:
    res.append("FizzBuzz")
  elif i%3==0:
    res.append("Fizz")
  elif i%5==0:
    res.append("Buzz")
  else:
    res.append(str(i))
print(res)

# Simple Array Sum
def simpleArraySum(ar):
    total=0
    for i in ar:
        total+=i
    return total
  
# StairCase
def staircase(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end="")
        for k in range(i):
            print("#",end="")
        print()
        
# Compare the Triplets
