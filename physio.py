import time

for i in range(6):
    for j in range(10):
        for k in range(5):
            print i + 1, j + 1, k + 1
            print '\a'
            if k == 4 and j == 9:
                time.sleep(0.2)
                print '\a'
            time.sleep(1)
        time.sleep(1)
    time.sleep(4)
