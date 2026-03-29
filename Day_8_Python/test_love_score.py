from Functions_with_input import calculate_love_score
from verification_report import show_report

print("=" * 50)
print("TEST 1: Vivek and Ramyashree")
print("=" * 50)
calculate_love_score("Vivek", "Ramyashree")

print("\n" + "=" * 50)
print("TEST 2: Alice and Bob")
print("=" * 50)
calculate_love_score("Alice", "Bob")

print("\n" + "=" * 50)
print("TEST 3: Love and True")
print("=" * 50)
calculate_love_score("Love", "True")

print("\n" + "=" * 50)
print("TEST 4: John and Jane")
print("=" * 50)
calculate_love_score("John", "Jane")

print("\n" + "=" * 50)
print("TEST 5: Albert and Olivia")
print("=" * 50)
calculate_love_score("Albert", "Olivia")

# Run the verification report
show_report()
