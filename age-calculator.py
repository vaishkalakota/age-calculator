from math import *


cd = int(input("Enter current day: "))
cm = int(input("Enter current month: "))
cy = int(input("Enter current year: "))
bd = int(input("Enter birth day: "))
bm = int(input("Enter birth month: "))
by = int(input("Enter birth year: "))


orig_cd, orig_cm = cd, cm


#days older calculation
if cd >= bd:
   days_older = cd-bd
else:
   cd+=30
   days_older = cd-bd
#months older calculation
if cm >= bm:
   months_older = cm-bm
else:
   cm+=12
   months_older = cm-bm


#years older calculation
if orig_cm > bm or (orig_cm == bm  and  orig_cd >= bd):
   years_older = cy - by
else:
   years_older = cy - by - 1


print("Days Older = {} \tMonths Older = {} \tYears Older = {}"
     .format(days_older, months_older, years_older))

