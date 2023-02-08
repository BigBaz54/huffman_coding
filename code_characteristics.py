def get_average_bit_length(code, freq):
    return sum([len(code[char]) * freq[char] for char in code.keys()]) / sum(freq.values())

def get_variance(code, freq):
    average = get_average_bit_length(code, freq)
    return sum([(len(code[char]) - average) ** 2 * freq[char] for char in code.keys()]) / sum(freq.values())

def is_prefix(code):
    for char in code.keys():
        for other_char in code.keys():
            if char != other_char and code[char].startswith(code[other_char]):
                return False
    return True