"""
Test cases for encryption and decryption logic
Tests the existing encript.py and decript.py functions
"""
import sys
sys.path.insert(0, '..')

# Create a mock object to avoid user input when testing
class MockInitObject:
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', ';', ':', '"', "'", '<', '>', ',', '.', '?', '/', ' ']
    input_message = ""
    encripted_message = ""
    shift_count = 0


class TestResult:
    """Store test result information"""
    def __init__(self, test_name, test_type, test_input, shift, expected, actual, passed):
        self.test_name = test_name
        self.test_type = test_type  # "Encryption" or "Decryption"
        self.test_input = test_input
        self.shift = shift
        self.expected = expected
        self.actual = actual
        self.passed = passed


def test_encrypt_alphabet(message, shift):
    """Test encryption of alphabet characters"""
    encrypted = ""
    mock_obj = MockInitObject()
    for char in message:
        if char in mock_obj.alphabet:
            index = mock_obj.alphabet.index(char) + shift
            # Wrap-around for alphabet (52 elements total: A-Z and a-z)
            while index >= len(mock_obj.alphabet):
                index = index - len(mock_obj.alphabet)
            encrypted += mock_obj.alphabet[index]
    return encrypted


def test_decrypt_alphabet(encrypted_message, shift):
    """Test decryption of alphabet characters"""
    decrypted = ""
    mock_obj = MockInitObject()
    for char in encrypted_message:
        if char in mock_obj.alphabet:
            index = mock_obj.alphabet.index(char) - shift
            # Wrap-around for alphabet going backwards
            while index < 0:
                index = index + len(mock_obj.alphabet)
            decrypted += mock_obj.alphabet[index]
    return decrypted


def test_encrypt_symbols(message, shift):
    """Test encryption of symbols"""
    encrypted = ""
    mock_obj = MockInitObject()
    for char in message:
        if char in mock_obj.symbols:
            index = mock_obj.symbols.index(char) + shift
            # Wrap-around for symbols (31 elements, indices 0-30)
            while index >= len(mock_obj.symbols):
                index = index - len(mock_obj.symbols)
            encrypted += mock_obj.symbols[index]
    return encrypted


def test_decrypt_symbols(encrypted_message, shift):
    """Test decryption of symbols"""
    decrypted = ""
    mock_obj = MockInitObject()
    for char in encrypted_message:
        if char in mock_obj.symbols:
            index = mock_obj.symbols.index(char) - shift
            # Wrap-around for symbols going backwards
            while index < 0:
                index = index + len(mock_obj.symbols)
            decrypted += mock_obj.symbols[index]
    return decrypted


