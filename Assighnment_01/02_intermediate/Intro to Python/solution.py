"""
Planetary Weight Calculator

This program asks the user for their weight on Earth
and the name of a planet in the solar system, then
calculates and displays their equivalent weight on
that planet using gravity ratios.
"""

# Gravity constants relative to Earth
planet_gravity = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

def main():
    # Get user input for weight
    earth_weight_input = input("Enter a weight on Earth: ")
    earth_weight = float(earth_weight_input)

    # Get planet name
    planet = input("Enter a planet: ")

    # Lookup gravity constant
    gravity = planet_gravity[planet]

    # Calculate weight on that planet
    planetary_weight = earth_weight * gravity
    rounded_weight = round(planetary_weight, 2)

    # Print result
    print(f"The equivalent weight on {planet}: {rounded_weight}")

if __name__ == "__main__":
    main()
