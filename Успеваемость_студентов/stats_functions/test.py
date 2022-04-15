from functions import is_numeric_array, mean, variance, standard_deviation
from functions import kurtosis, skewness, standard_error, median, quantile
from functions import interval, mode, covariance, correlation

data = [
         [38],
         [1, 2, 3, 4, 5],
         [1.5, 3, 2, 2.5, 4, 4.5, 1.5, 6],
         [76, 84, 69, 92, 58, 89, 73, 97, 85, 77],
         [-34, -91, -46, -26, -82, -17, -75, -41, -8, -59],
         [4, 9, 11, 12, 17, 5, 8, 12, 14],
         [
            26.6, 10.6, -3.1, 1.7, -12.9, 37.0, 22.9, -22.2, 12.6, 36.2,
            0.8, 7.3, 6.1, -48.3, 11.2, -4.8, -38.8, -32.8, -49.4, 45.4, 
            -46.0, -17.2, -37.2, -20.7, -45.2, -22.2, -14.1, -9.4, 34.1, 47.5, 
            37.2, 49.8, 17.9, -42.2, 28.8, 17.9, 28.5, 15.6, 11.6, 12.2, 
            -32.2, -34.0, 45.2, -41.6, 8.3, 36.1, 35.0, 14.1, 0.1, 27.1, 
            17.7, 25.2, 26.4, 13.3, 13.6, -26.5, 41.3, -35.2, 26.7, -1.5, 
            -29.5, -13.6, -41.7, 46.6, -24.3, 44.6, -46.0, -4.3, 36.9, 20.4, 
            -16.3, 28.4, -42.1, 28.7, -5.4, -38.4, -34.2, -15.3, -6.1, -27.5, 
            -29.1, 36.5, -7.5, -0.1, 39.5, 26.3, 7.2, 46.5, -8.0, 47.0, 
            30.4, 40.2, -39.0, -46.7, -35.2, 19.9, 32.4, 28.0, -2.0, 34.0
        ],
        [
            -279.1, 128.4, -8.3, 134.8, 77.5, -30.4, 34.1, 67.2, -80.5, 23.9, 
            78.3, 125.1, -46.4, -152.1, -2.4, 37.1, -46.5, 47.4, -29.2, 41.3, 
            -24.0, -77.7, -18.6, -196.3, -84.6, -137.4, -35.7, 43.0, 49.2, -136.7, 
            -10.7, 26.3, -10.0, 200.8, 10.2, 103.0, -26.6, 87.7, 168.5, -68.9, 
            -267.8, 77.9, 159.0, -146.7, -0.2, -222.9, 52.6, 30.8, 88.5, -153.3, 
            50.1, 62.8, 27.8, -53.7, -105.7, 105.9, -141.8, -64.1, 103.7, 125.6, 
            -163.1, 145.0, 91.8, 67.8, 211.1, -125.8, -16.8, -68.9, -74.8, -193.3, 
            -92.6, 9.0, -176.6, -254.4, -2.4, -24.0, 45.4, -52.9, 163.5, 64.3, 
            -142.2, -28.5, 66.4, 9.3, 24.9, 18.7, -157.0, -84.0, 118.0, 4.0, 
            148.3, -102.9, -54.7, -176.3, -197.1, 42.2, 42.6, -8.8, -46.8, -16.1
        ],
        [
            58.1, 88.0, 1.1, 61.5, 7.1, 23.8, 8.5, 100.6, 5.7, 5.8, 
            20.3, 25.0, 6.6, 78.1, 11.3, 65.5, 4.6, 6.0, 9.4, 46.6, 
            23.7, 12.1, 19.9, 19.2, 8.1, 1.7, 105.5, 59.5, 19.9, 3.5, 
            13.3, 8.3, 24.6, 6.9, 1.7, 4.3, 16.7, 16.8, 60.7, 103.2, 
            8.4, 8.6, 11.0, 3.5, 70.5, 12.6, 83.0, 8.1, 1.5, 2.3, 
            44.9, 73.0, 6.4, 36.6, 65.3, 2.0, 31.1, 5.7, 1.8, 20.9, 
            28.9, 43.9, 45.0, 126.8, 1.1, 10.6, 1.5, 2.5, 3.0, 9.6, 
            1.0, 10.3, 16.3, 18.4, 4.8, 21.4, 5.1, 50.2, 5.5, 1.4, 
            16.9, 6.6, 134.5, 2.9, 4.1, 22.3, 6.6, 6.8, 118.5, 19.5, 
            7.8, 2.8, 9.6, 68.3, 72.1, 15.9, 1.8, 6.5, 106.9, 2.0, 
        ],
        [16, "nlptr", 51, 33, True]
]

