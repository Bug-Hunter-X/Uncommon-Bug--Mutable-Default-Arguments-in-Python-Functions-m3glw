def function_with_uncommon_bug(data):
    # This function demonstrates an uncommon bug related to mutable default arguments
    results = []
    for item in data:
        results.append(item.upper())
    return results

my_data = ['apple', 'banana', 'cherry']
result1 = function_with_uncommon_bug(my_data)
print(f"Result 1: {result1}")  # Expected output

my_data2 = ['date', 'fig']
result2 = function_with_uncommon_bug(my_data2)
print(f"Result 2: {result2}")  # Unexpected output if you modify my_data before the second call