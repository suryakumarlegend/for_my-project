#code by surya kumar
i=eval(input("enter your mark:"))
if i>=90:
    print("A+")
elif i>=80 and i<=89:
    print("A")
elif i>=70 and i<=79:
    print("B")
elif i>=60 and i<=69:
    print("C")
elif i>=50 and i<=59:
    print("D")
elif i<50:
    print("Fail")
else:
    print("invalid mark!")
