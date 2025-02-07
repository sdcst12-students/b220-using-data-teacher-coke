import random

# Data

starport_table = {
    2: "A (Excellent quality with refined fuel, over-haul, shipyards)",
    3: "A (Excellent quality with refined fuel, over-haul, shipyards)",
    4: "A (Excellent quality with refined fuel, over-haul, shipyards)",
    5: "B (Good quality with refined fuel, over-haul, shipyards for non-starships)",
    6: "B (Good quality with refined fuel, over-haul, shipyards for non-starships)",
    7: "C (Routine quality with unrefined fuel, some re-pair facilities)",
    8: "C (Routine quality with unrefined fuel, some re-pair facilities)",
    9: "D (Poor quality with unrefined fuel; no re-pair facilities)",
    10: "E (Frontier installation; no facilities)",
    11: "E (Frontier installation; no facilities)",
    12: "X (red travel zone)"
}

Naval = {
    2: "no",
    3: "no",
    4: "no",
    5: "no",
    6: "no",
    7: "no",
    8: "yes",
    9: "yes",
    10: "yes",
    11: "yes",
    12: "yes",
}

Scout = {
    2: "no",
    3: "no",
    4: "no",
    5: "no",
    6: "no",
    7: "yes",
    8: "yes",
    9: "yes",
    10: "yes",
    11: "yes",
    12: "yes",
}

Gas = {
    2: "yes",
    3: "yes",
    4: "yes",
    5: "yes",
    6: "yes",
    7: "yes",
    8: "yes",
    9: "yes",
    10: "no",
    11: "no",
    12: "no",
}

# Size Table (in miles and km)
size_table = {
    0: "Asteroid/Planetoid Belt",
    "R": "Ring(around a world)",
    "S": "Small World (200km)",
    1: "1,000 miles (1,600 km)",
    2: "2,000 miles (3,200 km)",
    3: "3,000 miles (4,800 km)",
    4: "4,000 miles (6,400 km)",
    5: "5,000 miles (8,000 km)",
    6: "6,000 miles (9,600 km)",
    7: "7,000 miles (11,200 km)",
    8: "8,000 miles (12,800 km)",
    9: "9,000 miles (14,400 km)",
    10: "10,000 miles (16,000 km)"
}

# Atmosphere Table
atmosphere_table = {
    0: "None",
    1: "Trace",
    2: "Very Thin, Tainted",
    3: "Very Thin",
    4: "Thin, Tainted",
    5: "Thin",
    6: "Standard",
    7: "Standard, Tainted",
    8: "Dense",
    9: "Dense, Tainted",
    10: "Exotic",
    11: "Corrosive",
    12: "Insidious",
    13: "Dense, High",
    14: "Ellipsoid",
    15: "Thin, Low"
}

# Hydrographics Table
hydrographics_table = {
    0: "No standing water",
    1: "10% Water",
    2: "20% Water",
    3: "30% Water",
    4: "40% Water",
    5: "50% Water",
    6: "60% Water",
    7: "70% Water",
    8: "80% Water",
    9: "90% Water",
    10: "No land masses"
}

# Population Table
population_table = {
    0: "No inhabitants",
    1: "Tens of inhabitants",
    2: "Hundreds of inhabitants",
    3: "Thousands of inhabitants",
    4: "Tens of thousands of inhabitants",
    5: "Hundreds of thousands of inhabitants",
    6: "Millions of inhabitants",
    7: "Tens of millions of inhabitants",
    8: "Hundreds of millions of inhabitants",
    9: "Billions of inhabitants",
    10: "Tens of billions of inhabitants"
}

# Law Level Table
law_level_table = {
    0: "No prohibitions",
    1: "Body pistols, explosives, and poison gas prohibited",
    2: "Portable energy weapons prohibited",
    3: "Machine guns, automatic rifles prohibited",
    4: "Light assault weapons prohibited",
    5: "Personal concealable firearms prohibited",
    6: "All firearms except shotguns prohibited",
    7: "Shotguns prohibited",
    8: "Long bladed weapons controlled, and open possession prohibited",
    9: "Possession of any weapon outside of one's residence is prohibited",
    10: "Weapon possession is prohibited"
}

# Tech Level
tech_level = {
    0: "Stone Age. Primitive",
    1: "Bronze Age to Middle Ages",
    2: "circa 1400 to 1700",
    3: "circa 1700 to 1860",
    4: "circa 1860 to 1900",
    5: "circa 1900 to 1939",
    6: "circa 1940 to 1969",
    7: "circa 1970 to 1979",
    8: "circa 1980 to 1989",
    9: "circa 1990 to 2000",
    10: "Interstellar community",
    11: "Average Imperial",
    12: "Average Imperial",
    13: "Above average Imperial",
    14: "Above average Imperial",
    15: "Technical maximum Imperial",
    16: "Occasional non-Imperial"
}

