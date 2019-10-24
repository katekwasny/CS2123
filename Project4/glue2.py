# Spencer Stith, Kate Kwasny
# Starter Code for Counting Inversions, Q1 HW4
# CS 2123, The University of Tulsa

from collections import deque
import itertools

def mergeandcount(lft,rgt):
    """
    Glue procedure to count inversions between lft and rgt.
    Input: two ordered sequences lft and rgt
    Output: tuple (number inversions, sorted combined sequence)
    """
    #print("LEFT: ", lft)
    #print("RIGHT: ", rgt)
    output = []
    lftPoint, rgtPoint = 0, 0
    inversions = 0
    while ((lftPoint < len(lft)) and rgtPoint < len(rgt)):
        #print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        l = lft[lftPoint]
        r = rgt[rgtPoint]

        #print("LFT: ", lft)
        #print("RGT: ", rgt)
        #print("THIS THING r: ", r)
        #print("THIS THING l: ", l)
        x = len(lft)
        if (r < l):
            print(r, "conflicts with ", lft[lftPoint:])
            output.append(r)
            #print("appending: ", r)
            #inversions += len(lft) - 1
            inversions += x
            #print("inver: ", inversions)
            #print("x: ", x)
            rgtPoint += 1
            #rgt.remove(r)
            #lft.remove(l)
        else:
            output.append(l)
            lftPoint += 1
            x -= 1
    #print("output before: ", output)
    if lftPoint > rgtPoint:
        #print("leftpoint greater, extending ", rgt[rgtPoint:])
        output.extend(rgt[rgtPoint:])
    else:
        output.extend(lft[lftPoint:])
    #print("output: ", output)
    print("inversions: ", inversions)
    return (inversions, output)

def sortandcount(seq):
    """
    Divide-conquer-glue method for counting inversions.
    Function should invoke mergeandcount() to complete glue step.
    Input: ordered sequence seq
    Output: tuple (number inversions, sequence)
    """
    aInversions = 0
    bInversions = 0
    inver = 0
    if len(seq) == 1:
        return (0, seq)
    else:
        mid = len(seq)/2
        middle = int(mid)
        a, b = seq[:middle], seq[middle:]
        #print("a: ", a)
        #print("b: ", b)
        (aInversions, a) = sortandcount(a)
        (bInversions, b) = sortandcount(b)
        inver = aInversions + bInversions
        print("aInversions: ", aInversions)
        print("bInversions: ", bInversions)
        print("inver :", inver)
        (inver, seq) = mergeandcount(a, b)
    #print("seq: ", seq)
    return (inver, seq)

if __name__ =="__main__":
    seq1 = [7, 10, 18, 3, 14, 17, 23, 2, 11, 16]
    seq2 = [2, 1, 3, 6, 7, 8, 5, 4, 9, 10]
    seq3 = [1, 3, 2, 6, 4, 5, 7, 10, 8, 9]
    songs1 = [(1,"Stevie Ray Vaughan: Couldn't Stand the Weather"),
             (2,"Jimi Hendrix: Voodoo Chile"),
             (3,"The Lumineers: Ho Hey"),
             (4,"Adele: Chasing Pavements"),
             (5,"Cake: I Will Survive"),
             (6,"Aretha Franklin: I Will Survive"),
             (7,"Beyonce: All the Single Ladies"),
             (8,"Coldplay: Clocks"),
             (9,"Nickelback: Gotta be Somebody"),
             (10,"Garth Brooks: Friends in Low Places")]
    songs2 = [(3,"The Lumineers: Ho Hey"),
             (4,"Adele: Chasing Pavements"),
             (2,"Jimi Hendrix: Voodoo Chile"),
             (1,"Stevie Ray Vaughan: Couldn't Stand the Weather"),
             (8,"Coldplay: Clocks"),
             (6,"Aretha Franklin: I Will Survive"),
             (5,"Cake: I Will Survive"),
             (7,"Beyonce: All the Single Ladies"),
             (9,"Nickelback: Gotta be Somebody"),
             (10,"Garth Brooks: Friends in Low Places")]
    songs3 = [(1,"Stevie Ray Vaughan: Couldn't Stand the Weather"),
             (2,"Jimi Hendrix: Voodoo Chile"),
             (3,"The Lumineers: Ho Hey"),
             (4,"Adele: Chasing Pavements"),
             (6,"Aretha Franklin: I Will Survive"),
             (5,"Cake: I Will Survive"),
             (7,"Beyonce: All the Single Ladies"),
             (8,"Coldplay: Clocks"),
             (10,"Garth Brooks: Friends in Low Places"),
             (9,"Nickelback: Gotta be Somebody")]
    print(seq1)
    print("# Inversions: %i\n" %sortandcount(seq1)[0])
    print(seq2)
    print("# Inversions: %i\n" %sortandcount(seq2)[0])
    print(seq3)
    print("# Inversions: %i\n" %sortandcount(seq3)[0])
    print(songs1)
    print("# Inversions: %i\n" %sortandcount(songs1)[0])
    print(songs2)
    print("# Inversions: %i\n" %sortandcount(songs2)[0])
    print(songs3)
    print("# Inversions: %i\n" %sortandcount(songs3)[0])