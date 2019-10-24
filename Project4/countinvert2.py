# Spencer Stith & Katherine Kwasny
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
    #Initialize the beginning variables
    output = []
    currentLeft = 0
    currentRight = 0
    inversions = 0
    #While both lists still have elements (adjusted for using pointers)
    while (currentLeft < len(lft) and currentRight < len(rgt)):
        ai = lft[currentLeft]
        bi = rgt[currentRight]
        #If right element is less than the left element
        if bi < ai:
            #Conflition
            print(bi, " conflicts with ",lft[currentLeft:])
            #Push to the output
            output.append(bi)
            #Number of elements left in the other list
            inversions += len(lft) - currentLeft
            currentRight += 1
        else:
            output.append(ai)
            currentLeft += 1
            #Push the rest of the list to the output
    while currentLeft < len(lft):
        output.append(lft[currentLeft])
        currentLeft += 1
    while currentRight < len(rgt):
        output.append(rgt[currentRight])
        currentRight += 1
    return (inversions, output)

def sortandcount(seq):
    """
    Divide-conquer-glue method for counting inversions.
    Function should invoke mergeandcount() to complete glue step.
    Input: ordered sequence seq
    Output: tuple (number inversions, sequence)
    """
    inversions = 0
    if len(seq) == 1:
        #Nothing to change; will just return with 0 inversions and sequence of length 1
        pass
    else:
        mid = int(len(seq)/2)
        firstHalf = seq[:mid]
        lastHalf = seq[mid:]
        #Collect inversions
        rFirst, firstHalf = sortandcount(firstHalf)
        rLast, lastHalf = sortandcount(lastHalf)
        r, seq = mergeandcount(firstHalf, lastHalf)
        #Add up all of the inversions and return
        inversions = r +rFirst + rLast
    return (inversions, seq)

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
    print("~~~~~ Number 1 ~~~~~")
    print(seq1)
    print("# Inversions: %i\n" % sortandcount(seq1)[0])
    print("~~~~~ Number 2 ~~~~~")
    print(seq2)
    print("# Inversions: %i\n" % sortandcount(seq2)[0])
    print("~~~~~ Number 3 ~~~~~")
    print(seq3)
    print("# Inversions: %i\n" % sortandcount(seq3)[0])

    print("~~~~~ Songs 1 ~~~~~")
    print(songs1)
    print("# Inversions: %i\n" % sortandcount(songs1)[0])
    print("~~~~~ Songs 2 ~~~~~")
    print(songs2)
    print("# Inversions: %i\n" % sortandcount(songs2)[0])
    print("~~~~~ Songs 3 ~~~~~")
    print(songs3)
    print("# Inversions: %i\n" % sortandcount(songs3)[0])
