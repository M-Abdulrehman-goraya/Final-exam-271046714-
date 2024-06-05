def recursion(a,binary = ""):
    if a==0:
        return binary
    else:
        binary = str(a%2) + binary
        return recursion(a//2,binary)
output = recursion(7)
print(output)