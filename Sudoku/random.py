from random import randrange
def rand_number ():
    i = 0
    j = 0
    tab1 = []
    grid = [
        [3, 7, 4, 5, 8, 6, 9, 2, 1],
        [8, 5, 1, 9, 2, 4, 3, 6, 7],
        [6, 9, 2, 7, 1, 3, 5, 8, 4],
        [5, 4, 7, 1, 9, 2, 8, 3, 6],
        [1, 8, 9, 3, 6, 7, 2, 4, 5],
        [2, 6, 3, 4, 5, 8, 7, 1, 9],
        [9, 2, 5, 8, 4, 1, 6, 7, 3],
        [4, 3, 6, 2, 7, 5, 1, 9, 8],
        [7, 1, 8, 6, 3, 9, 4, 5, 2]
        ]
    number = (randrange(0,1))
    if number == 0:
        for i in grid:
            for y in i:
                last = y[0]
                y[0] = y[1]
                y[1] = last
        return grid
    else:
        return grid

    # while i < 9:
    #     tab = []
    #     while j < 9:
    #         if number in tab:
    #             number = (randrange(1, 9))
    #         else:
    #             tab.append(number)
    #         j += 1
    #     tab1.append(tab)
    #     i += 1
    # return tab1


test = rand_number()
print(test)
