
class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(s, numRows):
        
        i=0
        outputList=[]
        finalList=[]

        # initail 
        for row in range(numRows):  
            outputList.append([])

        #when s is empty return empty string  
        if s == "":
            return s
        #when  numRows =1 return original string
        elif numRows == 1:  
            return s
        #when  the length of s is less than numRows then return original string
        elif len(s) <= numRows:
            return s
        else:
            for char in s:
                # use 2*numRows-2 as a cylce period
                if i%(2*numRows-2) < numRows:
                    outputList[(i%(2*numRows-2))].append(char)

                elif i%(2*numRows-2) >= numRows:
                    tmp= (i%(2*numRows-2) - (((i%(2*numRows-2))-(numRows-1))*2))                    
                    outputList[tmp].append(char)

               i = i+1
                
            for row in range(numRows):  
                for char in outputList[row]:
                    finalList.append(char)

            return ''.join(finalList)

    print(convert("PAYPALISHIRING", 3))