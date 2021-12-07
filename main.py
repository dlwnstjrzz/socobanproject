def makeMapToArr ():
    maps = []
    mapFile = open("map.txt", "r")

    lines = mapFile.readlines()
    rowSize = 0
    stage = []
    for line in lines:
        if 'Stage' in line or '=' in line:
            if len(stage) > 0:
                for i in range(len(stage)):
                    while len(stage[i]) < rowSize:
                        stage[i].append(' ')

                maps.append(stage)
                stage = []
                rowSize = 0
            continue


        rowSize = max(len(line.rstrip()), rowSize)
        row = []
        for cell in line:
            if cell == '#':
                row.append('0')
            elif cell == 'O':
                row.append('1')
            elif cell == 'o':
                row.append('2')
            elif cell == 'P':
                row.append('3')
            elif cell == ' ':
                row.append(cell)
        stage.append(row)
    return maps


def makeArrToData (map):
    for i in range(len(map)):    #i는 1스테이지
