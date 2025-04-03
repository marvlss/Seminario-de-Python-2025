# Mis funciones
def print_ranking(round):
    print (f"{"Jugador":<9} {"Kills":<7} {"Asistencias":<13} {"Muertes":<9} {"MVPs":<6} {"Puntos":<8}")
    print ("-"*56)
    for key in round:
        print (f"{key:<9} {round[key]["kills"]:<7} {round[key]["assists"]:<13} {round[key]["deaths"]:<9} {round[key]["mvps"]:<6} {round[key]["points"]:<6}")
    print ("-"*56)

def increase_values(ROriginal, RFinal):
    max = 0
    mvp = ""
    for player in RFinal:
        RFinal[player]["kills"] += ROriginal[player]["kills"]
        RFinal[player]["assists"] += ROriginal[player]["assists"]
        if ROriginal[player]["deaths"]:
            RFinal[player]["deaths"] += 1
        round_points = increase_points(ROriginal[player])
        RFinal[player]["points"] += round_points
        if round_points > max:
            max = round_points
            mvp = player
    RFinal[mvp]["mvps"] += 1

def increase_points(player):
    total = (player["kills"] * 3) + (player["assists"])
    if player["deaths"]:
        total -= 1
    return total