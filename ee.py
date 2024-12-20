import random

def simulate_basketball_game(players):
    results = {}
    
    for player_name, shooting_skill in players.items():
        makes = 0
        misses = 0
        total_shots = 20  # Number of shots each player will take
        
        for _ in range(total_shots):
            shot_outcome = random.randint(1, 100)
            if shot_outcome <= shooting_skill * 10:
                makes += 1
            else:
                misses += 1
        
        results[player_name] = {
            'makes': makes,
            'misses': misses
        }
    
    return results

# Define players and their shooting skills
players = {
    'Player 1': 4,  # 40% shooting skill
    'Player 2': 7,  # 70% shooting skill
    'Player 3': 9   # 90% shooting skill
}

# Run the simulation
game_results = simulate_basketball_game(players)

# Output the results
for player, result in game_results.items():
    print(f"{player}: {result['makes']} makes, {result['misses']} misses")