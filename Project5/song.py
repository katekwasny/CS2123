#Kate Kwasny & John Wu
#Project 5
from collections import deque
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
    r = len(s) + 1
    c = len(t) + 1
    C = {}
    for j in range(c):
        C[0,j] = j
    for i in range(1, len(s) +1):
        C[i, 0] = i
    for i in range(1, r):
        for j in range(1, c):
            if s[i] == t[j]: cmatch = C[i-1, j-1]
            else: cmatch = C[i-1, j-1] + 1
            #case 2 insert
            cinsert = C[i, j-1] + 1
            #case 3 delete
            cdelete = C[i-1, j] + 1
            cmin = min(cmatch, cinsert, cdelete)
            C[i, i] = cmin
    for keys, values in C.items():
        print(keys)
        print(values)
    return C[i,j]


    print("Delete ", s[i])
    print("Insert ", t[j])
    print("Replace ", s[i], " with ", t[j])
    print("Leave ", s[i], " unchanged")



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