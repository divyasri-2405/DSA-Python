#back tracking with binary numbers
n=int(input("Enter n: "))
def backtrack(s):
    if len(s)==n:
        print(s)
        return
    backtrack(s+'0')
    backtrack(s+'1')
backtrack('')
