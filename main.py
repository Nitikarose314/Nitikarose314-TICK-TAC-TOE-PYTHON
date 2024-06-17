
def sum(a,b,c):
    return a+b+c
def printboard(x, z):
    zero = "x" if x[0] else ('o' if z[0] else 0)
    one = "x" if x[1] else ('o' if z[1] else 1)
    two = "x" if x[2] else ('o' if z[2] else 2)
    three = "x" if x[3] else ('o' if z[3] else 3)
    four = "x" if x[4] else ('o' if z[4] else 4)
    five = "x" if x[5] else ('o' if z[5] else 5)
    six = "x" if x[6] else ('o' if z[6] else 6)
    seven = "x" if x[7] else ('o' if z[7] else 7)
    eight = "x" if x[8] else ('o' if z[8] else 8)
    print(f" {zero} | {one} | {two} ")
    print("------")
    print(f" {three} | {four} | {five} ")
    print("------")
    print(f" {six} | {seven} | {eight} ")

    
def chck(x,z):
    xwin=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in xwin:
        if (sum(x[win[0]],x[win[1]],x[win[2]])==3):
            print("x won")
            return 1
        if(sum(z[win[0]],z[win[1]],z[win[2]])==3):
             print("y won")
             return 0
    return-1    


if __name__ == "__main__":
    x = [0, 0, 0, 0, 0, 0, 0,0,0]
    z = [0, 0, 0, 0, 0, 0, 0,0,0]
    turn = 1
    print("welcome")
    while True:
        printboard(x,z)
        if turn == 1:
            print("x chance \n")
            value = int(input("enter value: "))
            z[value] = 1
        else:
            print("y chance \n")
            value = int(input("enter value: "))
            x[value] = 1
        chw=chck(x,z)
        if(chw !=-1):
    
            print("match over")
            break
        

        turn=1-turn