# The calculations are done in farthings. That is in quarters of pence.
"""
denomination = [['Guinea', 1008, False],
                ['Sovereign', 960, True],
                ['Half Guinea', 504, False],
                ['Half Sovereign', 480, True],
                ['Third Guinea', 336, True],
                ['Crown', 240, True],
                ['Half Crown', 120, False],
                ['Florin', 96, True],
                ['Shilling', 48, False],
                ['Sixpence', 24, False],
                ['Groat', 16, True],
                ['Threepence', 12, True],
                ['Half-groat', 8, True],
                ['Penny', 4, False],
                ['Halfpenny', 2, True],
                ['Farthing', 1, True]]
"""
import permanency

denomination = permanency.pull()

# Value of the pound, shilling and pence in farthings.
exchange = (('£', 960),
            ('s', 48),
            ('d', 4))


def lowest_denomination(pounds=0, shillings=0, pence=0):
    farthings = pounds * 960 + shillings * 48 + pence * 4
    return farthings


def coins_to_value(list):
    # This will ignore letters, unfilled entries, negative numbers, and floats.
    # The format of the list: [['coin_name', amount], . . ., ['coin_name', amount]]

    value = 0
    for coin in list:

        count = 0
        while True:
            if coin[0] == denomination[count][0]:
                value += coin[1] * denomination[count][1]
                break
            count += 1

    return value


def value_to_coins(farthings):
    total_coinage = []
    for dem in denomination:

        if dem[2]:
            quantity = 0
            while farthings >= dem[1]:
                quantity += 1
                farthings -= dem[1]

            if quantity > 0:
                amount = [dem[0], quantity]
                total_coinage.append(amount)

    return total_coinage


def farthings_to_readable(farthings):
    pounds, shillings, pence = 0, 0, 0
    fraction = ''

    while farthings >= exchange[0][1]:
        pounds += 1
        farthings -= exchange[0][1]
    pounds = str(pounds)

    while farthings >= exchange[1][1]:
        shillings += 1
        farthings -= exchange[1][1]
    shillings = str(shillings)

    while farthings >= exchange[2][1]:
        pence += 1
        farthings -= exchange[2][1]
    pence = str(pence)

    if farthings == 3:
        fraction = '¾'
        farthings -= 3
        if pence == '0':
            pence = ''

    elif farthings == 2:
        fraction = '½'
        farthings -= 2
        if pence == '0':
            pence = ''

    elif farthings == 1:
        fraction = '¼'
        farthings -= 1
        if pence == '0':
            pence = ''

    readable = exchange[0][0] + pounds + '. ' \
               + shillings + exchange[1][0] + '. ' \
               + pence + fraction + exchange[2][0] + '.'

    return readable
