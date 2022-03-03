#Addition  of two fractions 

from fractions import Fraction


f1_nume = int(input("Enter the numerator for 1st fraction :"))
f1_deno  = int(input("Enter the denominator for 1st fraction :"))
f2_nume = int(input("Enter the numerator for 2nd fraction :"))
f2_deno = int(input("Enter the denominator  for 2nd fraction :"))
if(f1_deno == f2_deno):
    fration = f1_nume + f2_nume
    print("addition: "   + str(fration)+ '/ '+ str(f1_deno))
else:
    Fraction = (f1_nume * f2_deno) + (f2_nume * f1_deno)
    print("addition: "   + str(Fraction)+ '/ '+ str(f1_deno * f2_deno))

