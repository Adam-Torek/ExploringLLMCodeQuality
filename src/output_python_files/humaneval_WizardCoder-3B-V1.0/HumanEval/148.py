def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''

# Planet names
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# Function to find the closest planet to the sun
def closest_planet(planet1, planet2):
    # Check if planet1 and planet2 are valid planet names
    if planet1 not in planets or planet2 not in planets:
        return ()
    
    # Find the index of planet1 and planet2 in the planets list
    index1 = planets.index(planet1)
    index2 = planets.index(planet2)
    
    # Find the closest planet to the sun
    if index1 < index2:
        return planets[index1+1:index2]
    else:
        return planets[:index2] + planets[index2+1:]

# Test cases
print(closest_planet("Jupiter", "Neptune")) # Output: ("Saturn", "Uranus")
print(closest_planet("Earth", "Mercury")) # Output: ("Venus")
print(closest_planet("Mercury", "Uranus")) # Output: ("Venus", "Earth", "Mars", "Jupiter", "Saturn")<|endoftext|>