
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded =[]
        string_ord =""
        result = ""
        for c in strs:
            cl = list(c)
            code = [5] * len(cl)
            for i in range(len(cl)):
                string_ord += (chr(ord(cl[i])+code[i]))
            
            encoded.append(string_ord)
            result = result +"##:"+ string_ord
            string_ord = ""
        result += "##:"
        return result

    def decode(self, s: str) -> List[str]:
            decoded =[]
            string_ord =""
            code = [5] * len(s)
            c =3
            while c < len(s):
                if s[c:c+3] == "##:":
                    # print(c)
                    # print(s[c:c+3])
                    decoded.append(string_ord)
                    string_ord = ""
                    c +=3
                else:

                    string_ord += (chr(ord(s[c]) - code[c]))
                    c+=1
                    
            return decoded