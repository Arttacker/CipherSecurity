simple_leet_dict = {
    'A': '4', 'B': '8', 'C': 'C', 'D': 'D', 'E': '3',
    'F': 'F', 'G': '6', 'H': 'H', 'I': '1', 'J': 'J',
    'K': 'K', 'L': '1', 'M': 'M', 'N': 'N', 'O': '0',
    'P': 'P', 'Q': 'Q', 'R': 'R', 'S': '5', 'T': '7',
    'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y',
    'Z': '2',
}

# Reverse the simple leet dictionary to create a decoding dictionary
simple_decode_dict = {v: k for k, v in simple_leet_dict.items()}

complex_leet_dict = {
    'A': '4', 'B': '8', 'C': '<', 'D': '|)', 'E': '3',
    'F': '|=', 'G': '6', 'H': '#', 'I': '!', 'J': '_|',
    'K': '|<', 'L': '1', 'M': r'|\/|', 'N': r'|\|', 'O': '0',
    'P': '|*', 'Q': '0_', 'R': '|2', 'S': '5', 'T': '7',
    'U': '|_|', 'V': r'\/', 'W': r'\^/', 'X': '><', 'Y': '`/',
    'Z': '2'
}

# Reverse the dictionary to create a decoding dictionary
decode_dict = {v: k for k, v in complex_leet_dict.items()}


def simple_leet_encode(text: str) -> str:
    return "".join(simple_leet_dict.get(c.upper(), c) for c in text).upper()


def simple_leet_decode(text: str) -> str:
    return "".join(simple_decode_dict.get(c.upper(), c) for c in text).upper()


def complex_leet_encode(text: str) -> str:
    return "".join(complex_leet_dict.get(c.upper(), c) for c in text)


def complex_leet_decode(text: str) -> str:
    i = 0
    decoded_text = ''
    while i < len(text):
        # Try to match multi-character leet symbols first
        for length in range(4, 0, -1):
            if i + length <= len(text) and text[i:i + length] in decode_dict:
                decoded_text += decode_dict[text[i:i + length]]
                i += length
                break
        else:
            # If no match, just add the original character
            decoded_text += text[i]
            i += 1
    return decoded_text
