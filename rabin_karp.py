class RabinKarp:
    def __init__(self):
        self.base = 29
        self.prime = 99991 # Big prime number for hash calculations

    def search(self, pattern, text):
        if not pattern or not text:
            raise ValueError("No Pattern or Text found")

        pattern_len = len(pattern)
        text_len = len(text)

        if pattern_len > text_len: # if pattern to long return empty list
            return []

        hash_pattern = 0
        hash_text = 0
        h = 1
        result = []

        for _ in range(pattern_len - 1):
            h = (h * self.base) % self.prime

        for i in range(pattern_len):
            # Calc hash values for pattern and text
            hash_pattern = (self.base * hash_pattern + ord(pattern[i])) % self.prime
            hash_text = (self.base * hash_text + ord(text[i])) % self.prime


        # Move pattern through text
        for i in range(text_len - pattern_len +1):
            if hash_pattern == hash_text: # Check if pattern and text match approximately
                if pattern == text[i:i + pattern_len]: # Character by character comparison for exact match
                    result.append(i)

            # Calc hash for next text block
            if i < text_len - pattern_len:
                hash_text = self.get_rolling_hash_value(text[i + 1:i + pattern_len + 1], text[i], hash_text)

        return result

    def get_rolling_hash_value(self, sequence, last_character, previous_hash):
        if last_character == '\0':
            # Initial hash calculation
            hash_value = 0
            for char in sequence:
                hash_value = (self.base * hash_value + ord(char)) % self.prime
            return hash_value
        else:
            # Rolling hash calculation
            removed = (ord(last_character) * pow(self.base, len(sequence) - 1, self.prime)) % self.prime
            hash_rolling = ((previous_hash - removed) * self.base + ord(sequence[-1])) % self.prime

            return hash_rolling

if __name__ == "__main__":
    rk = RabinKarp()
    text = "AbCdExxx, Xxxxxke"
    pattern = "xxx"
    result = rk.search(pattern, text)
    print(result)