fruits = ['grape', 'raspberry', 'apple', 'banana']

print(f"Sort with sorted(): {sorted(fruits)}")
print(f"fruits object itself is not modified: {fruits}")

print(f"Sort in reverse order: {sorted(fruits, reverse=True)}")

print(f"Sort by length: {sorted(fruits, key=len)}")
print("grape is before apple because sorting is stable")

print(f"Sort by length in reverse order: {sorted(fruits, key=len, reverse=True)}")
print("grape is again before apple because sorting is table")

fruits.sort()
print(f"After in place sorting: {fruits}")