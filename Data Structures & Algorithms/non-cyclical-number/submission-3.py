class Solution:
    def isHappy(self, n: int) -> bool:

        set_check = set()
        num = 0
        while num != 1:
            c = str(n)
            list_it = list(c)
            num = 0
            print(list_it)
            for i in list_it:
                print(num,i,int(i),int(i)**2)
                num += (int(i)**2)
                print("num", num)
            if num == 1:
                return True
            elif num in set_check:
                return False
            else:
                set_check.add(num)
                n = num
        

        