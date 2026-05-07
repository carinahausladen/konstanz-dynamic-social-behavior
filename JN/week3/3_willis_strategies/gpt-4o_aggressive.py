def strategy(my_history, opp_history):
    if not my_history:  # First move, default to cooperate.
        return 'C'
    
    if opp_history[-1] == 'D':  # Retaliate if last opponent move was defect.
        return 'D'
    
    if len(my_history) > 1 and opp_history.count('C') < opp_history.count('D'):
        # If opponent has defected more than cooperated, become aggressive.
        return 'D'
    
    # Define parameters for tit-for-tat with forgiveness
    forgiveness_chance = 0.1  # 10% chance to forgive and start cooperating again
    num_rounds = len(my_history)
    
    lookback = min(5, num_rounds)  # Look back up to 5 moves
    
    # If opponent has cooperated more than they've defected recently, cooperate.
    if opp_history[-lookback:].count('C') > opp_history[-lookback:].count('D'):
        return 'C'
    
    # With a slight chance, try to cooperate if the opponent recently cooperated.
    if my_history[-1] == 'C' and num_rounds >= 2 and opp_history[-2] == 'C':
        return 'C'
    
    # Default to defect in uncertain or aggressive scenarios.
    return 'D'