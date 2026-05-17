nums = [1,2,2,3,3,3]
k = 2
freq={}
for i in nums:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)
li=[]
for key,value in freq.items():
	if value>=k:
	    li.append(key)
print(li)
