print('\n')
print('''QUANTITY THAT WE CAN CALCULATE :-\n\na)electric field at to dipole at axial point\nb)electric field at to dipole at equotorial point''')
a="electric field at to dipole at axial point"
b="electric field at to dipole at equotorial point\n"
print('-------------------------------------------------------------------------------------------------------------------------')
#k=input("WHAT DO YOU WANT TO CALCULATE :- (please write index number of quantity)\n")
r=(10**9)*9
A=float(input("* Amount of charge = "))
B=float(input("* Distance between two charge = "))
print('-------------------------------------------------------------------------------------------------------------------------')
D=float(A*B)
f=B*B*B
E=((r*D)/f)
G=(2*E)
k=input("* What do you want to calculate :- (please write index number of quantity) = ")
print()
if (k=='a'):print("• FILED AT AXIAL POINT = ",G)
if (k=='b'):print("• FILED AT EQUOTORIAL POINT = ",E)
