
def superReducedString(S):
    s=list(S)
    x=""
    prev=0
    curr=0
    nxt=1
    while(curr<len(s) and nxt<len(s)):
        if s[curr]==s[nxt] :
            if curr==0:
                del s[curr]
                del s[curr]
            elif (nxt<len(s)-1):
                del s[curr]
                del s[curr]
                if curr>0:
                    curr=curr-1
                    nxt=nxt-1
            else:
                del s[curr]
                del s[curr]
        else:
            curr=nxt
            nxt=nxt+1
    x=""
    for i in s:
        x=x+i
    print(x)



superReducedString("baab")
