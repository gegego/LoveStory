from controller import Controller

def draw(status):
    for i in range(0,20):
        print('')
        for j in range(0,20):
            if( i==19 or j==0 or j==19):
                print('*',end='')
            elif(status[i][j-1] > 0):
                print('*',end='')
            else:
                print(' ',end='')



controller = Controller(19,18)
controller.initGame()
status = controller.get_current_status()
draw(status)
