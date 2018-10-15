# python2

def read_input():
    return (raw_input().rstrip(), raw_input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def rabin_karp(pattern, text):
    p = 100000009
    x = 2
    P = len(pattern)
    y = (x**P) % p
    T = len(text)
    result = []

    def _hash_func(s):
        ans = 0
        for c in reversed(s):
            ans = (ans * x + ord(c)) % p
        return ans

    def _precompute(t):
        hash_list = [None]*(T-P+1)
        i0 = T-P+1
        last_hash = _hash_func(t[i0-1:i0+P-1])
        hash_list[i0-1] = last_hash
        for index in range(i0-1, 0, -1):
            new_hash = (x*last_hash +  (ord(t[index-1]) - ord(t[index-1+P])*y))%p
            hash_list[index-1] = new_hash
            last_hash = new_hash


        return hash_list

    hashP = _hash_func(pattern)
    hash_list = _precompute(text)

    # for idx, val in enumerate((hash_list)):
    #     if val == hashP:
    #         result.append(idx)

    idx = 0
    for i in hash_list:
        if i == hashP:
            result.append(idx)
        idx += 1


    return result



if __name__ == '__main__':
    print_occurrences(rabin_karp(*read_input()))
