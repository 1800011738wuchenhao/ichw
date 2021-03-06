#ways to tile
#Wuchenhao
#2018/12/17
"""Module for tile work

This module provides all the ways to pave a wall of given length and
width with bricks of given length and width.It can also draw the way
you choose."""

if __name__=='__main__':
    wall=input('请输入墙的尺寸(长*宽)')
    A,B=int(wall.split('*')[0]),int(wall.split('*')[1])

    brick=input('请输入砖的尺寸(长*宽)')
    a,b=int(brick.split('*')[0]),int(brick.split('*')[1])

    AA=[0]*(A*B)

    def allcoor(x,y):
        '''Returns: The all the coordinates of a brick

        The value returned has type list.

        Parameter x:the abscissa of the lower-left corner of the brick
        Precondition: x is a int

        Parameter y:the ordinate of the lower-left corner of the brick
        Precondition: y is a int'''
        allcoors=[]
        for j in range(b):
            for k in range(a):
                allcoors.append((x+k,y+j))
        return(allcoors)

    def tonum(t):
        '''Returns: the one-dimensional form of a way

        The value returned has type tuple.

        Parameter t:one of the ways given by function output
        Precondition: t is a list'''
        for l in range(len(t)):
            x,y=t[l][0],t[l][1]
            t[l]=(x+y*A)
        return tuple(t)

    def tocoor(i):
        '''Returns: the coordinate of a num

        The value returned has type tuple.

        Parameter i:a num you want to convert to coordinate
        Precondition: i is an int'''
        return((i%A,i//A))

    def judge(p):
        '''Returns: if a brick can be put in from position p

        The value returned has type bool.

        Parameter p:a num represent a position you want to judge
        Precondition: p is an int'''
        if p%A+a>A or p//A+b>B or p==A*B+1:
            return False
        for i in range(b):
            for j in AA[p+i*A:p+i*A+a]:
                if j == 1:
                    return False
        else:
            return True

    def tile(n=0):
        '''Returns:all the ways to pave the wall with bricks(there may
        be a same way occurs for more than one time).

        The value returned has type list.'''
        global a,b,A,B
        ans=[]
        while AA[n]==1:
            n+=1
            if n==A*B:
                return [[]]
        for (a, b) in [(a, b), (b, a)]:
            if judge(n):
                bricks=tonum(allcoor(tocoor(n)[0],tocoor(n)[1]))
                for p in bricks:
                    AA[p]=1
                bb = tile(n)
                for cc in bb:
                    cc.append(bricks)
                ans.extend(bb)
                for p in bricks:
                    AA[p]=0
        return ans

    def output():
        '''Returns:all the ways to pave the wall with bricks,deleted the
        same ones.

        The value returned has type list.'''
        ways_without_repeats=list(set([tuple(p) for p in tile()]))
        tupled_ways=[0]*len(ways_without_repeats)
        for t in ways_without_repeats:
            tupled_ways[ways_without_repeats.index(t)]=list(t)
        return(tupled_ways)

    for i in output():
        print(i)

    c=int(input('输入要画出的方法(从0到'+str(len(output()))+')'))
    import turtle
    wn=turtle.Screen()
    p=turtle.Pen()
    wn.setworldcoordinates(0,0,A,B)
    p.speed(0)
    p.pensize(1)
    for u in range(A*B):
        p.up()
        p.goto(tocoor(u)[0]+0.5,tocoor(u)[1]+0.5)
        p.write(u)
        p.goto(tocoor(u))
        p.down()
        p.fd(1)
        p.lt(90)
        p.fd(1)
        p.lt(90)
        p.fd(1)
        p.lt(90)
        p.fd(1)
        p.lt(90)
    p.pensize(5)
    for i in output()[c]:
        p.up()
        p.goto(tocoor(min(i)))
        p.down()
        a,b=int(brick.split('*')[0]),int(brick.split('*')[1])
        if max(i)-min(i)==a*b-1:
            p.fd(a)
            p.lt(90)
            p.fd(b)
            p.lt(90)
            p.fd(a)
            p.lt(90)
            p.fd(b)
            p.lt(90)
        else:
            p.fd(b)
            p.lt(90)
            p.fd(a)
            p.lt(90)
            p.fd(b)
            p.lt(90)
            p.fd(a)
            p.lt(90)
