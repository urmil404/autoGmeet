import pywhatkit as kit
import timeTable as tt
import calendar
from datetime import datetime
from datetime import date

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
check_time = now.strftime("%H:%M")
current_hour = int(current_time[:2])
current_minute = int(current_time[3:5])
current_date = date.today()
today = calendar.day_name[current_date.weekday()]
msg = ""


def showTodaysLectures(today):
    global msg
    while(check_time == "14:00"):
        print("checking time...")
        if check_time == "09:30":
            lecName = tt.Lecture[today][1]
            msg = f"{lecName[1]}"
            print(f"{today} Lecture 1 Started")
        elif check_time == "10:30":
            lecName = tt.Lecture[today][2]
            msg = f"{lecName[2]}"
            print(f"{today} Lecture 2 Started")
        elif check_time == "12:00":
            lecName = tt.Lecture[today][3]
            msg = f"{lecName[3]}"
            print(f"{today} Lecture 3 Started")
        elif check_time == "13:00":
            lecName = tt.Lecture[today][4]
            msg = f"{lecName[4]}"
            print(f"{today} Lecture 4 Started")


def openWP(msg):
    print("Opening WhatsApp...")
    print(f"Link is ===>{msg}")
    # kit.sendwhatmsg_instantly("+911234567890", msg,current_hour, current_minute+1, 5)
    # kit.sendwhatmsg_to_group("GyHLAbFQwuqHnA6Rw3rlJ5", "Hy guys", current_hour, current_minute+1, 2)


if __name__ == "__main__":
    showTodaysLectures(today)
    openWP(msg)
