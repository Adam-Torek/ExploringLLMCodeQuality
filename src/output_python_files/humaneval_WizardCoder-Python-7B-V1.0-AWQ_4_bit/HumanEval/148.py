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
    index1 = planets.index(planet1)
    index2 = planets.index(planet2)
    if index1 > index2:
        return tuple(planets[index2+1:index1])
    else:
        return tuple(planets[index1+1:index2])

# Test cases
print(bf("Jupiter", "Neptune")) # ("Saturn", "Uranus")
print(bf("Earth", "Mercury")) # ("Venus")
print(bf("Mercury", "Uranus")) # ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
print(bf("Mars", "Saturn")) # ()
print(bf("Saturn", "Mars")) # ()
print(bf("Uranus", "Jupiter")) # ()
print(bf("Venus", "Earth")) # ()
print(bf("Earth", "Venus")) # ()
print(bf("Jupiter", "Earth")) # ()
print(bf("Saturn", "Venus")) # ()
print(bf("Uranus", "Venus")) # ()
print(bf("Neptune", "Mercury")) # ()
print(bf("Mars", "Mars")) # ()
print(bf("Mercury", "Mercury")) # ()
print(bf("Uranus", "Uranus")) # ()
print(bf("Neptune", "Neptune")) # ()
print(bf("Saturn", "Saturn")) # ()
print(bf("Venus", "Venus")) # ()
print(bf("Mars", "Mars")) # ()
print(bf("Jupiter", "Jupiter")) # ()
print(bf("Saturn", "Saturn")) # ()
print(bf("Uranus", "Uranus")) # ()
print(bf("Neptune", "Neptune")) # ()
print(bf("Mercury", "Mercury")) # ()
print(bf("Venus", "Venus")) # ()
print(bf("Mars", "Mars")) # ()
print(bf("Jupiter", "Jupiter")) # ()
print(bf("Saturn", "Saturn")) # ()
print(bf("Uranus", "Uranus")) # ()
print(bf("Neptune", "Neptune")) # ()
print(bf("Mercury", "Mercury")) # ()
print(bf("Venus", "Venus")) # ()
print(bf("Mars", "Mars")) # ()
print(bf("Jupiter", "Jupiter")) # ()
print(bf("Saturn", "Saturn")) # ()
print(bf("Uranus", "Uranus")) # ()
print(bf("Neptune", "Neptune")) # ()
print(bf("Mercury", "Mercury")) # ()
print(bf