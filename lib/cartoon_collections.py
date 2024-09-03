def roll_call_dwarves(dwarves):
    for i, dwarf in enumerate(dwarves):
        print(f"{i+1}. {dwarf}")

def summon_captain_planet(planeteer_calls):
    return [call.capitalize() + "!" for call in planeteer_calls]

def long_planeteer_calls(planeteer_calls):
    return any(len(call) > 4 for call in planeteer_calls)

def find_the_cheese(snacks):
    cheeses = ["cheddar", "gouda", "camembert"]
    for snack in snacks:
        if snack in cheeses:
            return snack
    return None
    
