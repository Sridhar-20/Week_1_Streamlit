Basic = float(input("Enter the basic salary \n"))

# HRA = float(0.67*Basic) if Basic<10000 else float(0.69*Basic) if Basic<=20000 else float(0.73*Basic)
# DA = float(0.73*Basic) if Basic<10000 else float(0.76*Basic) if Basic<=20000 else float(0.89*Basic)

if Basic < 10000 :
    HRA = float(0.67*Basic)
    DA = float(0.73*Basic)
elif Basic<=20000 :
    HRA = float(0.69*Basic)
    DA = float(0.76*Basic)
else :
    HRA = float(0.73*Basic)
    DA = float(0.89*Basic)

GS = HRA + DA + Basic
print(f"The gross salary is {GS:.2f}")