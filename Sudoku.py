def main():
    a = [3,None,8,None,None,None,6,None,None]
    b = [4,2,9,None,3,None,8,None,5]
    c = [5,6,1,None,None,9,None,3,4]
    d = [None,None,4,7,None,6,None,None,1]
    e = [2,None,7,None,1,None,4,6,None]
    f = [None,1,None,None,9,5,None,None,7]
    g = [None,4,5,None,None,None,1,2,8]
    h = [8,None,None,5,None,None,9,None,6]
    i = [1,None,6,8,None,2,None,7,3]

    grid = [a,b,c,d,e,f,g,h,i]
    digs = [1,2,3,4,5,6,7,8,9]

    cols,boxes,grid = update(grid)
    
    print("\n\nThe Puzzle\n\n")
    displayer(grid)
    
    grid = solver(grid,cols,boxes,digs)
    
    print("\n\nTHE SOLUTION\n\n")
    displayer(grid)





def update(grid):
    
    uped_grid = grid
    
    col1 = list()
    col2 = list()
    col3 = list()
    col4 = list()
    col5 = list()
    col6 = list()
    col7 = list()
    col8 = list()
    col9 = list()
    
    cols = [col1,col2,col3,col4,col5,col6,col7,col8,col9]
    
    
    for x in range(9):
        for r in grid:
            cols[x].append(r[x])
    
    
    boxa1 = list()
    boxa2 = list()
    boxa3 = list()
    boxb1 = list()
    boxb2 = list()
    boxb3 = list()
    boxc1 = list()
    boxc2 = list()
    boxc3 = list()
    
    boxes = [boxa1,boxa2,boxa3,boxb1,boxb2,boxb3,boxc1,boxc2,boxc3]
    
    boxno = 0
    
    for box in boxes:
        if boxno in [0,1,2]:
            for row in grid[0:3]:
                for j in range(3):
                    box.append(row[j+boxno*3])
        elif boxno in [3,4,5]:
            boxno_ = boxno - 3
            for row in grid[3:6]:
                for j in range(3):
                    box.append(row[j+boxno_*3])
        elif boxno in [6,7,8]:
            boxno_ = boxno - 6
            for row in grid[6:]:
                for j in range(3):
                    box.append(row[j+boxno_*3])
        boxno += 1
    return cols,boxes,uped_grid


    
def get_box(row,posit,grid,boxes):
    if row in (grid[0],grid[1],grid[2]) and posit in (0,1,2):
        return boxes[0]
    elif row in (grid[0],grid[1],grid[2]) and posit in (3,4,5):
        return boxes[1]
    elif row in (grid[0],grid[1],grid[2]) and posit in (6,7,8):
        return boxes[2]
    elif row in (grid[3],grid[4],grid[5]) and posit in (0,1,2):
        return boxes[3]
    elif row in (grid[3],grid[4],grid[5]) and posit in (3,4,5):
        return boxes[4]
    elif row in (grid[3],grid[4],grid[5]) and posit in (6,7,8):
        return boxes[5]
    elif row in (grid[6],grid[7],grid[8]) and posit in (0,1,2):
        return boxes[6]
    elif row in (grid[6],grid[7],grid[8]) and posit in (3,4,5):
        return boxes[7]
    elif row in (grid[6],grid[7],grid[8]) and posit in (6,7,8):
        return boxes[8]
    else:
        return "you dun goofed"
    




def displayer(grid):
    sp_cou = 1
    nl_cou = 1
    for r in grid:
        for x in r:
            print(str(x).ljust(6),sep="    ",end="")
            if sp_cou == 3:
                print("  ",end="")
                sp_cou = 1
            else:
                sp_cou += 1
        print("\n")
        if nl_cou == 3:
            print("\n")
            nl_cou = 1
        else:
            nl_cou += 1
        


def solver(rows,columns,squares,digs):
    grid = rows
    cols = columns
    safety = 1
    boxes = squares
    while True:
        for s in range(9):
            row = grid[s]
            for dig in digs:
                possib = 0
                spot = 0
                if dig in row:
                    pass
                else:
                    for x in range(9):
                        box = get_box(row,x,grid,boxes)
                        if row[x] == None:
                            if dig not in cols[x] and dig not in box:
                                possib += 1
                                spot = x
                if possib == 1:
                    grid[s][spot] = dig
                    cols,boxes,grid = update(grid)
        for row in grid:
            if None in row:
                cest_fini = False
                break
            else:
                cest_fini = True
        if cest_fini == True:
            return grid
        safety += 1
        if safety > 1000:
            print("We're running in coicles")
            return grid
            
                

main()






