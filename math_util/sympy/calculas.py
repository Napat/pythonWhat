import re
import sympy as sp
    
def convertpowereq(pwstr="**3"):
    pwstr = pwstr.replace('*', '')
    pwstr = pwstr.replace('0', '⁰')
    pwstr = pwstr.replace('1', '¹')
    pwstr = pwstr.replace('2', '²')
    pwstr = pwstr.replace('3', '³')
    pwstr = pwstr.replace('4', '⁴')
    pwstr = pwstr.replace('5', '⁵')
    pwstr = pwstr.replace('6', '⁶')
    pwstr = pwstr.replace('7', '⁷')
    pwstr = pwstr.replace('8', '⁸')
    pwstr = pwstr.replace('9', '⁹')
    return pwstr
    
def searchstridx(rs, pattern):
    idxsearch = 0
    idxreplaces = []
    while True:
        #print(rs[idxsearch:])
        idxfound = rs[idxsearch:].find(pattern)
        if idxfound == -1:
            return idxreplaces
        else:
            idxreplaces.append(idxsearch+idxfound)
            idxsearch = idxsearch + idxfound + 3

def prettystr_polynomeq(rs):
    if len(rs) < 2:
        return rs

    idxreplaces = searchstridx(rs, "**")
    #print(f"idx replaces: {idxreplaces}")
   
    powernums = re.findall(r'\*\*\d+', rs)  # match "**number"
    #print(f"power: {powernums}")

    # Replace number after "**n" with 'ⁿ'
    for idx, idxreplace in reversed(list(enumerate(idxreplaces))):
        replace_len = len(powernums[idx])
        rs = rs[0:idxreplace] + convertpowereq(powernums[idx]) + rs[idxreplace+replace_len:]
        #print(f"{idx}: {rs}")

    # Remove multiply sign
    rs = rs.replace("*", "")
    return rs

def integrate_solve(problem, symbol):
    return str(sp.integrate(problem, symbol))

print("-------- pretty polynomial equation")
print(prettystr_polynomeq('x'))
print(prettystr_polynomeq('2*x'))
print(prettystr_polynomeq('2'))
print(prettystr_polynomeq('x**8+x**9'))
print(prettystr_polynomeq('4*x**10+x**9+10'))
print(prettystr_polynomeq('99*x**8+x**6'))

print("-------- integrate_solve")
symbol = sp.Symbol('x')
problem = '5*x**10 + 2*x**4 + 5*x**3 + 2'
result = integrate_solve(problem, symbol)

ppproblem = prettystr_polynomeq(problem)
ppresult = prettystr_polynomeq(result)
print(f"problem {problem}\n\r\t {ppproblem}")
print(f"result {result}\n\r\t {ppresult}")
print(f"∫ ({ppproblem}) dx = {ppresult}")
