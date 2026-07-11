class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        cleaned = ""
        for ch in paragraph:
            if ch.isalpha():
                cleaned += ch.lower()
            else:
                cleaned += " "
        p=cleaned.split()
        h=[]
        for i in banned:
            h.append(i)
        
        d={}
        c=0
        
        for para in p:
            if para not in h:
                if para not in d:
                    d[para]=1
                elif para in d:
                    d[para]+=1
        print(d)
        wc=''
        maxc=0
        for w,c in d.items():
            if c>maxc:
                wc=w
                maxc=c
        return wc

