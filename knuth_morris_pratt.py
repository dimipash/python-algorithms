def compute_lps_array(pattern):
    l = 0  # length of the previous longest prefix suffix
    lps = [0] * len(pattern)
    
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[l]:
            l += 1
            lps[i] = l
            i += 1
        else:
            if l != 0:
                l = lps[l - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    
    lps = compute_lps_array(pattern)
    
    i = 0  # index for text
    j = 0  # index for pattern
    results = []
    
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
            
            if j == m:
                results.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
                
    return results

# Example usage:
if __name__ == "__main__":
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    
    print(f"Searching for '{pattern}' in '{text}'")
    matches = kmp_search(text, pattern)
    
    if matches:
        print("Pattern found at indices:", matches)
    else:
        print("Pattern not found")
