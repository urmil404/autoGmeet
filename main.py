import pywhatkit as kit
import timeTable as tt
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
current_hour = int(current_time[:2])
current_minute = int(current_time[3:5])
msg = ""


def showTodaysLectures(day):
    for i in range(1, 5):
        lecName = tt.Lecture[day][i]
        global msg
        msg = f"{lecName['1-OSTP - KG']}"
        # msg = f"{lecName}]"
        break

def openWP(msg):
    print("Opening WhatsApp...")
    print(msg)
    # kit.sendwhatmsg_instantly("+918128389164", msg,current_hour, current_minute+1, 5)
    # kit.sendwhatmsg_to_group("GyHLAbFQwuqHnA6Rw3rlJ5", "Hy guys", current_hour, current_minute+1, 2)


if __name__ == "__main__":
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    showTodaysLectures(days[0])
    openWP(msg)
    # for d in days:
