def time_to_text(minutes):
    heures = minutes // 60
    minutes_restantes = minutes % 60
    print(heures, "heures et", minutes_restantes, "minutes")

time_to_text(160)
time_to_text(90)
time_to_text(45)
time_to_text(125)