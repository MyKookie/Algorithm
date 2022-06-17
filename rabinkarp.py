# Rabin Karp Algorithm
 
# d is the number of characters in the input alphabet
d = 256

# pat  -> pattern
# txt  -> text
# q    -> A prime number
 
def search(pat, txt, q):
    M = len(pat)
    N = len(txt)
    i = 0          # counter
    j = 0          # counter
    hash_p = 0    # hash value for pattern
    hash_t = 0    # hash value for txt
    h = 1          # initial value
 
    # The value of h would be "pow(d, M-1)%q"
    # 'mod q' is done to prevent overflow
    for i in range(M-1):
        h = (h*d)%q
 
    # Calculate the hash value of pattern and first window of text
    # ord() : function returns a integer representing the Unicode character 
    for i in range(M):
        hash_p = (d*hash_p + ord(pat[i]))%q
        hash_t = (d*hash_t + ord(txt[i]))%q
 
    # Slide the pattern over text one by one
    for i in range(N-M+1):
        # Check the hash values of current window of text and
        # pattern if the hash values match then only check
        # for characters one by one
        if hash_p==hash_t:
            # Check for characters one by one
            for j in range(M):
                if txt[i+j] != pat[j]:
                    break
                else: j+=1
 
            # if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
            if j==M:
                print ("Pattern found at index " + str(i))
 
        # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
        if i < N-M:
            # ((d (t - txt[character to be removed] * h) + txt[character to be added] ) mod q
            hash_t = (d*(hash_t-ord(txt[i])*h) + ord(txt[i+M]))%q
 
            # We might get negative values of t, converting it to
            # positive
            if hash_t < 0:
                hash_t = hash_t+q
 
# Driver Code
txt = "algorisfunalgoisgreat"
pat1 = "fun"
pat2 = "great" 
# A prime number
q = 101
 
# Function Call
print('First Pattern:')
search(pat1,txt,q)
print('Second Pattern:')
search(pat2,txt,q)