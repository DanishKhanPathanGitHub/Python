a, b = 1,2
#here, 1,2 is actually a tuple, it's first element assigned to a and 2nd to b
#see below
a = 1,2
print(type(a))
#so what makes a tuple a tuple is , not ()
a,b,c = [1,2,3]
print(a,b,c)
d = {1:1.0, 2:2.0, 3:3.0, 4:4.0, 5:5.0}
for e in d.items():
    print(e, end=",")
print()
#so, we can unpack and assign the values of iterables to variables
a = [1,2,3,4,5,6]
a1,a2,a3 = a[0], a[1], a[2:]
print(a1,a2,a3)
s = {1,2,3,4,5}
#well now indexing won't work, so what's now?
#* means all the elements remaining
s1,s2,*s3, s4 = s
print(s1,s2,s3, s4)
string = 'ABCDEFG'
s1,s2,*s3, s4 = string
print(s1,s2,s3, s4)
#whatever we unpack, string, tuple or list, * will unpack it to list.
#we only allowed to use * only once, becoz if we use it 2 times it's ambiguous
#here ex. s1 *s2 s3 *s4, what it means, like s1 assigned 1st element, and how much
#to s2 and what s3 assigned to and what about s4, so it doesn't allowed
#this is amazingly crazy
s1, s2 = 'abc', 'bcde'
#imagine we have to create a string of all characters fro s1 and s2 without repeating
print({*s1, *s2})
#how handy is this 
d1 = {1:1.0, 2:2.0, 3:3.0}
d2 = {3:3.00001, 4:4.0}
d3 = {**d1, **d2}
#** to unpack bothe keys and values and only works with dictionaries obviously
#3 will be override by the last 3 key,as it appear in d2 here, 
# value for key 3 will be
print(d3)

#ehhe boy last thing - nested unpacking
weird = [1,2,3,4,5,'python']
a,b,*c,(d,e,*f) = weird
print(a,b,c,d,e,f)
#here,
#a=1, b =2, (d,e,*f)='python', and rest of would be c, as [3,4,5]
# d=p. e=y, f=[t, h, o, n]

