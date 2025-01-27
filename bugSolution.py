def function_with_uncommon_bug_fixed(data=None):
    if data is None:
        results = []
    else:
        results = data
    for item in data:
        results.append(item.upper())
    return results

my_data = ['apple', 'banana', 'cherry']
result1 = function_with_uncommon_bug_fixed(my_data)
print(f"Result 1: {result1}")

my_data2 = ['date', 'fig']
result2 = function_with_uncommon_bug_fixed(my_data2)
print(f"Result 2: {result2}")

# Demonstrating the fix with no initial data
result3 = function_with_uncommon_bug_fixed()
print(f"Result 3: {result3}") # Should raise an error because data is None