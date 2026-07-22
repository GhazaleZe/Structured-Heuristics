class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        ind = len(digits)-1
        for i in digits:
            num += i * (10 **ind)
            ind -=1
        num +=1
        numliststr = list(str(num))
        
        # for j in range(len(numliststr )):
        #     result.append(int(numliststr[j]))
        return list(map(int, numliststr))

