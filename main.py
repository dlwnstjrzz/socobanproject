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
    for index, map in enumerate(maps):
        playStage(map, index+1)
    print('전체 게임을 클리어하셨습니다!\n축하드립니다!')

def printMap (map, hallPos):

    for hall in hallPos:
        if map[hall[0]][hall[1]] == ' ':
            map[hall[0]][hall[1]] = 'O'

    for row in map:

        print(''.join(row))


def playStage(map, stage_num):
    print('Stage' + str(stage_num) + '\n')
    moveCount = 0

    myPos, hallPos = checkPosition(map)
    while not finishCheck(map, hallPos):
        printMap(map, hallPos)
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
                printImpossible(command, map, hallPos)
                continue

            nextPos = [myPos[0] + move[0], myPos[1] + move[1]]
            if rightRange(map, nextPos):
                realNext = map[nextPos[0]][nextPos[1]]

                if realNext == ' ' or realNext == 'O':
                    map[nextPos[0]][nextPos[1]] = 'P'
                    map[myPos[0]][myPos[1]] = ' '
                    myPos = nextPos
                elif realNext == '#':
                    printImpossible(command, map, hallPos)
                    continue
                elif realNext == 'o':
                    nextNextPos = [nextPos[0] + move[0], nextPos[1] + move[1]]
                    if rightRange(map, nextNextPos):
                        realNextNext = map[nextNextPos[0]][nextNextPos[1]]
                        if realNextNext == ' ':
                            map[nextNextPos[0]][nextNextPos[1]] = 'o'
                            map[nextPos[0]][nextPos[1]] = 'P'
                            map[myPos[0]][myPos[1]] = ' '
                            myPos = nextPos
                        elif realNextNext == 'O':
                            map[nextNextPos[0]][nextNextPos[1]] = '0'
                            map[nextPos[0]][nextPos[1]] = 'P'
                            map[myPos[0]][myPos[1]] = ' '
                            myPos = nextPos
                        else:
                            printImpossible(command, map, hallPos)
                            continue
                    else:
                        printImpossible(command, map, hallPos)
                        continue



            else:
                printImpossible(command, map, hallPos)
                continue

            printMap(map, hallPos)
            print(notice + '\n')
            moveCount += 1
    print('빠밤! Stage ' + str(stage_num) + ' 클리어!')
    print('턴수: ' + str(moveCount) + '\n')


def printImpossible(command, map, hallPos):
    printMap(map, hallPos)
    print('\n' + command + ' (경고!) 해당 명령을 수행할 수 없습니다!\n')


def rightRange(map, pos):
    return 0 <= pos[0] and pos[0] < len(map) and 0 <= pos[1] and pos[1] < len(map[0])


def checkPosition (map):
    myPos = []
    hallPos = []

    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 'P':
                myPos = [i, j]
            elif map[i][j] == 'O':
                hallPos.append([i, j])
    return myPos, hallPos

def finishCheck(map, hallPos):
    for hall in hallPos:
        if map[hall[0]][hall[1]] != '0':
            return False

    return True


Main()

