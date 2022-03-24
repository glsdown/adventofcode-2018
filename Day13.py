up_cart = '^'
down_cart = 'v'
left_cart = '<'
right_cart = '>'

left = [0,-1]
right = [0, 1]
up = [-1,0]
down = [1, 0]

track = [list(line) for line in open('day13input.txt', 'r')]
cart_picture = [[-1 for i in range(len(track[j]))] for j in range(len(track))]

carts = {}
cart_num = 0

for row in range(len(track)):
    for col in range(len(track[row])):
        if track[row][col] == up_cart:
            carts[cart_num] = {'direction': [i for i in up], 'position':[row, col], 'intersect':0}
            track[row][col] = "|"
            cart_picture[row][col] = cart_num
            cart_num += 1
        elif track[row][col] == down_cart:
            carts[cart_num] = {'direction': [i for i in down], 'position':[row, col], 'intersect':0}
            track[row][col] = "|"
            cart_picture[row][col] = cart_num
            cart_num += 1
        elif track[row][col] == left_cart:
            carts[cart_num] = {'direction': [i for i in left], 'position':[row, col], 'intersect':0}
            track[row][col] = "-"
            cart_picture[row][col] = cart_num
            cart_num += 1
        elif track[row][col] == right_cart:
            carts[cart_num] = {'direction': [i for i in right], 'position':[row, col], 'intersect':0}
            track[row][col] = "-"
            cart_picture[row][col] = cart_num
            cart_num += 1

crash = False

while not crash:
    for row in range(len(cart_picture)):
        for col in range(len(cart_picture[row])):
            if cart_picture[row][col] != -1:
                cart = cart_picture[row][col]
                xchange, ychange = carts[cart]['direction']
                carts[cart]['position'] = [row + xchange, col + ychange]
                cart_picture[row][col] = -1
                if cart_picture[row + xchange][col + ychange] != -1:

                    # Part 1
                    #print("CRASH! At", carts[cart]['position'][::-1])
                    #crash = True
                    #exit()
                    carts.pop(cart)
                    carts.pop(cart_picture[row + xchange][col + ychange])
                    cart_picture[row + xchange][col + ychange] = -1
                    continue

                if track[row + xchange][col + ychange] == "\\":
                    carts[cart]['direction'].reverse()
                elif track[row + xchange][col + ychange] == "/":
                    carts[cart]['direction'].reverse()
                    carts[cart]['direction'] = [-i for i in carts[cart]['direction']]
                elif track[row + xchange][col + ychange] == "+":
                    if carts[cart]['intersect'] == 0:

                        # Go left
                        if carts[cart]['direction'][1] == 0:
                            carts[cart]['direction'].reverse()
                        else:
                            carts[cart]['direction'].reverse()
                            carts[cart]['direction'] = [-i for i in carts[cart]['direction']]

                    elif carts[cart]['intersect'] == 2:

                        # Go right
                        if carts[cart]['direction'][0] == 0:
                            carts[cart]['direction'].reverse()
                        else:
                            carts[cart]['direction'].reverse()
                            carts[cart]['direction'] = [-i for i in carts[cart]['direction']]

                    carts[cart]['intersect'] = (carts[cart]['intersect'] + 1) % 3

    carts_on_track= [key for key in carts.keys()]

    for cart in carts_on_track:
        row, col = carts[cart]['position']

        if cart_picture[row][col] != -1:
            # PART 1
            #print("CRASH! At", carts[cart]['position'][::-1])
            #crash = True
            #exit()
            try:
                carts.pop(cart)
                carts.pop(cart_picture[row][col])
            except:
                pass
            cart_picture[row][col] = -1
        else:
            cart_picture[row][col] = cart

    if len(carts.keys()) == 1:
        print(carts)
        break



