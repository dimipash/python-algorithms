def build_suffix_array(text):
    n = len(text)
    suffixes = sorted([(text[i:], i) for i in range(n)])
    suffix_array = [suffix[1] for suffix in suffixes]
    return suffix_array

def lcp_array(text, suffix_array):
    n = len(text)
    rank = [0] * n
    lcp = [0] * n

    for i, suffix in enumerate(suffix_array):
        rank[suffix] = i

    h = 0
    for i in range(n):
        if rank[i] > 0:
            j = suffix_array[rank[i] - 1]
            while i + h < n and j + h < n and text[i + h] == text[j + h]:
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1
    return lcp

# Example usage:
if __name__ == "__main__":
    text = "banana"
    suffix_array = build_suffix_array(text)
    lcp = lcp_array(text, suffix_array)

    print("Suffix Array:", suffix_array)
    print("LCP Array:", lcp)
