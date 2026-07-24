def longest_consecutive_sequence(nums):
    
    seen = set() # 1 2
    longest_sequence = 0 # 2
    sequence = 0 # 1 2
    temporal_num = 0 # 1 0 1 2
    
    for num in nums:
        
        temporal_num = num
        
        while temporal_num+1 in seen or temporal_num-1 in seen:
            sequence += 1
            
            if temporal_num+1 in seen: 
                temporal_num += 1 
            else:  
                temporal_num -= 1
            
        seen.add(num)
        longest_sequence = max(longest_sequence, sequence + 1)
        sequence = 0
            
    return longest_sequence
    
    
print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))         # 4
print(longest_consecutive_sequence([1, 2, 0, 1]))                   # 3
print(longest_consecutive_sequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])) # 9
print(longest_consecutive_sequence([[]]))                           # 0