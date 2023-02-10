import random

def split_string(w):
    result = [(w,)]
    w_len = len(w)
    if w_len == 1:
        return result
    else:
        for i in range(1, w_len):
            post_segments = split_string(w[i:])
            for seg in post_segments:
                result.append((w[:i],) + seg)
    return result
result = split_string("abcdefghijkl")
print(len(result))

    