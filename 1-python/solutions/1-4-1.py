from datetime import datetime
today=datetime.now()
print(today.day)


birthday = input("Enter your birthday : ")
test = datetime.strptime(birthday, "%Y-%m-%d")
print(test)

from dateutils import parsedate_mdy, fortmatdate_ymd

                         
