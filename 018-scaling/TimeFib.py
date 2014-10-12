#!/usr/bin/env python3

from timeit import timeit

def doTest(alg,data):
    for val in data:
        timeSum = timeit("fib{}({})".format(alg,val),setup="from fibonacci import fib{}".format(alg),number=5)
        yield timeSum / 5

def printResTable(alg):
    if not 1 <= alg <= 2:
        raise ValueError("Algorithm must be 1 or 2")

    modifier = 10 if alg == 1 else int(10e3)
    data = [x * modifier for x in range(1, 5)]

    headingCells = "".join(["<th>n = {}</th>".format(x * modifier) for x in range(1,5)])
    result = "".join(["<td>{:.4}</td>".format(round(res,4)) for res in list(doTest(alg,data))])

    heading = "<table border="1"><thead><tr><th></th><th colspan=\"4\" align=\"center\">Seconds taken to find the nth Fibonacci number</th></tr>"
    subHeading = "<tr><th>Algorithm</th>" + headingCells  + "</tr></thead>"
    resLine = "<tbody><tr><td>fib{}</td>".format(alg) + result + "</tr></tbody></table>"
    filename = "Fib{}Results.html".format(alg)

    with open(filename,'w') as log:
        log.write("{}\n{}\n{}\n".format(heading,subHeading,resLine))

if __name__ == '__main__':
    printResTable(1)
    printResTable(2)
