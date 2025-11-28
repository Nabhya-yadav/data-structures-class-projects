from collections import Counter

# Using the same data_dict as above

data_dict = {

'item1': 'apple',

'item2': 'banana',

'item3': 'apple',

'item4': 'orange',

'item5': 'banana',

'item6': 'apple'

}

# Counter creates a dictionary where keys are values and values are their counts

value_counts = Counter(data_dict.values())

print(f"All value frequencies: {value_counts}")

print(f"Frequency of 'apple' using Counter: {value_counts['apple']}")