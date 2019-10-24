#Kate Kwasny & John Wu
#Project 5: Dynamic programming Edit Distance

def read_playlist(filename):
    """
    Input: filename of CSV file listing (song,artist,genre) triples
    Output: List of (song,artist,genre)
    """
    playlist = []
    for line in open(filename):
        bits = [b.strip() for b in line.split(',')]
        playlist.append(bits)
    return playlist

def playlist_transform(s,t,compareType="Song"):
    """
    Computes the edit distance for two playlists s and t, and prints the minimal edits
      required to transform playlist s into playlist t.
    Inputs:

    s: 1st playlist (format: list of (track name, artist, genre) triples)
    t: 2nd playlist (format: list of (track name, artist, genre) triples)
    compareType: String indicating the type of comparison to make.
       "Song" (default): songs in a playlist are considered equivalent if the
         (song name, artist, genre) triples match.
       "Genre": songs in a playlist are considered equivalent if the same genre is used.
       "Artist": songs in a playlist are considered equivalent if the same artist is used.
    Output: The minimum edit distance and the minimal edits required to transform playlist
      s into playlist t.
    """
    #Makes blanks in front of statements
    if s[0] is not " ":
        s.insert(0, " ")
    if t[0] is not " ":
        t.insert(0, " ")

    #Determines the sorting type
    sortingType = 0
    if compareType is "Artist":
        sortingType = 1
    if compareType is "Genre":
        sortingType = 2
    #make the cost dictionary
    C = {}
    for j in range(len(t)):
        C[0,j] = j
    for i in range(1, len(s)):
        C[i, 0] = i
    for i in range(1, len(s)):
        for j in range(1, len(t)):
            if sortingType == 0:
                if s[i] == t[j]: cmatch = C[i-1, j-1] #same
                else: cmatch = C[i-1, j-1] + 1 #replace
            else:
                if s[i][sortingType] == t[j][sortingType]:
                    cmatch = C[i-1, j-1] #same
                else:
                    cmatch = C[i-1, j-1] + 1 #replace
            cinsert = C[i, j - 1] + 1 #insert
            cdelete = C[i - 1, j] + 1 #delete
            cmin = min(cmatch, cinsert, cdelete)
            C[i,j] = cmin
    print(C[i,j], " edits needed to turn playlist 1 into playlist 2")
    backtrack(C, s, t, sortingType)

def backtrack(C, s, t, sortingtype):
    row = len(s) - 1
    col = len(t) - 1
    instructions = []
#backtracks
    #marks the values around a point to create a path
    while row > 0 or col > 0:
        match = len(s) + 1
        insert = len(s) + 1
        delete = len(s) + 1
        #insert
        if row == 0 and col != 0:
            instr = "Insert " + str(t[col])
            instructions.append(instr)
            col -= 1
        #delete
        if col == 0 and row != 0:
            instr = "Delete " + str(s[row])
            instructions.append(instr)
            row -= 1
        #marks the cells
        if (row -1, col-1) in C:
            match = C[row-1, col-1]
        if (row, col-1) in C:
            insert = C[row, col -1]
        if (row -1, col) in C:
            delete = C[row -1, col]
        cinstruction = min(match, insert, delete) #list of instructions taken

        #creates the strings for the instructions
        if cinstruction is match:
            if sortingtype != 0 and (row != 0 and col != 0):
                #same
                if t[col][sortingtype] == s[row][sortingtype]:
                    instr = "Leave " + str(t[col])
                    instructions.append(instr)
                #replace
                else:
                    instr = "Replace " + str(s[row]) + " with " + str(t[col])
                    instructions.append(instr)
            #same
            elif t[col] == s[row]:
                instr = "Leave " + str(t[col])
                instructions.append(instr)
            #replace
            else:
                instr = "Replace " + str(s[row]) + " with " + str(t[col])
                instructions.append(instr)
            row -= 1
            col -= 1
        #insert
        elif cinstruction is insert:
            instr = "Insert " + str(t[col])
            instructions.append(instr)
            col -= 1
        #delete
        elif cinstruction is delete:
            instr = "Delete " + str(s[row])
            instructions.append(instr)
            row -= 1
    instructions.reverse() #corrects the order
    del instructions[0] #there is an empty cell, this deletes it
    for steps in instructions:
        print(steps)

if __name__=="__main__":
    #obtain local copy from http://secon.utulsa.edu/cs2123/blues1.csv
    b1 = read_playlist("blues1.csv")
    #obtain local copy from http://secon.utulsa.edu/cs2123/blues2.csv
    b2 = read_playlist("blues2.csv")
    print("Playlist 1")
    for song in b1:
        print(song)
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("Playlist 2")
    for song in b2:
        print(song)
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("Comparing playlist similarity by song")
    playlist_transform(b1,b2)
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("Comparing playlist similarity by genre")
    playlist_transform(b1,b2,"Genre")
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("Comparing playlist similarity by artist")
    playlist_transform(b1,b2,"Artist")
    #include your own playlists below

    play1 = read_playlist("p5playlist1.csv")
    play2 = read_playlist("p5playlist2.csv")
    for song in play1:
        print(song)
    for song in play2:
        print(song)
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("Comparing playlist similarity by song")
    playlist_transform(play1, play2)
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("Comparing playlist similarity by genre")
    playlist_transform(play1, play2, "Genre")
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("Comparing playlist similarity by artist")
    playlist_transform(play1, play2, "Artist")