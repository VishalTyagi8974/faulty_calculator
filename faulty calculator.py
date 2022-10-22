# faulty calculator
# 45*3=555, 56+9=77, 56/6=4

a=int(input("put first number"))
b=input("put your mathematical sign")
c=int(input("put second number"))

if a==45 and b== "*" and c==3 :
    print(555)
elif a==56 and b== "+" and c==9 :
    print(77)
elif a==56 and b== "/" and c==6 :
    print(4)

# now a normal calculator

elif b=="+":
    print(a+c)
elif b=="-":
    print(a-c)
elif b=="*":
    print(a*c)
elif b=="/":
    print(a/c)
else:
    print("invalid input")

