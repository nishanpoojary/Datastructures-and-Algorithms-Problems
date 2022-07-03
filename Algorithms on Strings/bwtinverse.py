# python3

def last_to_first(s):
    counts = {'$': 0, "A": 0, 'C': 0, 'G': 0, 'T': 0}
    for char in s:
        counts[char] += 1
    temp = -1
    position = {}
    for t in ['$', 'A', 'C', 'G', 'T']:
        temp += counts[t]
        position[t] = temp
    array = [0] * len(s)
    for i in range(len(s)-1, -1, -1):
        array[i] = position[s[i]]
        position[s[i]] -= 1
    return array

def invert_bwt(s):
    ltf = last_to_first(s)
    result = '$'
    pos = 0
    for i in range(len(s) - 1):
        result += s[pos]
        pos = ltf[pos]
    result = result[::-1]
    return result

if __name__ == '__main__':
    bwt = input()
    print(invert_bwt(bwt))