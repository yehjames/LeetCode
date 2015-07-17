class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(x):
        resultList=[]
        preZero=True
        finalList=[]
        print(2**32)
        if x ==0:
            return x

        if x >=0:            
            for number in str(x):
                resultList.append(number)

            print(resultList)

            for number in reversed(resultList):
                print("number="+number)
                if (preZero) & (int(number) ==0):
                    print("if preZero & int(number) ==0:")
                    continue
                elif int(number) !=0:
                    print("int(number) !=0:")
                    preZero=False
                    finalList.append(number)
                elif preZero is False and int(number) ==0:
                    print("preZero is False and int(number) ==0:")
                    finalList.append(number)


            print(finalList)
            if int(''.join(finalList)) < 2**31:
                return int(''.join(finalList))
            else:
                return 0

        if x <0:            
            for number in str(abs(x)):
                resultList.append(number)

            print(resultList)
            finalList.append("-")
            for number in reversed(resultList):
                print("number="+number)
                if (preZero) & (int(number) ==0):
                    print("if preZero & int(number) ==0:")
                    continue
                elif int(number) !=0:
                    print("int(number) !=0:")
                    preZero=False
                    finalList.append(number)
                elif preZero is False and int(number) ==0:
                    print("preZero is False and int(number) ==0:")
                    finalList.append(number)

            print(finalList)

            if int(''.join(finalList)) > -(2**31):
                return int(''.join(finalList))
            else:
                return 0


                


    print(reverse(300))
    # print(type(reverse(003)))
    