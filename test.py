# function used for prototyping things :3

import os
import libraries.mob as mob



map = ["PPPPPPPPPPPPPPPPPPP0000000000000000PP0000000S00000000PP0000000000000000PP0000000000000000PP0000000000000000PP0000000000000000PP0000000000000000PP0000000000000000PP0000000000000000PP0000000000000000PP0000000000000000PP0000000000000000PP0000000E00000000PP0000000000000000PP0000000000000000PP0000000000000000PPPPPPPPPPPPPPPPPPP"]
map_bkp = list(map[0])
map_bkp[map[0].index('S')] = '0'
player = mob.Player(map[0].index('S'), 'FFFFFF')



if __name__ == "__main__":
    print("Hello world!")

    while(True):

        inp = input()

        mapa = list(map[0])



        #player movemeNyant
        if inp == 'w':
            aux = player.pos
            mapa[aux] = map_bkp[aux]
            mapa[aux - 18] = 'S'
            player.pos = aux - 18
        if inp == 'a':
            aux = player.pos
            mapa[aux] = map_bkp[aux]
            mapa[aux - 1] = 'S'
            player.pos = aux - 1
        if inp == 's':
            aux = player.pos
            mapa[aux] = map_bkp[aux]
            mapa[aux + 18] = 'S'
            player.pos = aux + 18
        if inp == 'd':
            aux = player.pos
            mapa[aux] = map_bkp[aux]
            mapa[aux + 1] = 'S'
            player.pos = aux + 1
        map[0] = ''.join(mapa)

        if inp in ['Q','q']:
            break;


        #draUwUing 

        if os.name == 'nt': # esse é pra vc ryan kkkkkk pq ######## o windows usa um clear diferente?
            os.system('cls')
        else:
            os.system('clear')

        index = 0
        mapx = ""
        for x in map[0]:
            if index % 18 == 0:
                print(mapx)
                mapx = ""
            if x == 'P':
                mapx += "WWW"
            if x == '0':
                mapx += "[ ]"
            if x == '1':
                mapx += "[-]"
            if x == 'S':
                mapx += "[@]"
            if x == 'E':
                mapx += "[S]"
            index += 1
        
        print(mapx)






    pass