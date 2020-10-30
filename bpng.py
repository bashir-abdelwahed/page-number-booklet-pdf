import sys

"""
booklet page number generator program to be used with EVINCE:
if you want to print a booklet, follow the steps described in this link:
https://help.gnome.org/users/gnome-help/stable/printing-booklet-duplex.html.en
https://help.gnome.org/users/evince/stable/duplex-npage.html.en
and use this little useful function
"""

def generate_booklet_seq(pages):
    assert(pages % 4 == 0)
    ind = []
    for i in range(0, pages/4):
        ind.append(pages - 2*i)
        ind.append(2*i + 1)
        ind.append(2*i + 2)
        ind.append(pages - 2*i -1)
    
    return ','.join([str(i) for i in ind])


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("program usage: ./bpng #pages \nOr python bpng.py #pages")
        exit()
    try:
        int(sys.argv[1])
    except ValueError:
        print("#pages must be a positive integer")
        exit()
    print("copy and paste the following line in the pages area:")
    print(generate_booklet_seq(int(sys.argv[1])))
