from itertools import permutations, combinations


def permute(s):
    """Generate all permutations of a string recursively."""
    if len(s) <= 1:
        return [s]
    perms = permute(s[1:])
    char = s[0]
    result = []
    for perm in perms:
        for i in range(len(perm) + 1):
            result.append(perm[:i] + char + perm[i:])
    return result


def combine(s, r):
    """Generate all combinations of r characters from the string."""
    if r == 0:
        return [""]
    if r > len(s):
        return []
    return [s[0] + comb for comb in combine(s[1:], r - 1)] + combine(s[1:], r)


def rotate_string(s, k):
    """Rotate the string k positions to the right."""
    if not s:
        return ""
    k = k % len(s)
    return s[k:] + s[:k]


def reverse_string(s):
    """Reverse the string."""
    return s[::-1]


def alternate_chars(s):
    """Rearrange string to alternate vowels and consonants."""
    vowels = "".join([c for c in s if c in "aeiouAEIOU"])
    consonants = "".join([c for c in s if c not in "aeiouAEIOU"])
    result = []
    v, c = 0, 0
    for i in range(len(s)):
        if i % 2 == 0 and v < len(vowels):
            result.append(vowels[v])
            v += 1
        elif c < len(consonants):
            result.append(consonants[c])
            c += 1
        else:
            (
                result.append(vowels[v])
                if v < len(vowels)
                else result.append(consonants[c])
            )
    return "".join(result)


def generate_anagrams(s):
    """Generate all unique anagrams of the string."""
    return set("".join(p) for p in permutations(s))


def lexicographic_permutations(s):
    """Generate permutations in lexicographic order."""
    return sorted("".join(p) for p in permutations(s))


def largest_number(s):
    """Rearrange digits to form the largest possible number."""
    if not s.isdigit():
        raise ValueError("Input string must contain only digits.")
    return "".join(sorted(s, reverse=True))


# Example usage
if __name__ == "__main__":
    s = "abc"
    print("Permutations:", permute(s))
    print("Combinations (2 at a time):", combine(s, 2))
    print("Rotate string by 2:", rotate_string(s, 2))
    print("Reverse string:", reverse_string(s))
    print("Alternate characters:", alternate_chars(s))
    print("Anagrams:", generate_anagrams(s))
    print("Lexicographic permutations:", lexicographic_permutations(s))
    num_str = "3412"
    print("Largest number from digits:", largest_number(num_str))
