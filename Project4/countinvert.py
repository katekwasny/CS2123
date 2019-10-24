# Kate Kwasny, Spencer Stith
# Starter Code for Counting Inversions, Q1 HW4
# CS 2123, The University of Tulsa

from collections import deque
import itertools


def mergeandcount(lft, rgt):
    """
    Glue procedure to count inversions between lft and rgt.
    Input: two ordered sequences lft and rgt
    Output: tuple (number inversions, sorted combined sequence)
    """
    output = []
    lenLeft = 0

    lenLeft = len(lft)


    #Maintain a current pointer into each list, initialized to point to the front elements
    leftPointer = 0
    rightPointer = 0

    #Maintain a variable count for the number of inversions, initialized to 0
    invCount = 0

    #While both lists are nonempty:
    while leftPointer < len(lft) and rightPointer < len(rgt):

        #print("LEFT: ", lft)
        #print("RIGHT: ", rgt)

        #Let ai, bj, be the elements pointed to by the current pointer
        leftElement = lft[leftPointer]
        rightElement = rgt[rightPointer]

        #Append the smaller of these two to the output list


        #If bj is the smaller element then
        if(rightElement < leftElement):
            invCount += len(lft[leftPointer:])
            print(rightElement, " conflicts with ", lft[leftPointer:], "invCount: \n", invCount)
            output.append(rightElement)
            #Increment count by the number of elements remaining in A

            #print(invCount," + ", lenLeft)


            rightPointer += 1

        #Endif
        elif(leftElement < rightElement):
            output.append(leftElement)
            leftPointer += 1

        #Advance the current pointer in the list from which the smaller element was selected

    #Endwhile

    #Once one list is empty, append the remainder of the other list to the output
    if leftPointer > rightPointer:
        output.extend(rgt[rightPointer:])

    else:
        output.extend(lft[leftPointer:])

    print("Count: ", invCount)
    #Return count and the merged list
    return invCount, output

def sortandcount(seq):
    """
    Divide-conquer-glue method for counting inversions.
    Function should invoke mergeandcount() to complete glue step.
    Input: ordered sequence seq
    Output: tuple (number inversions, sequence)
    """
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    #If the list has one element:
    if len(seq) == 1:
        #there are no inversions (0, seq)
        return 0, seq

    #Else
    else:
        #Divide the list into two halves
        mid = len(seq)/2
        mid = int(mid)
        #A containts the first n/2 elements
        a = seq[:mid]
        #B contains the remaining n/2 elements
        b = seq[mid:]

        print("A: ", a)
        print("B: ", b)

        #(ra, A) = sortandcount(a)
        (ra, a) = sortandcount(a)

        #(rb, B) = sortandcount(b)
        (rb, b) = sortandcount(b)

        #(r, seq) = meergeandcount(a, b)
        (r, seq) = mergeandcount(a, b)
    #endif

    #Return r = ra + rb + r, and the sorted list seq
    r = ra + rb + r

    #print("R: ", r)

    return r, seq

if __name__ == "__main__":
    seq1 = [7, 10, 18, 3, 14, 17, 23, 2, 11, 16]
    seq2 = [2, 1, 3, 6, 7, 8, 5, 4, 9, 10]
    seq3 = [1, 3, 2, 6, 4, 5, 7, 10, 8, 9]
    songs1 = [(1, "Stevie Ray Vaughan: Couldn't Stand the Weather"),
              (2, "Jimi Hendrix: Voodoo Chile"),
              (3, "The Lumineers: Ho Hey"),
              (4, "Adele: Chasing Pavements"),
              (5, "Cake: I Will Survive"),
              (6, "Aretha Franklin: I Will Survive"),
              (7, "Beyonce: All the Single Ladies"),
              (8, "Coldplay: Clocks"),
              (9, "Nickelback: Gotta be Somebody"),
              (10, "Garth Brooks: Friends in Low Places")]
    songs2 = [(3, "The Lumineers: Ho Hey"),
              (4, "Adele: Chasing Pavements"),
              (2, "Jimi Hendrix: Voodoo Chile"),
              (1, "Stevie Ray Vaughan: Couldn't Stand the Weather"),
              (8, "Coldplay: Clocks"),
              (6, "Aretha Franklin: I Will Survive"),
              (5, "Cake: I Will Survive"),
              (7, "Beyonce: All the Single Ladies"),
              (9, "Nickelback: Gotta be Somebody"),
              (10, "Garth Brooks: Friends in Low Places")]
    songs3 = [(1, "Stevie Ray Vaughan: Couldn't Stand the Weather"),
              (2, "Jimi Hendrix: Voodoo Chile"),
              (3, "The Lumineers: Ho Hey"),
              (4, "Adele: Chasing Pavements"),
              (6, "Aretha Franklin: I Will Survive"),
              (5, "Cake: I Will Survive"),
              (7, "Beyonce: All the Single Ladies"),
              (8, "Coldplay: Clocks"),
              (10, "Garth Brooks: Friends in Low Places"),
              (9, "Nickelback: Gotta be Somebody")]

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

"""The code still isn't accounting for the right half of conflicts for when the code is split
like it counts the left half of inverses fine, and then the right half is wrong. But I got the number of inversions 
correct for the integer lists. I am still having trouble with the songs lists. For songs 2 
[3, 4, 2, 1, 8, 6, 5, 7, 9, 10] when it splits, it only accounts for [3, 4, 2, 1, 8] this halves inverse count 
 and not this one [6, 5, 7, 9, 10] and when glue-ing back it ignores them too
"""