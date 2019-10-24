# Kate Kwasny & Caleb Gardner
# P3 Code, CS 2123 The University of Tulsa
# Implementation of interval partitioning algorithm
import datetime
from heapq import heappush , heappop

def scheduleRooms(rooms,cls):
    """
    Input: rooms - list of available rooms
           cls   - dictionary mapping class names to pair of (start,end) times
    Output: Return a dictionary mapping the room name to a list of
    non-conflicting scheduled classes.
    If there are not enough rooms to hold the classes, return 'Not enough rooms'.
    """

    classes = [] #priority queue of classes (start time, class)
    j = 0 #room counter
    k = len(rooms) #number of rooms available
    availrooms =[] #priority queue of available rooms (end time, room)
    rmassign = {}
    rmassign[rooms[0]] = [] #create an empty room

    # sort by start time
    for x in cls:
        heappush(classes, (cls[x][0], x)) #push the classrooms and start times into heap

    heappush(availrooms, (datetime.time(1), rooms[0])) #start with 0:00 finish time and first room

    #for j = 1 to n
    while classes:
        (classStart, className) = heappop(classes)
        (roomFinish, roomName) = heappop(availrooms)
        #if lecture j is compatible with some classroom
            #schedule lecture je in any such classroom k
        if classStart >= roomFinish:
            rmassign[roomName].append(className)
            heappush(availrooms, (cls[className][1], roomName))
        #else
            #allocate a new classroom d + 1
            #scedule lecture j in classroom d + 1
            # d = d+1
        else:
            heappush(availrooms, (roomFinish,roomName)) #puts it back
            j = j+1 #increase room counter
            if j < k: #if room number is less than number of available rooms
                heappush(availrooms, (cls[className][1], rooms[j]))
                rmassign[rooms[j]] = []
                rmassign[rooms[j]].append(className)
            else:
                return "There are not enough rooms."

    return rmassign

if __name__=="__main__":
    print("* * * * * * * Classes For Cool People * * * * * * *")
    cl1 = {"a": (datetime.time(9),datetime.time(10,30)),
           "b": (datetime.time(9),datetime.time(12,30)),
           "c": (datetime.time(9),datetime.time(10,30)),
           "d": (datetime.time(11),datetime.time(12,30)),
           "e": (datetime.time(11),datetime.time(14)),
           "f": (datetime.time(13),datetime.time(14,30)),
           "g": (datetime.time(13),datetime.time(14,30)),
           "h": (datetime.time(14),datetime.time(16,30)),
           "i": (datetime.time(15),datetime.time(16,30)),
           "j": (datetime.time(15),datetime.time(16,30))}
    rm1 = [1,2,3]
    print(cl1)
    print("\n~~~~~~~3 AVAILABLE ROOMS~~~~~~~")
    print(scheduleRooms(rm1,cl1))
    print("\n~~~~~~~2 AVAILABLE ROOMS~~~~~~~")
    print(scheduleRooms([1,2],cl1))
    ensrooms = ['KEH U1','KEH M1','KEH M2','KEH M3','KEH U2','KEH U3','KEH U4','KEH M4','KEH U8','KEH U9']
    csclasses = {'CS 1043': (datetime.time(9,30),datetime.time(11)),
              'CS 2003': (datetime.time(10,30),datetime.time(12)),
              'CS 2123': (datetime.time(11,15),datetime.time(12,45)),
              'CS 3003': (datetime.time(8,15),datetime.time(11,30)),
              'CS 3353': (datetime.time(11),datetime.time(12)),
              'CS 4013': (datetime.time(13),datetime.time(14,45)),
              'CS 4063': (datetime.time(12,30),datetime.time(14,30)),
              'CS 4123': (datetime.time(14),datetime.time(15)),
              'CS 4163': (datetime.time(14),datetime.time(16,30)),
              'CS 4253': (datetime.time(12),datetime.time(16)),
    }
    print("\n* * * * * * * Classes For NERDS * * * * * * *")
    print(csclasses)
    print("\n~~~~~~~10 AVAILABLE ROOMS~~~~~~~")
    print(scheduleRooms(ensrooms,csclasses))
    print("\n~~~~~~~4 AVAILABLE ROOMS~~~~~~~")
    print(scheduleRooms(ensrooms[:4],csclasses))
