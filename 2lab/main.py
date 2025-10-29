def frequency_mapping(str1, str2):
    groups1 = {}
    groups2 = {}
    for char in set(str1):
        count = str1.count(char)
        groups1[count] = groups1.get(count, []) + [char]
    
    for char in set(str2):
        count = str2.count(char)
        groups2[count] = groups2.get(count, []) + [char]
    
    result = []
    for count in sorted(groups1.keys()):
        if count not in groups2 or len(groups1[count]) != len(groups2[count]):
            return "Невозможно установить однозначное соответствие"
        
        
        for a, b in zip(sorted(groups1[count]), sorted(groups2[count])):
            result.append(f"{a}={b}")
    
    return " ".join(result)

print(frequency_mapping("abcbaa", "jkekjj"))  
print(frequency_mapping("aab", "dcc"))   


