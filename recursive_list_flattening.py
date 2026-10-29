# 3. Intermediate — Recursive List Flattening
# Medium
# Suggested time: 20–30 minutes

# Problem

# Write a recursive function flatten(items) that converts a nested list into a single flat list.

def flatten(items):
    if not items:
        return []
    result = []

    for item in items:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


print(flatten([1, [2, [3, 4]], 5]))
print(flatten([]))
