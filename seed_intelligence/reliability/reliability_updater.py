from ..feedback.strategy_reward import measured_rewards

def update(trials):
    valid, wins, mean_gain = measured_rewards(trials)
    return valid, wins, (1 + wins) / (2 + valid), mean_gain
