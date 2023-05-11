def lltonum(ll):
    i = 10 **(len(ll)-1)
    n=0
    for e in ll:
        n=n+i*int(e)
        i=i/10
    return int(n)
print(lltonum(['4','3','9','2']))

from functools import reduce 
def passar_a_numero(digits):
    return reduce(lambda x,y:x*10+y,digits)
print(passar_a_numero([4,3,9,2]))