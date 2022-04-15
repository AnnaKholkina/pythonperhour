from functions import mean

def test_mean():
    assert mean([1, 2, 3]) == 2, "Should be 2"
    print('Test 1 passed')

def test_mean_tuple():
    assert mean((1, 2, 3)) == 2, "Should be 2"
    print('Test 2 passed')

if __name__ == "__main__":
    test_mean()
    test_mean_tuple()