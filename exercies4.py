import sys

def main():
    # flags=[]
    flags1=" "
    reverse = False
    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-r':
            reverse = True

        elif '-' in sys.argv[i]:
            # flags.append(sys.argv[i][1:])
            flags1 +=str(sys.argv[i][1:])
    if reverse:
        print(flags1[-1:])
    else:
        print(flags1)

    #print(flags)



main()
