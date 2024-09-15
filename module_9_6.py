from itertools import combinations

# Variant 1
def  all_variants(text):
    for i in range(len(text)):
        if i == 0:
            for j in range(1, len(text)+1):
                yield text[j-1:j]
        if i == 1:
            for j in range(len(text)-1):
                yield text[j:j+i+1]
        if i == 2:
            yield text[0:i + 1]

# Variant 2
# def  all_variants(text):
#     for i in range(1,len(text)+1):
#         yield list(combinations(text, i))


a = all_variants("abc")
for i in a:
    print(*i)