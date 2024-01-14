import webbrowser

f = open("songlist.txt", 'r')

for song in (f.readlines()):
    webbrowser.open('http://www.google.com/search?q=' + song)