#Agilan Ampigaipathar (100553054)

#Edit sentence var to search into a different String
sentence = "HELLO user1";
#Prompt user for input to be searched for 
keyword = raw_input("Enter a search term: ");
found = False;
begin = 0;
end = len(sentence);

#Takes in begin and end for recursion later on
def find(begin, end):
  #Base Cases
  #If keyword is found, end the function 
  if(found == True):
    return True;
  #One letter sentence 
  if(begin == end):
    #If keyword matched the sentence
    if(keyword == sentence):
      return True;
    else:
      return False;
  #If keyword is not found yet then divide and conquer     
  if(found == False and begin != end):
    middle = (begin + end) / 2;
    #Recursively call back function for start to middle and middle +1 to end
    left = find(begin,middle);
    right = find(middle+1,end);

    #left Half 
    leftTemp = "";
    firstIndex = 0;
    firstFound = False;
    for i in range(middle):
      #Append to temp string for left half 
      leftTemp += sentence[i];
      if (keyword == leftTemp):
        return True;
      #first index when it matches the first char of the sentence
      if (keyword[0] == sentence[i] and firstFound == False):
        firstIndex = i;
        leftTemp += sentence[firstIndex];
        firstFound = True;
    
    #if keyword is found in the left temp string
    if (keyword in leftTemp):
      return True;

    #right Half
    rightTemp = "";
    lastIndex = 0;
    j = middle + 1;
    for j in range(end):
      rightTemp += sentence[j];
      if (keyword == rightTemp):
        return True;
      if (keyword[:len(sentence)-1] == sentence[j]):
        lastIndex = j;
    
    #if the keyword is in the right string at all
    if(keyword in rightTemp):
      return True;

    if (keyword == sentence[firstIndex:lastIndex]):
      return True;

    if (left == True):
      return True;
    if (right == True):
      return True;

result = find(begin, end);
print(result);

