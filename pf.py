import pyprimesieve as pps
import os.path as ospth

def infintegen(base=1):
    x=base
    while True:
        yield x
        x=x+1

usebase=0
if ospth.exists("primes.out"):
    with open("primes.out","r") as f:
        usebase=len(f.read().split("\n"))

with open("primes.out","a") as pout:
    for n in infintegen(usebase):
        pout.write(str(pps.primes_nth(n))+"\n")
