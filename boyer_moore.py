def bad_char_heuristic(pattern):
    bad_char = {}
    for i in range(len(pattern)):
        bad_char[pattern[i]] = i
    return bad_char

def good_suffix_heuristic(pattern):
    m = len(pattern)
    border_pos = [0] * (m + 1)
    shift = [0] * (m + 1)
    
    # Case 1: The matching suffix occurs somewhere else in pattern
    i = m
    j = m + 1
    border_pos[i] = j
    
    while i > 0:
        while j <= m and pattern[i - 1] != pattern[j - 1]:
            if shift[j] == 0:
                shift[j] = j - i
            j = border_pos[j]
        i -= 1
        j -= 1
        border_pos[i] = j
        
    # Case 2: Only a part of the matching suffix occurs at the beginning
    j = border_pos[0]
    for i in range(m + 1):
        if shift[i] == 0:
            shift[i] = j
        if i == j:
            j = border_pos[j]
            
    return shift

def boyer_moore_search(text, pattern):
    n = len(text)
    m = len(pattern)
    
    bad_char = bad_char_heuristic(pattern)
    good_suffix = good_suffix_heuristic(pattern)
    
    s = 0  # s is shift of the pattern with respect to text
    results = []
    
    while s <= n - m:
        j = m - 1
        
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
            
        if j < 0:
            results.append(s)
            s += good_suffix[0]
        else:
            s += max(good_suffix[j + 1], j - bad_char.get(text[s + j], -1))
            
    return results

# Example usage:
if __name__ == "__main__":
    text = "ABAAABCDABC"
    pattern = "ABC"
    
    print(f"Searching for '{pattern}' in '{text}'")
    matches = boyer_moore_search(text, pattern)
    
    if matches:
        print("Pattern found at indices:", matches)
    else:
        print("Pattern not found")
