# James Hale and Kate Kwasny
# Project 2

import urllib.request, urllib.parse, urllib.error
from collections import deque
visited = None
path = None
def byte2str(b):
    """
    Input: byte sequence b of a string
    Output: string form of the byte sequence
    Required for python 3 functionality
    """
    return "".join(chr(a) for a in b)


def getLinks(url, baseurl="http://secon.utulsa.edu/cs2123/webtraverse/"):
    """
    Input: url to visit, Boolean absolute indicates whether URLs should include absolute path (default) or not
    Output: list of pairs of URLs and associated text
    """
    # import the HTML parser package
    try:
        from bs4 import BeautifulSoup
    except:
        print('You must first install the BeautifulSoup package for this code to work')
        raise
    # fetch the URL and load it into the HTML parser
    soup = BeautifulSoup(urllib.request.urlopen(url).read(), features="html.parser")
    # pull out the links from the HTML and return
    return [baseurl + byte2str(a["href"].encode('ascii', 'ignore')) for a in soup.findAll('a')]


def print_dfs(url):
    """
    Print all links reachable from a starting **url**
    in depth-first order
    """

    global visited
    theDict = {url: getLinks(url)}
    if visited is None:
        visited = set()
    visited.add(url)
    print(url)
    for x in theDict[url]:
        if x in visited:
            continue
        print_dfs(x)

    """
    theDict = {}
    visited, Q = set(), []
    Q.append(url)
    while Q:
        aLink = Q.pop()
        if aLink in visited: continue
        print (aLink)
        visited.add(aLink)
        theDict[aLink] = getLinks(aLink)
        Q.extend(getLinks(aLink))
    """

def print_bfs(url):
    """
    Print all links reachable from a starting **url**
    in breadth-first order
    """
    theDict = {}
    visited, Q = set(), deque()
    Q.append(url)
    while Q:
        aLink = Q.popleft()
        if aLink in visited: continue
        visited.add(aLink)
        Q.extend(getLinks(aLink))
        theDict[aLink] = getLinks(aLink)
        print (aLink)

def find_shortest_path(url1, url2):
    """
    Find and return the shortest path
    from **url1** to **url2** if one exists.
    If no such path exists, say so.
    """
    path = [url2]
    P = bfs_parents(url1)
    curr = url2
    pathExists = True
    if url2 in P:
        while P[curr] != url1:
            if P[curr] is None:
                print('Path not Found')
                pathExists = False
                break
            else:
                path.append(P[curr])
                curr = P[curr]
    else:
        pathExists = False
    path.append(url1)
    path.reverse()
    if pathExists:
        for x in path:
            print (x)
        print("*" * len(path[len(path)-1]))
    else:
        print ("No path exits.")
        print("*" * 14)

def find_max_depth(start_url):
    """
    Find and return the URL that is the greatest distance from start_url, along with the sequence of links that must be followed to reach the page.
    For this problem, distance is defined as the minimum number of links that must be followed from start_url to reach the page.
    """
    theDict = {}
    path = []
    visited, Q = set(), deque()
    Q.append(start_url)
    while Q:
        aLink = Q.popleft()
        if aLink in visited: continue
        visited.add(aLink)
        Q.extend(getLinks(aLink))
        theDict[aLink] = getLinks(aLink)
        path.append(aLink)
    find_shortest_path(start_url, path.pop())

def bfs_parents(url):
    theDict = {}
    visited, Q = set(), deque()
    Q.append(url)
    while Q:
        aLink = Q.popleft()
        if aLink in visited: continue
        visited.add(aLink)
        Q.extend(getLinks(aLink))
        theDict[aLink] = getLinks(aLink)
    P, Q = {url: None}, deque()
    Q.append(url)
    while Q:
        aLink = Q.popleft()
        for v in theDict[aLink]:
            if v in P: continue
            P[v] = aLink
            Q.append(v)
    return P


if __name__ == "__main__":

    starturl = "http://secon.utulsa.edu/cs2123/webtraverse/index.html"

    print("*********** (a) Depth-first search   **********")
    print_dfs(starturl)

    print("*********** (b) Breadth-first search **********")
    print_bfs(starturl)
    print("*********** (c) Find shortest path between two URLs ********")
    find_shortest_path("http://secon.utulsa.edu/cs2123/webtraverse/index.html",
                      "http://secon.utulsa.edu/cs2123/webtraverse/wainwright.html")
    find_shortest_path("http://secon.utulsa.edu/cs2123/webtraverse/turing.html",
                       "http://secon.utulsa.edu/cs2123/webtraverse/dijkstra.html")
    



    print("*********** (d) Find the longest shortest path from a starting URL *****")
    find_max_depth(starturl)

    #P = bfs_parents(starturl)
    #print(P)
