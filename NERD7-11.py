# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
    output = ""
    curr = root
    for num in s:
        if num == "0":
            curr = curr.left
        elif num == "1":
            curr = curr.right
        if curr.data != '\0':
            output = output + curr.data
            curr = root
    print(output)
