from datetime import datetime
day_of_year = datetime.now().timetuple().tm_yday
print(f"Dzisiaj jest {day_of_year} dzień roku.")
