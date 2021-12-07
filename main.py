def makeMapToArr ():
    maps = []
    mapFile = open("map.txt", "r")
    lines = mapFile.readlines()
    rowSize = 0
    hall = 0
    ball = 0
    stage = []
    position = []
    for line in lines:
        if 'Stage' in line or '=' in line:
            if len(stage) > 0:
                for i in range(len(stage)):
                    while len(stage[i]) < rowSize:
                        stage[i].append(' ') #stage1이 끝난 시점
                print(f"가로크기: {rowSize}\n세로크기: {len(stage)}\n구멍의 수:{hall}\n공의 수 :{ball}\n플레이어 위치 ({position[0] + 1}, {position[1]}) ")
                maps.append(stage)
                stage = []
                rowSize - 0
                hall = 0
                ball = 0
                position = []
            if '=' in line:
                continue

            print(''.join(line))
            continue

        print(''.join(line))
        rowSize = max(len(line.rstrip()), rowSize)
        row = []
        for cell in line:
            if cell == '#':
                row.append('0')
            elif cell == 'O':
                row.append('1')
                hall += 1
            elif cell == 'o':
                row.append('2')
                ball += 1
            elif cell == 'P':
                row.append('3')
                position.append(len(stage))
                position.append(len(row))
            elif cell == ' ':
                row.append(cell)
        stage.append(row)
    return maps






makeMapToArr()