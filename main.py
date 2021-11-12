import pywhatkit as kit
import timeTable as tt
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
check_time = now.strftime("%H:%M")
current_hour = int(current_time[:2])
current_minute = int(current_time[3:5])
msg = ""
print(check_time)


def showTodaysLectures(day):
    global msg
    while(check_time == "14:00"):
        print("checking time...")
        if check_time == "09:30":
            lecName = tt.Lecture[day][1]
            msg = f"{lecName[1]}"
            print(f"{day} Lecture 1 Started")
        elif check_time == "10:30":
            lecName = tt.Lecture[day][2]
            msg = f"{lecName[2]}"
        elif check_time == "12:00":
            lecName = tt.Lecture[day][3]
            msg = f"{lecName[3]}"
        elif check_time == "13:00":
            lecName = tt.Lecture[day][4]
            msg = f"{lecName[4]}"


def openWP(msg):
    print("Opening WhatsApp...")
    print(f"Link is ===>{msg}")
    kit.sendwhatmsg_instantly("+911234567890", msg,current_hour, current_minute+1, 5)
    # kit.sendwhatmsg_to_group("GyHLAbFQwuqHnA6Rw3rlJ5", "Hy guys", current_hour, current_minute+1, 2)


if __name__ == "__main__":
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    showTodaysLectures(days[0])
    openWP(msg)
    # for d in days:
