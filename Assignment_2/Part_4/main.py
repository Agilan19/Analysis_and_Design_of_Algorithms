#Agilan Ampigaipathar(100553054)

#Read from the file 
file = open('sample.txt', 'r') 
data = file.read()
file.close()
print data

#Get the frequency for each character 
def frequency (str):
    freqs = {}
    for ch in str:
        freqs[ch] = freqs.get(ch,0) + 1
    return freqs

freq = frequency(data)
print freq;

#Sort the keys in order of frequency of letter 
def sortFreq (freqs):
    letters = freqs.keys()
    tuples = []
    for let in letters:
        tuples.append((freqs[let],let))
    tuples.sort()
    return tuples

sort = sortFreq(freq);
print sort

def buildTree(tuples):
    while len(tuples) > 1:
        #Get the branches 
        leastTwo = tuple(tuples[0:2])                  
        #Get the other 
        theRest  = tuples[2:]     
        #Branch point frequency 
        combFreq = leastTwo[0][0] + leastTwo[1][0]
        #Adding branch point to end 
        tuples   = theRest + [(combFreq,leastTwo)] 
        #Sort them
        tuples.sort() 
    #Return as one tree
    return tuples[0]            

def trimTree (tree):
    #Trim for only letters
    p = tree[1]                                    
    #Ignore frequency count in first index 
    if type(p) == type("") : return p              
    #If only a leave, return it
    #Trim from left to right then put them together
    else : return (trimTree(p[0]), trimTree(p[1])) 

tree = buildTree(sort)
trim = trimTree(tree)
print trim

def assignCodes (node, pat=''):
    fileSize = 0
    conv = bin(fileSize)
    global codes
    codes = {}

    if type(node) == type(""):
        #Leaf
        codes[node] = pat    

        num = ' '.join(format(ord(x), 'b') for x in pat)
        if isinstance(pat, bytes):
          conv += num        
    else:                            
        #Branch point going left  
        assignCodes(node[0], pat+"0")    
        #Go right branch
        assignCodes(node[1], pat+"1")

        num = ' '.join(format(ord(x), 'b') for x in pat)
        if isinstance(pat, bytes):
          conv += num

    print "Compressed Size:", conv



assignCodes(trim)
print codes

def origFileSize(fileContent):
  return len(data) * 8;

origSize = origFileSize(data)
print "Original Size:", origSize
