import sys
import res
def draw(gun,man):
    global_line = []
    for line in range(16):
        global_line.extend(''.join(gun[line]+(' '*40)+man[line]+'H'))
    global_line = denester(global_line,16,len(global_line)/16)
    score = 123
    
    print('-'*((len(global_line[1])-len(str(score))-2)//2)+' '+str(score)+' '+'-'*((len(global_line[1])-len(str(score))-2)//2))

    for each in global_line:
        print(each)

def denester(asciistr,height,width):
    '''
    (string,int) -> list
    function slices an ascii docstring image into string lines
    >>> denester([--+--X\n--+--X],2)
    [['-', '-', '+', '-', '-'], ['-', '-', '+', '-', '-']]
    '''
    output_list = []
    asciistr = list(asciistr)
    width = len(asciistr)/height
    print(width)
    i = 1
    ch = 0
    while i <= height:
        line = []
        while ch < width:
            if (asciistr[ch] == 'H'):
                break
            elif (asciistr[ch] != '\n'):
                line.append(asciistr[ch])
            ch += 1
        ch += 1
        i += 1
        width *=2
        output_list.append(''.join(line))
    return output_list
