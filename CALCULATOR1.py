A=float(input("enter your first number:"))
B=input("enter the operation as\nMultiplication as '*'\nDivision as '/'\nAddition as '+'\nSubraction as '-' \nenter here :")
C=float(input("enter your second number:"))
if B=='+':
    E=A+C
    print(A,'+',C ,'=',E)
elif B=='-':
    F=A-C
    print(A,'-',C ,'=',F)
elif B=='*':
    G=A*C
    print(A,'*',C ,'=',G)
elif B=='/':
    H=A/C
    print(A,'/',C ,'=',H)
else:
    print("enter correctly")

