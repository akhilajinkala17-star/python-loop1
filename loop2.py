#1.
a=[1,2,3,4,5]
for i in a:
    print(i, "square:",i**2)

# 2.
def print_characters_with_index(text):
    for i in range(len(text)):
        print(f"Index {i}: {text[i]}")
print_characters_with_index("Hello")  

# 3.
a=[2,3,4,5,6,7,8,9,10]
sum=0
for i in a:
    if i%2==0:
        sum=sum+i
print(sum)

# 4.
d={"akki":1234, "chandu":1546, "abhi":4567}
for k,v in d.items():
    print(k, "=", v)

# 5.
numbers=[]
for i in range(1,101):
    numbers.append(i)
for i in numbers:
    if i%3==0 or i%5==0:
        print(i)




    





    
    

