import time


def main():
    string_A = 'Carthorse'
    string_B = 'Orchestra'

    def R(idx_a, idx_b, cache={}):
        if (idx_a, idx_b) in cache:
            return cache[(idx_a, idx_b)]

        while idx_a > -1 and idx_b > -1 and string_A[idx_a] == string_B[idx_b]:
            idx_a, idx_b = idx_a - 1, idx_b - 1

        if idx_a < 0:
            return idx_b + 1
        elif idx_b < 0:
            return idx_a + 1
        else:
            cache[(idx_a, idx_b)] = 1 + \
                min(R(idx_a, idx_b - 1), R(idx_a - 1, idx_b - 1), R(idx_a - 1, idx_b))

        return cache[(idx_a, idx_b)]

    start = time.time()
    ans = R(len(string_A) - 1, len(string_B) - 1)
    print(f'Time taken: {time.time()-start}\nAnswer: {ans}')


if __name__ == "__main__":
    main()
