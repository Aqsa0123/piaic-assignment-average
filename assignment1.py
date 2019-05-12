Physics_Marks=int(input("Enter your Physics Marks : "))
Mathematics_Marks=int(input("Enter your Mathematics Marks : "))
Chemistry_Marks=int(input("Enter your Chemistry Marks : "))
PST_Marks=int(input("Enter your Pakistan Studies Marks : "))
Urdu_Marks=int(input("Enter your Urdu Marks : "))
English_Marks=int(input("Enter your English Marks : "))
Average=(Physics_Marks+Mathematics_Marks+Chemistry_Marks+PST_Marks+Urdu_Marks+English_Marks)/6
print('Your Average score is ' + str(Average))
if Average>=80:
    print('Congradualations!! Your scored A+ Grade')
elif Average>=70 and Average<80:
    print('Good...!! You scored A grade')
elif Average>=50 and Average<70:
    print('You got B grade')
else:
    print('your Failed ...Study hard')
