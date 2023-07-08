

def gcp(p, q :int):
    if q == 0: return p
    r = p % q
    return gcp(q, r)


if __name__ == '__main__':
    print(gcp(7, 5))