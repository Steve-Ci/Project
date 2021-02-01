import sys
def main():
    vals =[]
    for val in sys.argv:
        vals.append(val)
    print(vals)
    punctuation =""
    if '-q' in vals:
        punctuation ="?"
    elif '-Q' in vals:
        punctuation = '!?'
    else:
        punctuation ="!"
    if '-n' in vals:
        flaq=vals.index('-n')
        num = vals[flaq+1]
        print(f'Hello! ,{vals[-1]}{punctuation*int(num)}')
    else:
        print(f'Hello! ,{vals[-1]}{punctuation}')
main()
