def alpha_beta_pruning(node, depth, alpha, beta, maximizingPlayer, values, index=0):
    if depth == 0:
        return values[index]

    if maximizingPlayer:
        maxEval = float('-inf')
        for i in range(2):
            eval = alpha_beta_pruning(node*2+i+1, depth-1, alpha, beta, False, values, index*2+i)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = float('inf')
        for i in range(2):
            eval = alpha_beta_pruning(node*2+i+1, depth-1, alpha, beta, True, values, index*2+i)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval

# Example tree (leaf node values)
values = [3, 5, 6, 9, 1, 2, 0, -1]
depth = 3

# Initial alpha = -infinity, beta = +infinity
optimal_value = alpha_beta_pruning(0, depth, float('-inf'), float('inf'), True, values)
print("Optimal value (with Alpha-Beta Pruning):", optimal_value)
