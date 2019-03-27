import time

chords = input("What are the chords?")
BPM = int(input("What is the BPM?"))
delay = 60 / BPM

print(BPM)
print(delay)

while 1==1:
    for i in chords:
        time.sleep(delay)
        print(i)