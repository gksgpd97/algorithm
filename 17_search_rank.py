#혼자 절대 못품
import bisect

lg = ["cpp","java","python"]
work = ["backend", "frontend"]
career = ["senior", "junior"]
food = ["pizza","chicken"]

def calc(table, a, b, c, d, e):
    rst = 0
    if a == '-':
        for item in lg:
            rst+=calc(table,item,b,c,d,e)
    elif b == '-':
        for item in work:
            rst+=calc(table,a,item,c,d,e)
    elif c == '-':
        for item in career:
            rst+=calc(table,a,b,item,d,e)
    elif d == '-':
        for item in food:
            rst+=calc(table,a,b,c,item,e)
    else:
        idx = bisect.bisect_left(table[a][b][c][d], e)
        rst = len(table[a][b][c][d])-idx
    return rst
def solution(info, query):
    answer = []
    table = {}
    for a in lg:
        table[a]={}
        for b in work:
            table[a][b]={}
            for c in career:
                table[a][b][c]={}
                for d in food:
                    table[a][b][c][d]=[]
    for s in info:
        a,b,c,d,e = s.split()
        table[a][b][c][d].append(int(e))    
    
    for a in lg:
        for b in work:
            for c in career:
                for d in food:
                    table[a][b][c][d].sort()
                    
    for q in query:
        a, aa, b, bb, c, cc, d, e = q.split()
        answer.append(calc(table, a,b,c,d,int(e)))
    
    #print(table)
    return answer