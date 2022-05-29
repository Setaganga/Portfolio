#So I got this project idea from a book when I was reading about datetimes and stuff. And I just had a random thought. Boom. Project
#Enter in Format: ARG1:yyyy-mm-dd or yyyy-mm-dd hh-mm ARG2: True if time included, otherwise False
#NOTE: THIS ALSO INCLUDES LEAP YEARS
from datetime import datetime
def birthdaycalc(birthday,withTime = False):
    if withTime:
        birthday = datetime.strptime(birthday, '%Y-%m-%d %H:%M')
        today = datetime.now().replace(second=0).replace(microsecond=0)
        TD = today - birthday
        hour = str(TD)[11:13]
        if hour[-1] == ":":
            hour = hour[0]
        minute = str(TD)[14:16]
        if minute[-1] == ":":
            minute = minute[0]
        result = f"Years:{TD.days // 365} Days:{TD.days % 365} Hours:{hour} Minutes:{minute}"
        return result
    else:
        birthday = datetime.strptime(birthday, '%Y-%m-%d')
        today = datetime.today()
        TD = today - birthday
        result = f"Years:{TD.days // 365} Days:{TD.days % 365}"
        return result

print(birthdaycalc("2007-4-7",False))
print(birthdaycalc("2007-4-7 19:07",True))
print(birthdaycalc("1974-5-4",False))
print(birthdaycalc("1974-3-15",False))