def test_is_numeric_array():
    print("Test-case for is_numeric_array function")
    assert is_numeric_array(data[0]) == True, "Should be True"
    print('Test 1 passed')
    
    assert is_numeric_array(data[2]) == True, "Should be True"
    print('Test 2 passed')
    
    assert is_numeric_array(data[9]) == False, "Should be False"
    print('Test 3 passed')
    
    print("=================================")
    
def test_mean():
    print('Test-case for mean function')
    assert mean([1, 2, 3]) == 2, "Should be 2"
    print('Test 1 passed')

    assert round(mean(data[0]), 3) == 38, "Should be 38"
    print('Test 2 passed')

    assert round(mean(data[1]), 3) == 3, "Should be 3"
    print('Test 3 passed')
    
    assert round(mean(data[2]), 3) == 3.125, "Should be 3.125"
    print('Test 4 passed')
    
    assert round(mean(data[3]), 3) == 80, "Should be 80"
    print('Test 5 passed')
    
    assert round(mean(data[4]), 3) == -47.9, "Should be -47.9"
    print('Test 6 passed')
    
    assert round(mean(data[5]), 3) == 10.222, "Should be 10.222"
    print('Test 7 passed')
    
    assert round(mean(data[6]), 3) == 2.933, "Should be 2.933"
    print('Test 8 passed')
    
    assert round(mean(data[7]), 3) == -12.775, "Should be -12.775"
    print('Test 9 passed')
    
    assert round(mean(data[8]), 3) == 27.001, "Should be 27.001"
    print('Test 10 passed')
    print('=================================')

def test_variance():
    print('Test-case for variance function')
    assert round(variance(data[0]), 3) == 0, "Should be 0"
    print('Test 1 passed')

    assert round(variance(data[1]), 3) == 2.5, "Should be 2.5"
    print('Test 2 passed')
    
    assert round(variance(data[2]), 3) == 2.554, "Should be 2.554"
    print('Test 3 passed')
    
    assert round(variance(data[3]), 3) == 137.111, "Should be 137.111"
    print('Test 4 passed')
    
    assert round(variance(data[4]), 3) == 794.322, "Should be 794.322"
    print('Test 5 passed')
    
    assert round(variance(data[5]), 3) == 17.444, "Should be 17.444"
    print('Test 6 passed')
    
    assert round(variance(data[6]), 3) == 879.876, "Should be 879.876"
    print('Test 7 passed')
    
    assert round(variance(data[7]), 3) == 11584.357, "Should be 11584.357"
    print('Test 8 passed')
    
    assert round(variance(data[8]), 3) == 1071.661, "Should be 1071.661"
    print('Test 9 passed')
    print('=================================')
    
def test_standard_deviation():
    print('Test-case for standard_deviation function')
    assert round(standard_deviation(data[0]), 3) == 0, "Should be 0"
    print('Test 1 passed')

    assert round(standard_deviation(data[1]), 3) == 1.581, "Should be 1.581"
    print('Test 2 passed')
    
    assert round(standard_deviation(data[2]), 3) == 1.598, "Should be 1.598"
    print('Test 3 passed')
    
    assert round(standard_deviation(data[3]), 3) == 11.709, "Should be 11.709"
    print('Test 4 passed')
    
    assert round(standard_deviation(data[4]), 3) == 28.184, "Should be 28.184"
    print('Test 5 passed')
    
    assert round(standard_deviation(data[5]), 3) == 4.177, "Should be 4.177"
    print('Test 6 passed')
    
    assert round(standard_deviation(data[6]), 3) == 29.663, "Should be 29.663"
    print('Test 7 passed')
    
    assert round(standard_deviation(data[7]), 3) == 107.631, "Should be 107.631"
    print('Test 8 passed')
    
    assert round(standard_deviation(data[8]), 3) == 32.736, "Should be 32.736"
    print('Test 9 passed')
    print('=================================')

