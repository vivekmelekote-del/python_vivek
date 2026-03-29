"""
Generate test report for encryption and decryption tests
"""
from test_encryption import run_tests


def generate_report():
    """Run tests and generate a detailed report"""
    results = run_tests()
    
    # Count passed and failed tests
    passed_count = sum(1 for result in results if result.passed)
    failed_count = sum(1 for result in results if not result.passed)
    total_count = len(results)
    success_rate = (passed_count / total_count * 100) if total_count > 0 else 0
    
    # Print report header
    print("\n" + "=" * 130)
    print("CAESAR CIPHER ENCRYPTION/DECRYPTION TEST REPORT")
    print("=" * 130 + "\n")
    
    # Print test results table
    print(f"{'#':<4} {'TYPE':<15} {'TEST NAME':<35} {'INPUT':<12} {'SHIFT':<6} {'EXPECTED':<12} {'ACTUAL':<12} {'STATUS':<10}")
    print("-" * 130)
    
    for idx, result in enumerate(results, 1):
        status = "✓ PASS" if result.passed else "✗ FAIL"
        print(f"{idx:<4} {result.test_type:<15} {result.test_name:<35} {result.test_input:<12} {result.shift:<6} {result.expected:<12} {result.actual:<12} {status:<10}")
    
    # Print summary
    print("\n" + "=" * 130)
    print("SUMMARY")
    print("=" * 130)
    print(f"Total Tests:    {total_count}")
    print(f"Passed:         {passed_count} ✓")
    print(f"Failed:         {failed_count} ✗")
    print(f"Success Rate:   {success_rate:.2f}%")
    print("=" * 130 + "\n")
    
    # Print detailed analysis
    print("DETAILED ANALYSIS")
    print("=" * 130)
    
    if failed_count > 0:
        print("\n❌ FAILED TESTS:\n")
        for result in results:
            if not result.passed:
                print(f"  • {result.test_name}")
                print(f"    Type:     {result.test_type}")
                print(f"    Input:    {result.test_input}")
                print(f"    Shift:    {result.shift}")
                print(f"    Expected: {result.expected}")
                print(f"    Actual:   {result.actual}")
                print()
    
    # Group tests by type
    encryption_tests = [r for r in results if r.test_type == "Encryption"]
    decryption_tests = [r for r in results if r.test_type == "Decryption"]
    reversibility_tests = [r for r in results if r.test_type == "Reversibility"]
    
    print("✓ TEST COVERAGE:\n")
    print(f"  Encryption Tests:     {len(encryption_tests)} tests")
    for test in encryption_tests:
        status = "✓" if test.passed else "✗"
        print(f"    {status} {test.test_name}")
    
    print(f"\n  Decryption Tests:     {len(decryption_tests)} tests")
    for test in decryption_tests:
        status = "✓" if test.passed else "✗"
        print(f"    {status} {test.test_name}")
    
    print(f"\n  Reversibility Tests:  {len(reversibility_tests)} tests")
    for test in reversibility_tests:
        status = "✓" if test.passed else "✗"
        print(f"    {status} {test.test_name}")
    
    print("\n" + "=" * 130)
    print("CONCLUSION")
    print("=" * 130)
    
    if failed_count == 0:
        print("✓ All tests passed! The encryption/decryption logic is working correctly.")
    else:
        print(f"✗ {failed_count} test(s) failed. Please review the encryption/decryption logic.")
    
    print("=" * 130 + "\n")
    
    return results


if __name__ == "__main__":
    generate_report()
