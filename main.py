import pywhatkit as kit
import timeTable as tt
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
current_hour = int(current_time[:2])
current_minute = int(current_time[3:5])
def openWP():
    print("Opening WhatsApp...")
    # kit.sendwhatmsg_instantly("+918128389164","demo msgs",current_hour,current_minute+1,5)
    kit.sendwhatmsg_to_group("GyHLAbFQwuqHnA6Rw3rlJ5", "Hy guys", current_hour, current_minute+1, 2)
def showTodaysLectures(day):
    for i in range(1, 5):
        print(tt.Lecture[day][i])


if __name__ == "__main__":
    showTodaysLectures("Monday")
    openWP()
