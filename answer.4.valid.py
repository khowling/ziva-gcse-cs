

journeys = [
    ["SM720", "4.5"],
    ["GC730", "3"],
    ["JP670", "2"],
    ["GC730", "3.5"],
    ["CC200", "9"],
    ["RY320", "12"]
]

# TODO: Create a function, pilotValid(), that:
# • takes a pilot code as a parameter
# • uses the 2D array journeys to calculate the number of hours that the pilot has flown
# • returns valid if the pilot has flown 9 hours or fewer or warning if the pilot has flown for more than 9 hours
# • uses casting where needed


def pilotValid(pilot_code):
    total_hours: float = 0
    for i in range(0,  len(journeys)):    
        if journeys[i][0] == pilot_code:
            total_hours += float(journeys[i][1])
    
    if total_hours <= 9:
        return "valid"
    else:
        return "warning"