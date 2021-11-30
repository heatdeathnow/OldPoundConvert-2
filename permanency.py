import calculate
import csv


def push():

    file = open('conf', 'w+')

    for line in calculate.denomination:
        file.write(f"{str(line)}".removeprefix('[').removesuffix(']').replace(', ', ',').replace("'", "") + '\n')

    file.close()


def pull():

    loaded = []

    try:
        with open("conf") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                loaded.append([str(row[0]), int(row[1]), False if row[2] == 'False' else True])
    except FileNotFoundError:
        hardcoded = "Guinea,1008,False\n" \
                    "Sovereign,960,True\n" \
                    "Half Guinea,504,True\n" \
                    "Half Sovereign,480,True\n" \
                    "Third Guinea,336,True\n" \
                    "Crown,240,True\n" \
                    "Half Crown,120,True\n" \
                    "Florin,96,True\n" \
                    "Shilling,48,True\n" \
                    "Sixpence,24,True\n" \
                    "Groat,16,True\n" \
                    "Threepence,12,True\n" \
                    "Half-groat,8,True\n" \
                    "Penny,4,True\n" \
                    "Halfpenny,2,True\n" \
                    "Farthing,1,True"

        file = open('conf', 'w+')
        file.write(hardcoded)
        file.close()

        with open("conf") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                loaded.append([str(row[0]), int(row[1]), False if row[2] == 'False' else True])

    return loaded