def test_kurtosis():
    print('Test-case for kurtosis function')
    assert round(kurtosis(data[0]), 3) == 0, "Should be 0"
    print('Test 1 passed')

    assert round(kurtosis(data[1]), 3) == -1.2, "Should be -1.2"
    print('Test 2 passed')
    
    assert round(kurtosis(data[2]), 3) == -0.263, "Should be -0.263"
    print('Test 3 passed')
    
    assert round(kurtosis(data[3]), 3) == -0.121, "Should be -0.121"
    print('Test 4 passed')
    
    assert round(kurtosis(data[4]), 3) == -1.201, "Should be -1.201"
    print('Test 5 passed')
    
    assert round(kurtosis(data[5]), 3) == -0.519, "Should be -0.519"
    print('Test 6 passed')
    
    assert round(kurtosis(data[6]), 3) == -1.235, "Should be -1.235"
    print('Test 7 passed')
    
    assert round(kurtosis(data[7]), 3) == -0.288, "Should be -0.288"
    print('Test 8 passed')
    
    assert round(kurtosis(data[8]), 3) == 1.698, "Should be 1.698"
    print('Test 9 passed')
    print('=================================')

def test_skewness():
    print('Test-case for skewness function')
    assert round(skewness(data[0]), 3) == 0, "Should be 0"
    print('Test 1 passed')

    assert round(skewness(data[1]), 3) == 0, "Should be 0"
    print('Test 2 passed')
    
    assert round(skewness(data[2]), 3) == 0.783, "Should be 0.783"
    print('Test 3 passed')
    
    assert round(skewness(data[3]), 3) == -0.42, "Should be -0.42"
    print('Test 4 passed')
    
    assert round(skewness(data[4]), 3) == -0.214, "Should be -0.214"
    print('Test 5 passed')
    
    assert round(skewness(data[5]), 3) == -0.042, "Should be -0.042"
    print('Test 6 passed')
    
    assert round(skewness(data[6]), 3) == -0.207, "Should be -0.207"
    print('Test 7 passed')
    
    assert round(skewness(data[7]), 3) == -0.331, "Should be -0.331"
    print('Test 8 passed')
    
    assert round(skewness(data[8]), 3) == 1.6, "Should be 1.6"
    print('Test 9 passed')
    print('=================================')
    
def test_standard_error():
    print('Test-case for standard_error function')
    assert round(standard_error(data[0]), 3) == 0, "Should be 0"
    print('Test 1 passed')

    assert round(standard_error(data[1]), 3) == 0.707, "Should be 0.707"
    print('Test 2 passed')
    
    assert round(standard_error(data[2]), 3) == 0.565, "Should be 0.656"
    print('Test 3 passed')
    
    assert round(standard_error(data[3]), 3) == 3.703, "Should be 3.703"
    print('Test 4 passed')
    
    assert round(standard_error(data[4]), 3) == 8.912, "Should be 8.912"
    print('Test 5 passed')
    
    assert round(standard_error(data[5]), 3) == 1.392, "Should be 1.392"
    print('Test 6 passed')
    
    assert round(standard_error(data[6]), 3) == 2.966, "Should be 2.966"
    print('Test 7 passed')
    
    assert round(standard_error(data[7]), 3) == 10.763, "Should be 10.763"
    print('Test 8 passed')
    
    assert round(standard_error(data[8]), 3) == 3.274, "Should be 3.274"
    print('Test 9 passed')
    print('=================================')
    
def test_median():
    print('Test-case for median function')
    assert round(median(data[0]), 3) == 38, "Should be 38"
    print('Test 1 passed')

    assert round(median(data[1]), 3) == 3, "Should be 3"
    print('Test 2 passed')
    
    assert round(median(data[2]), 3) == 2.75, "Should be 2.75"
    print('Test 3 passed')
    
    assert round(median(data[3]), 3) == 80.5, "Should be 80.5"
    print('Test 4 passed')
    
    assert round(median(data[4]), 3) == -43.5, "Should be -43.5"
    print('Test 5 passed')
    
    assert round(median(data[5]), 3) == 11, "Should be 11"
    print('Test 6 passed')
    
    assert round(median(data[6]), 3) == 7.25, "Should be 7.25"
    print('Test 7 passed')
    
    assert round(median(data[7]), 3) == -5.35, "Should be -5.35"
    print('Test 8 passed')
    
    assert round(median(data[8]), 3) == 11.15, "Should be 11.15"
    print('Test 9 passed')
    print('=================================')

