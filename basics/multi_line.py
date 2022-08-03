from mailbox import linesep


data = "" #empty string

while True:
    line = input ("line >>>")
    if not line:
        break
    data += line+" "#for correct spacing space is added

    print ("You have entered following data")
    print(data) 