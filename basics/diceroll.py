from random import randint  
flag = 0

d = [ '1','2','3','4','5','6']

while flag<4:
    input ("press enter to roll the dice")
    out = randint(1,6)
    print (f'number on dice is {d[out-1]}')
    if (out==6):
        flag+=1
    if ([out+1]==6):
        flag+=1
    if ([out+2]==6):
        flag+=1

        if flag==3:
          print("you WIN")
          break

    elif (out==1):
        flag+=1
    if ([out+1]==1):
        flag+=1
    if ([out+2]==1):
        flag+=1
        
        if flag==3:
            print("you LOSE")
            break
        



