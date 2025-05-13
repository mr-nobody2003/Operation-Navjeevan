def clean_cities(cities):
    #Removes duplicates from the list and sorts it alphabetically.
    return sorted(set(cities))

def identify_high_alert(cleaned_cities, previous_intel):
    #Performs set operations to:
    #1. Find all unique cities.
    #2. Find cities unique to both sets.
    #3. Identify cities common between sets (high alert).
    all_cities = cleaned_cities.union(previous_intel)
    unique_cities = cleaned_cities.symmetric_difference(previous_intel)
    high_alert_cities = cleaned_cities.intersection(previous_intel)
    return all_cities, unique_cities, high_alert_cities

def city_intel(high_alert_cities, city_data):
    #Extracts data for high alert cities and computes total population and aid requests.
    high_alert_info = {city: data for city, *data in city_data if city in high_alert_cities}
    total_population = sum(data[0] for data in high_alert_info.values())
    total_aid_requests = sum(data[1] for data in high_alert_info.values())
    return high_alert_info, total_population, total_aid_requests

def track_supplies(supplies):
    #Tracks supply distribution and organizes data into a nested dictionary.
    supply_dict = {}
    for city, supply_type, quantity in supplies:
        if city not in supply_dict:
            supply_dict[city] = {}
        supply_dict[city][supply_type] = quantity
    return supply_dict

# Input for Mission 1
print("\n========================== Mission 1 =============================")
cities = ["Kyiv", "Kharkiv", "Odessa", "Kyiv", "Lviv", "Kharkiv", "Dnipro"]
print("Input cities : ",cities)
cleaned_cities = clean_cities(cities)
print("Cleaned cities:", cleaned_cities)
    
# Input for Mission 2
print("\n========================== Mission 2 =============================")
cleaned_cities_set = set(cleaned_cities)
print("cleaned_cities : ",cleaned_cities)
previous_intel_set = {"Kyiv", "Mariupol", "Lviv", "Donetsk"}
print("Previous intel : ",previous_intel_set)
all_cities, unique_cities, high_alert_cities = identify_high_alert(cleaned_cities_set, previous_intel_set)
print("All cities:", all_cities)
print("Unique cities:", unique_cities)
print("High alert cities:", high_alert_cities)

# Input for Mission 3
print("\n========================== Mission 3 =============================")
city_data = [
    ("Kyiv", 2800000, 250),
    ("Kharkiv", 1431000, 180),
    ("Lviv", 721301, 90),
    ("Odessa", 1029049, 120)
]
print("High alert cities : ",high_alert_cities ,"City data : ",city_data)
high_alert_info, total_population, total_aid_requests = city_intel(high_alert_cities, city_data)
print("High alert cities info:", high_alert_info)
print("Total population:", total_population)
print("Total aid requests:", total_aid_requests)

# Input for Mission 4
print("\n========================== Mission 4 =============================")
supplies = [
    ("Kyiv", "Food", 500),
    ("Moscow", "Medicines", 200),
    ("Lviv", "Water", 300),
    ("Saint Petersburg", "Blankets", 100),
    ("Kharkiv", "Food", 150)
]
print("Supplies : ",supplies)
supply_distribution = track_supplies(supplies)
print("Supply distribution:", supply_distribution)
