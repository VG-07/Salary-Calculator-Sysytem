# //  # Salary System
# // # -- Input Section
# // # Employee Name : manasi
# // # Monthly Salary : 56700/-
# // # leave : 7
# // # TDS : 10%
# // # Extra Pay : 0
# // # Month(int) : 1
# // # Year(int) : 2023

# // # --- OutPut ----
# // # Employee Name : Manasi
# // # Monthly Salary : = 56700/-
# // # Yearly Salary (CTC) = 680400/-
# // # leave Amount =  12,803.22580645161/-
# // # TDS Amount =  4,389.677419354839
# // # Final pay Salary : = 39507.09677419355 + Extra Pay


name = (input('enter your name : '))
month_salary =int(input('enter your salary : '))
monthleave =int(input('enter your leav month : '))
TDS=int(input('enter reduct your TDS: ''%'))
extra_pay=int(input('Enter how much extra pay : '))
month = int(input('enter month in number : '))
year = int(input('enter A year : '))
print("--------------------------------")


if month == 1 or month ==3 or month ==5 or month ==7 or month ==8 or month ==10 or month ==12 :
  days= 31
elif month == 4 or month ==6 or month ==9 or month ==11 :
  days=30
elif ((month==2) and (year%4==0) or (year % 100 != 0) or (year % 400 == 0)) :
    days=29
else :
  days=28

p_lakh = month_salary * 12
print(f'Yearly salary CTC: {p_lakh} -/')

perday = (month_salary / days)
print(f'perday salary : {perday} -/')

leave_amount = ( perday * monthleave )
print(f'leave Amount : {leave_amount} -/')

TDS_amount = (month_salary / TDS)
print(f'TDS amount : {TDS_amount} -/')

TDScut = TDS_amount +leave_amount
after_TDS_and_LEAVE=month_salary - TDScut
final_salary = after_TDS_and_LEAVE + extra_pay

print(f'final totaL value : {final_salary} -/')