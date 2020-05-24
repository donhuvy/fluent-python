from collections import namedtuple

# Initialize a namedtuple with 1) a class name and 2) a list of field names,
# which can be given as an iterable of strings of as a single space delimited
# string.
City = namedtuple("City", "name country population coordinates")
tokyo = City("Tokyo", "JP", 36.933, (35.689722, 139.691667))
print(tokyo)

# Access the data by name
print(tokyo.population)
print(tokyo.coordinates)

# Access the data by position
print(tokyo[1])

# Class attribution for namedtuple
print(tokyo._fields)

LatLong = namedtuple("LatLong", "lat long")
delhi_data = ("Delhi NCR", "IN", 21.935, LatLong(28.613889, 77.208889))
# Instantiate a namedtuple from an iterable
# Same as delhi = City(*delhi_data)
delhi = City._make(delhi_data)
print(delhi)

# Convert to a collections.OrderDict with _asdict()
for key, value in delhi._asdict().items():
    print(f"{key}: {value}")