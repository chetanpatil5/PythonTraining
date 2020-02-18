inputstr=input("Enter the string to check Palindrome : ")
s=inputstr[::-1]

if s== inputstr:
    print("String : ",s,"is a Palindrome")
else:
     print("String : ",s,"is a NOT Palindrome")
