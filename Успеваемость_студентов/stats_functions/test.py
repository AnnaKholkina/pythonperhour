from functions import mean, mode

def test_mean():
    print('Test-case for mean function')
    assert mean([1, 2, 3]) == 2, "Should be 2"
    print('Test 1 passed')

    assert mean((1, 2, 3)) == 2, "Should be 2"
    print('Test 2 passed')
    print('=================================')

def test_mode():
    print('Test-case for mode function')

    assert mode([1, 1, 2, 2, 3, 4]) == [1, 2], "Should be [1, 2]"
    print('Test 1 passed')
    print('=================================')

if __name__ == "__main__":
    test_mean()
    test_mode()