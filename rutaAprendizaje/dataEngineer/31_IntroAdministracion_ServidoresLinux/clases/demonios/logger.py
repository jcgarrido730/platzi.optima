import time
from datetime import datetime

while True:
    with open("/datelogs/timestamp.txt", "a") as f:
        f.write("\nTimestamp: " + str(datetime.now()))
        f.close()
    time.sleep(1)