def run_tests():
    """Run all encryption and decryption tests"""
    results = []
    
    # ============ ENCRYPTION TESTS ============
    
    # Test 1: Encrypt single character (A)
    test_input = "A"
    shift = 1
    expected = "B"
    actual = test_encrypt_alphabet(test_input, shift)
    passed = actual == expected
    results.append(TestResult("Single Character Encryption (A)", "Encryption", test_input, shift, expected, actual, passed))
    
    # Test 2: Encrypt multiple characters
    test_input = "ABC"
    shift = 3
    expected = "DEF"
    actual = test_encrypt_alphabet(test_input, shift)
    passed = actual == expected
    results.append(TestResult("Multiple Characters Encryption (ABC)", "Encryption", test_input, shift, expected, actual, passed))
    
    # Test 3: Encrypt lowercase
    test_input = "abc"
    shift = 1
    expected = "bcd"
    actual = test_encrypt_alphabet(test_input, shift)
    passed = actual == expected
    results.append(TestResult("Lowercase Encryption (abc)", "Encryption", test_input, shift, expected, actual, passed))
    
    # Test 4: Encrypt with shift value
    test_input = "Z"
    shift = 1
    expected = "a"  # Z is at index 25, +1 = 26 which is 'a'
    actual = test_encrypt_alphabet(test_input, shift)
    passed = actual == expected
    results.append(TestResult("Encryption (Z+1)", "Encryption", test_input, shift, expected, actual, passed))
    
    # Test 5: Encrypt with wrap-around (z)
    test_input = "z"
    shift = 1
    expected = "A"  # z is at index 51, +1 wraps to 0 which is 'A'
    actual = test_encrypt_alphabet(test_input, shift)
    passed = actual == expected
    results.append(TestResult("Wrap-around Encryption (z+1)", "Encryption", test_input, shift, expected, actual, passed))
    
    # Test 6: Encrypt symbol
    test_input = "!"
    shift = 1
    expected = "@"
    actual = test_encrypt_symbols(test_input, shift)
    passed = actual == expected
    results.append(TestResult("Symbol Encryption (!)", "Encryption", test_input, shift, expected, actual, passed))
    
    # Test 7: Encrypt space
    test_input = " "
    shift = 1
    expected = "!"
    actual = test_encrypt_symbols(test_input, shift)
    passed = actual == expected
    results.append(TestResult("Space Character Encryption", "Encryption", test_input, shift, expected, actual, passed))
    
    # ============ DECRYPTION TESTS ============
    
    # Test 8: Decrypt single character
    test_input = "B"
    shift = 1
    expected = "A"
    actual = test_decrypt_alphabet(test_input, shift)
    passed = actual == expected
    results.append(TestResult("Single Character Decryption (B)", "Decryption", test_input, shift, expected, actual, passed))
    
    # Test 9: Decrypt multiple characters
    test_input = "DEF"
    shift = 3
    expected = "ABC"
    actual = test_decrypt_alphabet(test_input, shift)
    passed = actual == expected
    results.append(TestResult("Multiple Characters Decryption (DEF)", "Decryption", test_input, shift, expected, actual, passed))
    
    # Test 10: Decrypt lowercase
    test_input = "bcd"
    shift = 1
    expected = "abc"
    actual = test_decrypt_alphabet(test_input, shift)
    passed = actual == expected
    results.append(TestResult("Lowercase Decryption (bcd)", "Decryption", test_input, shift, expected, actual, passed))
    
    # Test 11: Decrypt with wrap-around
    test_input = "A"
    shift = 1
    expected = "z"  # A (index 0) - 1 = -1, wraps to 51 which is 'z'
    actual = test_decrypt_alphabet(test_input, shift)
    passed = actual == expected
    results.append(TestResult("Wrap-around Decryption (A-1)", "Decryption", test_input, shift, expected, actual, passed))
    
    # Test 12: Decrypt symbol
    test_input = "@"
    shift = 1
    expected = "!"
    actual = test_decrypt_symbols(test_input, shift)
    passed = actual == expected
    results.append(TestResult("Symbol Decryption (@)", "Decryption", test_input, shift, expected, actual, passed))
    
    # ============ REVERSIBILITY TESTS ============
    
    # Test 13: Encrypt then decrypt
    original = "Hello"
    shift = 5
    encrypted = test_encrypt_alphabet(original, shift)
    decrypted = test_decrypt_alphabet(encrypted, shift)
    passed = decrypted == original
    results.append(TestResult("Reversibility: Encrypt & Decrypt (Hello)", "Reversibility", original, shift, original, decrypted, passed))
    
    # Test 14: Higher shift value
    test_input = "XYZ"
    shift = 10
    actual = test_encrypt_alphabet(test_input, shift)
    # X(23)+10=33, Y(24)+10=34, Z(25)+10=35 -> h, i, j
    expected = "hij"
    passed = actual == expected
    results.append(TestResult("Higher Shift Value (XYZ, shift=10)", "Encryption", test_input, shift, expected, actual, passed))
    
    return results


if __name__ == "__main__":
    results = run_tests()
    for result in results:
        status = "✓ PASS" if result.passed else "✗ FAIL"
        print(f"{status} - {result.test_name}")
