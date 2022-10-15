print ('----------------------------------------------------------------------')
print("QUANTITY THAT WE CAN CALCULATE :-")
print ('----------------------------------------------------------------------')
print(" (1) electric field due to dipole at axial point\n(2) electric field  due to dipole at equotorial point")
a="electric field at to dipole at axial point"
b="electric field at to dipole at equotorial point\n"
print ('----------------------------------------------------------------------')
r=(10**9)*9
A=float(input("* Amount of charge = "))
B=float(input("* Distance between two charge = "))
print ('----------------------------------------------------------------------')
D=float(A*B)
f=B*B*B
E=((r*D)/f)
G=(2*E)
k=input("* What do you want to calculate :- (please write index number of quantity) = ")
print('----------------------------------------------------------------------')
if (k=='1'):print("• FILED AT AXIAL POINT = ",G)
if (k=='2'):print("• FILED AT EQUOTORIAL POINT = ",E)
