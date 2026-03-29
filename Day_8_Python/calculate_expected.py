#For my reference to test out
def find_letters(name, letter):
    count = 0
    for letter_in_name in name:
        if(letter == letter_in_name):
            count += 1
    return count

def calculate_expected_score(name1, name2):
    """Calculate expected love score manually"""
    letters = ['t', 'r', 'u', 'e', 'l', 'o', 'v', 'e']
    count = [0] * 8
    
    # Count letters in both names
    for name in [name1, name2]:
        for i, letter in enumerate(letters):
            count[i] += find_letters(name, letter)
    
    # Calculate score
    first_half = sum(count[0:4])  # t + r + u + e
    second_half = sum(count[4:8])  # l + o + v + e
    score = first_half * 10 + second_half
    
    return count, first_half, second_half, score

# Test cases
test_cases = [
    ("Vivek", "Ramyashree"),
    ("Alice", "Bob"),
    ("Love", "True"),
    ("John", "Jane"),
    ("Albert", "Olivia")
]

# print("\n" + "="*80)
# print("LOVE SCORE CALCULATOR - EXPECTED OUTPUT VERIFICATION")
# print("="*80 + "\n")

# for idx, (name1, name2) in enumerate(test_cases, 1):
#     count, first_half, second_half, score = calculate_expected_score(name1, name2)
    
#     print(f"TEST {idx}: {name1} & {name2}")
#     print("-" * 80)
#     print(f"Letter counts [t, r, u, e, l, o, v, e]: {count}")
#     print(f"First half (t+r+u+e):  {count[0]}+{count[1]}+{count[2]}+{count[3]} = {first_half}")
#     print(f"Second half(l+o+v+e): {count[4]}+{count[5]}+{count[6]}+{count[7]} = {second_half}")
#     print(f"Score calculation: ({first_half} * 10) + {second_half} = {score}%")
#     print()
expected_result = [('', '', 0)] # Initialize with dummy data, will be overwritten by get_expected_output()
def get_expected_output():
    global expected_result
    expected_result = []
    print("\n" + "="*80)
    print("SUMMARY TABLE")
    print("="*80)
    print(f"{'TEST':<6} {'NAME 1':<12} {'NAME 2':<12} {'EXPECTED %':<12}")
    print("-" * 80)
    for idx, (name1, name2) in enumerate(test_cases, 1):
        _, _, _, score = calculate_expected_score(name1, name2)
        print(f"{idx:<6} {name1:<12} {name2:<12} {score:<12}%")
        expected_result.append((name1, name2, score)) #Here i have grouped the expected result in a list of tuples to print in the verification report
    #print(expected_result)
