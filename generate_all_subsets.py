# 4. Advanced — Generate All Subsets
# Medium–Hard
# Suggested time: 30–45 minutes

# Problem

# Write a recursive function subsets(numbers) that returns every possible subset of a list of distinct integers.

def subsets(numbers):
    result = []
    if not len(numbers):
        result.append([])
        return result

    return result


print(subsets([]))
print(subsets([1]))
# print(subsets([1, 2]))
# print(subsets([1, 2, 3]))
