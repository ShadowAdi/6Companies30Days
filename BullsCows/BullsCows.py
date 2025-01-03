from collections import Counter
def BullsCowsBrute(secret: str, guess: str) -> str:
    n=len(secret)
    bulls,cows=0,0

    used_secret=[False]*n
    used_guess=[False]*n
    for i in range(n):
        if secret[i]==guess[i]:
            bulls+=1
            used_guess[i]=True
            used_secret[i]=True
    
    for i in range(n):
        if not used_guess[i]:
            for j in range(n):
                if not used_secret[j] and guess[i]==secret[j]:
                    cows+=1
                    used_secret[j]=True
                    break
    
    return f"{bulls}A{cows}B"


def BullsCows(secret: str, guess: str) -> str:
    bulls,cows=0,0

    unmatched_guess=Counter()
    unmatched_secret=Counter()

    for s,g in zip(secret,guess):
        if s==g:
            bulls+=1
        else:
            unmatched_guess[s]+=1
            unmatched_secret[g]+=1
    
    for digit in unmatched_guess:
        if digit in unmatched_secret:
            cows+=min(unmatched_secret[digit],unmatched_guess[digit])
    
    return f"{bulls}A{cows}B"


ans=BullsCows("1807","7810")
print(ans)