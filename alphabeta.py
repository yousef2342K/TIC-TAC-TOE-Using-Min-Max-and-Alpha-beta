def max_value(board, alpha=float('-inf'), beta=float('inf')):
    if terminal(board):
        return [utility(board), None]
    v = float('-inf')
    best_move = None
    for action in actions(board):
        hypothetical_value = min_value(result(board, action), alpha, beta)[0]
        if hypothetical_value > v:
            v = hypothetical_value
            best_move = action
        alpha = max(alpha, v)
        if alpha >= beta:
            break  # Beta cutoff
    return [v, best_move]

def min_value(board, alpha=float('-inf'), beta=float('inf')):
    if terminal(board):
        return [utility(board), None]
    v = float('inf')
    best_move = None
    for action in actions(board):
        hypothetical_value = max_value(result(board, action), alpha, beta)[0]
        if hypothetical_value < v:
            v = hypothetical_value
            best_move = action
        beta = min(beta, v)
        if alpha >= beta:
            break  # Alpha cutoff
    return [v, best_move]
