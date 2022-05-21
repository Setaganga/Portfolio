#So I got this project idea from a book when I was reading about datetimes and stuff. And I just had a random thought. Boom. Project
#Enter in Format: ARG1:yyyy-mm-dd or yyyy-mm-dd hh-mm ARG2: True if time included, otherwise False
#Im also using my birthday, so wish me a happy birthday on April 7th okay?
from datetime import datetime
def birthdaycalc(birthday,withTime = False):
    if withTime:
        birthday = datetime.strptime(birthday, '%Y-%m-%d %H:%M')
        today = datetime.now().replace(second=0).replace(microsecond=0)
        result = today - birthday
        hour = str(result)[11:13]
        minute = str(result)[14:16]
        result = f"Years:{result.days // 365} Days:{result.days % 365} Hours:{hour} Minutes:{minute}"
        return result
    else:
        birthday = datetime.strptime(birthday, '%Y-%m-%d')
        today = datetime.today()
        result = today - birthday
        return f"Years:{result.days // 365} Days:{result.days % 365}"

print(birthdaycalc("2007-4-7 7:07",True))
print(birthdaycalc("2007-4-7",False))
