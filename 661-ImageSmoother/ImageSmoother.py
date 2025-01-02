from typing import List
def ImageSmoother(img: List[List[int]])->List[List[int]]:
    ROWS,COLS=len(img),len(img[0])
    res=[[0]*COLS for _ in range(ROWS)]


    for r in range(ROWS):
        for c in range(COLS):
            total,cnt=0,0
            for i in range(r-1,r+2):
                for j in range(c-1,c+2):
                    if i==ROWS or i<0 or j==COLS or j<0:
                        continue
                    total+=img[i][j]
                    cnt+=1
            res[r][c]=total//cnt
    return res

ans=ImageSmoother([[1,1,1],[1,0,1],[1,1,1]])

print("Answer is: ",ans)