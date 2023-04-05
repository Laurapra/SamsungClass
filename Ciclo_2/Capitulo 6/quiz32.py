#PROGRAMACION EN PAREJAS
def max_subarray(arr):
    max_sum = float('-inf')
    current_sum = 0
    start_idx = 0
    end_idx = 0
    
    for i in range(len(arr)):
        current_sum += arr[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            end_idx = i
        
        if current_sum < 0:
            current_sum = 0
            start_idx = i + 1
    
    return (start_idx, end_idx, max_sum)
S = [-2,-1,-3,4,-1,2,1,-5,4]
M = max_subarray(S)
print(M)
