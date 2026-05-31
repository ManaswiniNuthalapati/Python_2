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
def compareTriplets(a, b):
    # Write your code here
    alice=0
    bob=0
    for i in range(len(a)):
        if a[i]>b[i]:
            alice+=1
        elif a[i]<b[i]:
            bob+=1
        else:
            pass
    res=[]
    res.append(alice)
    res.append(bob)
    return res
  
# A Very Big Sum
def aVeryBigSum(ar):
    res=0
    for i in ar:
        res+=i
    return res

# Plus Minus
def plusMinus(arr):
    pos=0
    neg=0
    zer=0
    for i in arr:
        if i>0:
            pos+=1
        elif i<0:
            neg+=1
        else:
            zer+=1
    print(f"{pos/n:.5f}")
    print(f"{neg/n:.5f}")
    print(f"{zer/n:.5f}")

# Migratory Birds
def migratoryBirds(arr):
    freq={}
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    max_count=max(freq.values())
    ans=[]
    for key in freq:
        if freq[key]==max_count:
            ans.append(key)
    return min(ans)

# Valid Perfect Square
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i=0
        sqr=False
        while i*i<=num:
            if i*i==num:
                sqr=True
                break
            i+=1
        return sqr

# Ugly Number
class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False
        while n%2==0:
            n=n//2
        while n%3==0:
            n=n//3
        while n%5==0:
            n=n//5
        return n==1
    
# Climbing Stairs
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        way_2=1
        way_1=2
        for i in range(3,n+1):
            curr=way_1+way_2
            way_2=way_1
            way_1=curr
        return way_1
    
# Count odd numbers in interval range
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high+1)//2-low//2
        
# Number of steps to reduce a number to zero
class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps=0
        while num>0:
            if num%2==0:
                num=num//2
            else:
                num=num-1
            steps+=1
        return steps
        
# Find numbers with even number of digits
class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0
        for n in nums:
            if len(str(n)) % 2 == 0:
                count += 1
        return count
    
# Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=s.lower()
        b=t.lower()
        if len(a)!=len(b):
            return False
        else:
            for ch in a:
                if a.count(ch)!=b.count(ch):
                    return False
                    break
            else:
                return True
        
# Reverse String
class Solution:
    def reverseString(self, s: list[str]) -> None:
        left=0
        right=len(s)-1
        while left<right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1

# Valid palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev=""
        for c in s:
            if c.isalnum():        
                rev+=c.lower()
        if rev == rev[::-1]:
            return True
        else:
            return False

# Two Sum
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        
# Games of Stones
def gameOfStones(n):
    if n%7==0 or n%7==1:
        return "Second"
    else:
        return "First"
 
# Stair Case
def staircase(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end="")
        for k in range(i):
            print("#",end="")
        print()

# Beautiful days at the movies
def beautifulDays(i, j, k):
    count=0
    for num in range(i,j+1):
        n=str(num)
        rev=int(n[::-1])
        if abs((num-rev)%k)==0:
            count+=1
    return count

# Repeat Strings
s="aba"
n=10
res=""
while len(res)<n:
    res+=s
total=res[:n]
count=0
for i in total:
    if i=="a":
        count+=1
print(count)

# The weakest rows in a matrix
mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]] 
k = 3
row=[]
idx=0
for li in mat:
    count=0
    for i in li:
        if i==1:
            count+=1
    row.append([count,idx])
    idx+=1
res=sorted(row)
print(res)
total=[]
for i in res:
    total.append(i[1])
print(total[:k])