# Government Type Table
government_table = {
    0: "No government structure",
    1: "Company/Corporation",
    2: "Participating Democracy",
    3: "Self-Perpetuating Oligarchy",
    4: "Representative Democracy",
    5: "Feudal Technocracy",
    6: "Captive Government",
    7: "Balkanization",
    8: "Civil Service Bureaucracy",
    9: "Impersonal Bureaucracy",
    10: "Charismatic Dictator",
    11: "Non-Charismatic Leader",
    12: "Charismatic Oligarchy",
    13: "Religious Dictatorship",
}

Star_System = []
# Initialize variables
Naval_Base = "no"
Scout_Base = "no"
Gas_Giant = "no"

system_presence = random.randint(1, 10)

if system_presence > 2:
    # Star Content
    x = random.randint(1, 6) + random.randint(1, 6)
    starport_type = starport_table[x]
    if x > 6:
        Naval_Base = Naval[x]
    else:
        Naval_Base = Naval[random.randint(1, 6) + random.randint(1, 6)]
    if 6 < x < 9:
        Scout_Base = Scout[random.randint(1, 6) + random.randint(1, 6) - 1]
    elif 4 < x < 7:
        Scout_Base = Scout[random.randint(1, 6) + random.randint(1, 6) - 2]
    elif x < 5:
        Scout_Base = Scout[random.randint(1, 6) + random.randint(1, 6) - 3]
    elif x > 9:
        Scout_Base = Scout[x]
    elif x == 9:
        Scout_Base = Scout[random.randint(1, 6) + random.randint(1, 6)]

    Gas_Giant = Gas[random.randint(1, 6) + random.randint(1, 6)]

    # Generate system name
    prefixes = ["LV", "ZX", "Omicron", "Epsilon", "Gamma", "Beta"]
    system_name = prefixes[random.randint(0, len(prefixes)-1)] + str(random.randint(100, 999))

    # World stats
    s = random.randint(1, 6) + random.randint(1, 6) - 2
    atom = random.randint(1, 6) + random.randint(1, 6) - 7 + s
    hydro = random.randint(1, 6) + random.randint(1, 6) - 7 + s
    Size = size_table[s]

    if s != 0:
        Atmosphere = atmosphere_table[atom]
    else:
        atom = 0
        Atmosphere = atmosphere_table[0]

    if s == -1:
        hydro = 0
    elif atom == -1 or atom == 10:
        hydro -= 4
    elif atom < 0:
        hydro = 0
    elif atom > 10:
        hydro = 10

    hydro = max(0, min(hydro, 10))
    Hydrographics = hydrographics_table[hydro]

    pop = random.randint(1, 6) + random.randint(1, 6) - 2
    gov = random.randint(1, 6) + random.randint(1, 6) - 7 + pop
    Population = population_table[pop]
    Government = government_table[gov]
    Law_Level = law_level_table[random.randint(1, 6) + random.randint(1, 6) - 7 + gov]

    tech = random.randint(1, 6)
    if s == 0 or s == 1:
        tech += 2
    elif s <= 4:
        tech += 1
    if x <= 4:
        tech += 6
    elif x <= 6:
        tech += 4
    elif x <= 8:
        tech += 2
    if atom < 4 or (9 < atom < 15):
        tech += 1
    if hydro == 9:
        tech += 1
    elif hydro == 10:
        tech += 2
    if 0 < pop < 6:
        tech += 1
    elif pop == 9:
        tech += 2
    elif pop == 10:
        tech += 4
    if gov == 0 or gov == 5:
        tech += 1
    elif gov == 13:
        tech -= 2
    tech = max(0, min(tech, 16))
    Tech_Level = tech_level[tech]

    # Append to Star_System
    print(f"Starport Type: {starport_type}")
    print(f"Naval Base: {Naval_Base}")
    print(f"Scout Base: {Scout_Base}")
    print(f"Gas Giant: {Gas_Giant}")
    print(f"System Name: {system_name}")
    print(f"Size: {Size}")
    print(f"Atmosphere: {Atmosphere}")
    print(f"Hydrographics: {Hydrographics}")
    print(f"Population: {Population}")
    print(f"Government: {Government}")
    print(f"Law Level: {Law_Level}")
    print(f"Tech Level: {Tech_Level}")

    Star_System.append(starport_type)
    Star_System.append(Naval_Base)
    Star_System.append(Scout_Base)
    Star_System.append(Gas_Giant)
    Star_System.append(system_name)
    Star_System.append(Size)
    Star_System.append(Atmosphere)
    Star_System.append(Hydrographics)
    Star_System.append(Population)
    Star_System.append(Government)
    Star_System.append(Law_Level)
    Star_System.append(Tech_Level)
else:
    print("No system generated.")


# did my best... still have some errors that I'm not able to solve

