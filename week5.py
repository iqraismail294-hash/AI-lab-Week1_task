#==========Task 1===========


import math
def minimax(depth, index, turn, scores, target):
    if depth == target:
        return scores[index]
    if turn:
        return max(
            minimax(depth+1,index*2,False,scores,target),
            minimax(depth+1,index*2+1,False, scores, target))
    else:
        return min(
            minimax(depth+1,index*2,True,scores,target),
            minimax(depth+1,index*2+1,True,scores,target))
scores = [3, 5, 2, 9, 0, 7]
treedepth = math.ceil(math.log2(len(scores)))
scores += [0] * (2**treedepth - len(scores))
print("The optimal value is:",minimax(0, 0, True, scores, treedepth))



#=========Task 2============



import math
count = 0
def minimax(depth, index, maxTurn, scores, target):
    global count
    if depth == target:
        count += 1
        return scores[index]
    if maxTurn:
        return max(
            minimax(depth + 1, index * 2,
                    False, scores, target),
            minimax(depth + 1, index * 2 + 1,
                    False, scores, target))
    else:
        return min(
            minimax(depth + 1, index * 2,
                    True, scores, target),
            minimax(depth + 1, index * 2 + 1,
                    True, scores, target))
scores = [3, 5, 2, 9, 3, 5, 2, 9]
depth = int(math.log2(len(scores)))
result = minimax(0, 0, True, scores, depth)
print("Optimal Value:", result)
print("Evaluated Leaves:", count)
    
                              
                              
#======Task 3=========


import math
def alpha_beta(depth, index, turn, scores, target, alpha, beta, counter):
    if depth == target:
        counter[0] += 1
        return scores[index]
    if turn:
        value = float('-inf')
        for i in (1,0):
            value = max(value,alpha_beta(depth + 1, index * 2 + i,False, scores, target, alpha, beta, counter))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for i in [1,0]:
            value = min(value,alpha_beta(depth + 1, index * 2 + i,True, scores, target, alpha, beta, counter))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value
scores = [3,5,2,9,3,5,2,9]
depth = int(math.log2(len(scores)))
counter = [0]
result = alpha_beta(0, 0, True, scores, depth,float('-inf'), float('inf'), counter)
print("Alpha Beta =", result)
print("Leaves =", counter[0])

    
        
