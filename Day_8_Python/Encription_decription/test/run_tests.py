"""
Main test runner for Caesar Cipher encryption/decryption
Run both tests and generate comprehensive report with a single command
"""
from report_generator import generate_report


def main():
    """Main entry point - runs tests and generates report"""
    print("\n" + "#" * 130)
    print("# STARTING CAESAR CIPHER ENCRYPTION/DECRYPTION TEST SUITE")
    print("#" * 130 + "\n")
    
    # Generate and display report (which runs tests internally)
    generate_report()
    
    print("#" * 130)
    print("# TEST SUITE COMPLETED")
    print("#" * 130 + "\n")


if __name__ == "__main__":
    main()