def test_quantile():
    print('Test-case for quantile function')
    assert quantile(data[0], 0.2) == 38, "Should be 38"
    print('Test 1 passed')

    assert quantile(data[0], 0.4) == 38, "Should be 38"
    print('Test 2 passed')
    
    assert quantile(data[0], 0.6) == 38, "Should be 38"
    print('Test 3 passed')
    
    assert quantile(data[1], 0.2) == 1, "Should be 1"
    print('Test 4 passed')
    
    assert quantile(data[1], 0.4) == 2, "Should be 2"
    print('Test 5 passed')
    
    assert quantile(data[1], 0.6) == 3, "Should be 3"
    print('Test 6 passed')
    
    assert quantile(data[2], 0.2) == 1.5, "Should be 1.5"
    print('Test 7 passed')
    
    assert quantile(data[2], 0.4) == 2, "Should be 2"
    print('Test 8 passed')
    
    assert quantile(data[2], 0.6) == 3, "Should be 3"
    print('Test 9 passed')
    print('=================================')
    
def test_interval():
    print('Test-case for interval function')
    assert round(interval(data[0]), 3) == 0, "Should be 0"
    print('Test 1 passed')

    assert round(interval(data[1]), 3) == 4, "Should be 4"
    print('Test 2 passed')
    
    assert round(interval(data[2]), 3) == 4.5, "Should be 4.5"
    print('Test 3 passed')
    
    assert round(interval(data[3]), 3) == 39, "Should be 39"
    print('Test 4 passed')
    
    assert round(interval(data[4]), 3) == 83, "Should be 83"
    print('Test 5 passed')
    
    assert round(interval(data[5]), 3) == 13, "Should be 13"
    print('Test 6 passed')
    
    assert round(interval(data[6]), 3) == 99.2, "Should be 99.2"
    print('Test 7 passed')
    
    assert round(interval(data[7]), 3) == 490.2, "Should be 490.2"
    print('Test 8 passed')
    
    assert round(interval(data[8]), 3) == 133.5, "Should be 133.5"
    print('Test 9 passed')
    print('=================================')

def test_mode():
    print('Test-case for mode function')
    assert mode([1, 1, 2, 2, 3, 4]) == [1, 2], "Should be [1, 2]"
    print('Test 1 passed')
    
    assert mode(data[0]) == [], "Should be []"
    print('Test 2 passed')

    assert mode(data[1]) == [], "Should be []"
    print('Test 3 passed')
    
    assert mode(data[2]) == [1.5], "Should be [1.5]"
    print('Test 4 passed')
    
    assert mode(data[3]) == [], "Should be []"
    print('Test 5 passed')
    
    assert mode(data[4]) == [], "Should be []"
    print('Test 6 passed')
    
    assert mode(data[5]) == [12], "Should be [12]"
    print('Test 7 passed')
    
    assert mode(data[6]) == [-22.2, -46.0, 17.9, -35.2], "Should be [-22.2, -46.0, 17.9, -35.2]"
    print('Test 8 passed')
    
    assert mode(data[7]) == [-2.4, -24.0, -68.9], "Should be [-2.4, -24.0, -68.9]"
    print('Test 9 passed')
    
    assert mode(data[8]) == [6.6], "Should be [6.6]"
    print('Test 10 passed')
    print('=================================')
    
def test_covariance():
    print('Test-case for covariance function')
    assert round(covariance(data[6], data[7]), 3) == 212.107, "Should be 212.107"
    print('Test 1 passed')

    assert round(covariance(data[6], data[8]), 3) == -38.217, "Should be -38.217"
    print('Test 2 passed')
    
    assert round(covariance(data[7], data[8]), 3) == 280.881, "Should be 280.881"
    print('Test 3 passed')
    print('=================================')

def test_correlation():
    print('Test-case for correlation function')
    assert round(correlation(data[6], data[7]), 3) == 0.066, "Should be 0.066"
    print('Test 1 passed')

    assert round(correlation(data[6], data[8]), 3) == -0.039, "Should be -0.039"
    print('Test 2 passed')
    
    assert round(correlation(data[7], data[8]), 3) == 0.08, "Should be 0.08"
    print('Test 3 passed')
    print('=================================')
    
if __name__ == "__main__":
    test_is_numeric_array()
    test_mean()
    test_variance()
    test_standard_deviation()
    test_kurtosis()
    test_skewness()
    test_standard_error()
    test_median()
    test_quantile()
    test_interval()
    test_mode()
    test_covariance()
    test_correlation()
