def makeMapToArr():
    maps = []
    mapFile = open("map.txt", "r")

    lines = mapFile.readlines()
    map = []
    rowSize = 0

    for line in lines:
        if 'Stage' in line or '=' in line:
            if len(map) > 0 :
                for i in range(len(map)):
                    while len(map[i]) < rowSize:
                        map[i].append(' ')

                maps.append(map)
                map = []
                rowSize = 0
            continue

        rowSize = max(len(line.rstrip()), rowSize)
        row = []
        for cell in line:
            if cell != '\n' :
                row.append(cell)
        map.append(row)
    return maps


def Main ():
    maps = makeMapToArr()

    return map


def printMap (map):
    for row in map:
        print(''.join(row))


def playStage(map, stage_num):
    print('Stage' + str(stage_num) + '\n')

    myPos = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 'P':
                myPos = [i, j]
    while True:
        printMap(map)
        commands = input('\n' + 'SOKOBAN> ').upper()

        for command in commands:

            move = [0, 0]
            notice = ''
            if command == 'Q':
                print('Bye~')
                exit()
            elif command == 'W':
                move = [-1, 0]
                notice = '\nW: 위로 이동합니다.'
            elif command == 'A':
                move = [0, -1]
                notice = '\nA: 왼쪽으로 이동합니다.'
            elif command == 'S':
                move = [1, 0]
                notice = '\nS: 아래로 이동합니다.'
            elif command == 'D':
                move = [0, 1]
                notice = '\nD: 오른쪽으로 이동합니다.'
            else:
                printImpossible(command, map)
                continue

            nextPos = [myPos[0] + move[0], myPos[1] + move[1]]
            realNext = map[nextPos[0]][nextPos[1]]

            if realNext == ' ':
                map[nextPos[0]][nextPos[1]] = 'P'
                map[myPos[0]][myPos[1]] = ' '
                myPos = nextPos

            else:
                printImpossible(command, map)
                continue

            printMap(map)
            print(notice + '\n')



def printImpossible(command, map):
    printMap(map)
    print('\n' + command + ' (경고!) 해당 명령을 수행할 수 없습니다!\n')





def checkPosition (map, hallPos):
    myPos = []
    hallPos = []

    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 'P':
                myPos = [i, j]
            elif map[i][j] == 'O':
                hallPos.append([i, j])





playStage(Main(), 2)
