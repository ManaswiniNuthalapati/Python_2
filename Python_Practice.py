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
