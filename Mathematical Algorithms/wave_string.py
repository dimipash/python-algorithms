def wave_string(s):
    """
    Generates a wave effect by capitalizing each alphabetic character in the string, one at a time.

    Parameters:
    s (str): The input string to create the wave effect on.

    Returns:
    list of str: A list containing each wave variation of the input string.

    Time Complexity: O(N^2), where N is the length of the string.
    Space Complexity: O(N^2), where N is the length of the string.
    """
    wave_list = []
    for i in range(len(s)):
        if s[i].isalpha():
            # Capitalize the i-th character and keep the rest unchanged
            wave = s[:i] + s[i].upper() + s[i + 1 :]
            wave_list.append(wave)
    return wave_list


# Example usage
if __name__ == "__main__":
    input_string = "hello"
    wave_output = wave_string(input_string)
    print("Wave Effect:")
    for wave in wave_output:
        print(wave)
