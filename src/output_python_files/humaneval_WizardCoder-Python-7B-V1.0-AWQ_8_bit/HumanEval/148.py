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
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    if planets.index(planet1) > planets.index(planet2):
        return tuple(planets[planets.index(planet1)+1:planets.index(planet2)])
    else:
        return tuple(planets[planets.index(planet2)+1:planets.index(planet1)])

# Test cases
print(bf("Jupiter", "Neptune")) # ("Saturn", "Uranus")
print(bf("Earth", "Mercury")) # ("Venus")
print(bf("Mercury", "Uranus")) # ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
print(bf("Mars", "Saturn")) # ()
print(bf("Saturn", "Mars")) # ()
print(bf("Uranus", "Jupiter")) # ()
print(bf("Neptune", "Mercury")) # ()
print(bf("Venus", "Venus")) # ()
print(bf("Mars", "Mars")) # ()
print(bf("Jupiter", "Jupiter")) # ()
print(bf("Saturn", "Saturn")) # ()
print(bf("Uranus", "Uranus")) # ()
print(bf("Neptune", "Neptune")) # ()
print(bf("Mercury", "Earth")) # ("Venus")
print(bf("Venus", "Earth")) # ("Mars", "Jupiter", "Saturn")
print(bf("Earth", "Venus")) # ("Mars", "Jupiter", "Saturn")
print(bf("Mars", "Jupiter")) # ("Saturn")
print(bf("Saturn", "Jupiter")) # ("Uranus")
print(bf("Uranus", "Saturn")) # ()
print(bf("Neptune", "Jupiter")) # ()
print(bf("Mercury", "Uranus")) # ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
print(bf("Uranus", "Neptune")) # ("Saturn")
print(bf("Saturn", "Neptune")) # ()
print(bf("Venus", "Mars")) # ()
print(bf("Mars", "Venus")) # ()
print(bf("Jupiter", "Venus")) # ()
print(bf("Saturn", "Venus")) # ()
print(bf("Uranus", "Venus")) # ()
print(bf("Neptune", "Venus")) # ()
print(bf("Mercury", "Mars")) # ()
print(bf("Mars", "Mercury")) # ()
print(bf("Saturn", "Mars")) # ()
print(bf("Uranus", "Mars")) # ()
print(bf("Neptune", "