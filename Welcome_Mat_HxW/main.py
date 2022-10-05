
def build_mat(height: int, width: int):

    welcome = "WELCOME"

    inc = True
    count = 1
    arr = []
    for h in range(int(height / 2)):
        s = ''.join(['-' for i in range(int(((width - (3 * count)) / 2)))])
        ss = ''.join(['.|.' for i in range(count)])
        arr.append(s + ss + s)
        count += 2

    string = ''
    for i in arr:
        string += i + '\n'

    s = ''.join(['-' for i in range(int(((width - len(welcome)) / 2)))])
    string += s + welcome + s

    arr.reverse()

    for i in arr:
        string += '\n' + i

    retur n(string)

if __name__ == '__main__':
    h, w = [int(i) for i in input().split()]
    output = build_mat(h, w)
    print(output)