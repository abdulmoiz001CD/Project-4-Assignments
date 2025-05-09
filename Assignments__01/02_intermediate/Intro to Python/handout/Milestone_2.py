# planetaryweight.py

def calculate_weight_on_planet(weight_on_earth, planet_name):
    gravity_percent = {
        'Mercury': 37.6,
        'Venus':   88.9,
        'Mars':    37.8,
        'Jupiter': 236.0,
        'Saturn':  108.1,
        'Uranus':  81.5,
        'Neptune': 114.0
    }

    if planet_name not in gravity_percent:
        raise ValueError(f"Unknown planet: '{planet_name}'")

    planet_weight = weight_on_earth * (gravity_percent[planet_name] / 100)
    return round(planet_weight, 2)

if __name__ == "__main__":
    try:
        w = float(input("Enter a weight on Earth: "))
        p = input("Enter a planet: ")
        result = calculate_weight_on_planet(w, p)
        print(f"The equivalent weight on {p}: {result}")
    except Exception as e:
        print(f"Error: {e}")
