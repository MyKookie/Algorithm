class Trie:
    head = {}

    def add(self, word,sign):
        cur = self.head
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        
        cur[sign] = word
        print(word,"has been added to the trie.")

    def search(self, word):
        
        cur = self.head
        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]

        if '*' in cur:
            print(word,'-- stopword')
            
        elif 'p' in cur:
            print(word,'-- positive')
            
        elif '!' in cur:
            print(word,'-- negative')
        


if __name__ =="__main__":   
    tree=Trie()
    
    stopw = []
    posw = []
    negw = []
    MY = []
    fil_1 = open("C:/Users/User/hello/Algorithm/stopword.txt","r")
    fil_2 = open("C:/Users/User/hello/Algorithm/positiveword.txt","r")
    fil_3 = open("C:/Users/User/hello/Algorithm/negativeWords",encoding="utf8")
    article = open("C:/Users/User/hello/Algorithm/MY.txt",encoding="utf8")

    for i in (fil_1.read().split("\n")):
        stopw.append(i)
    for j in (map(lambda x: x.lower(),fil_2.read().split(",  "))):
        posw.append(j)
    for k in (map(lambda x: x.strip(),fil_3.read().split(",   "))):
        negw.append(k)
    # print(stopw)
    # print(posw)
    # print(negw)
    for a in stopw:
        tree.add(a,"*")
        
    for b in posw:
        tree.add(b,"#")
        
    for c in negw:
        tree.add(c,"!")

    for d in map(lambda x: x.strip(),article.read().split(" ")):
        MY.append(d)

    for e in MY:
        tree.search(e)




    
#print (fil_1.read())
#tree.add("fun")
#tree.add("algo")
#tree.searchIn("algorisfunalgoisgreat")

