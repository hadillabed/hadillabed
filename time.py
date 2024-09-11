import datetime
def friday_13_th(year,month):
    date=datetime.date(year,month,13)
    if date.weekday()==4:
        return True
    else:
        return False
print(friday_13_th(2024,9))