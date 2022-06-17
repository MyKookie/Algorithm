# KMP Algorithm
def KMP(pat, txt):
    X = len(pat)
    Y = len(txt)
 
    # longest prefix suffix
    lps = [0]*X
    j = 0 # index for pat[]
 
    # Preprocess the pattern
    computeLPSArray(pat, X, lps)
 
    i = 0 # index for txt[]
    while i < Y:
        if pat[j] == txt[i]:
            i += 1
            j += 1
 
            if j == X:
                print ("index " + str(i-j))
                j = lps[j-1]
 
        # mismatch after j matches
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
 
def computeLPSArray(pat, X, lps):
    len = 0 # length of the previous longest prefix suffix
 
    lps[0] # lps[0] is always 0
    i = 1
 
    #calculates lps[i] for i = 1 to X-1
    while i < X:
        if pat[i]== pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len-1]
 
            else:
                lps[i] = 0
                i += 1
 
txt = "algorisfunalgoisgreat"
word1 = "algo"
word2 = "fun"
print("algorisfunalgoisgreat")
print("Found word 'algo' and 'fun' at:")
KMP(word1, txt)
KMP(word2, txt)