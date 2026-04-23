def strategy(my_history, opp_history):
    # Cooperate initially or if it's the first round
    if not my_history:
        return 'C'
    
    # If opponent recently defected, defect to punish but then return to cooperation
    if opp_history[-1] == 'D':
        if len(opp_history) > 1 and opp_history[-2] == 'D':
            return 'D'
    
    # Be forgiving: if the opponent cooperates, return cooperation
    return 'C'