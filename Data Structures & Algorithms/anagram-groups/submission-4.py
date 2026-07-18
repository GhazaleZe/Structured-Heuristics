class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        mymap = {}
        for i in strs:
            c = list(i)
            c.sort()
            if tuple(c) in mymap:
                mymap[tuple(c)].append(i)
            else:
                mymap[tuple(c)] = [i]

        for val in mymap.values():
            result.append(val)
        return result           


            