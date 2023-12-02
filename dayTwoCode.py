

res= 0
#PArt One
#initConfigure ={"red" : 12, "green" : 13, "blue" : 14}

with open("dayTwoData.txt") as dataSource:
    for line in dataSource:
        gameNum = line.split(':')[0].split(' ')[-1]
        gameSet = line.strip().split(':')[-1].split(';')
        mybool = True
        initConfigure ={"red" : 0, "green" : 0, "blue" : 0} # Part 2 
        
        for i in range(0, len(gameSet)):
            gameSetItem = gameSet[i]
            game = gameSetItem.split(',')
            for val in game:
                mygame = val.strip().split(' ')
                if mygame[-1] in initConfigure:
                    if int(mygame[0]) > initConfigure[mygame[-1]]:
                        initConfigure[mygame[-1]] = int(mygame[0])
                        mybool = False
        ###########Part One #########
        # if mybool:
        #     res+= int(gameNum)

        res += initConfigure['blue'] * initConfigure['green'] * initConfigure['red']
        print(res)
               
            