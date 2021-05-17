# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
# Part 1: Greet Template
def greet(name, greeting_template='Hello, <name>!'):
    return greeting_template.replace('<name>', name)

# Part 2: Force
def force(mass, body='earth'):
    celestial_bodies = [
        {'name': 'sun', 'gravity': 274},
        {'name': 'jupiter', 'gravity': 24.9},
        {'name': 'neptune', 'gravity': 11.2},
        {'name': 'saturn', 'gravity': 10.4},
        {'name': 'earth', 'gravity': 9.8},
        {'name': 'uranus', 'gravity': 8.9},
        {'name': 'venus', 'gravity': 8.9},
        {'name': 'mars', 'gravity': 3.7},
        {'name': 'mercury', 'gravity': 3.7},
        {'name': 'moon', 'gravity': 1.6},
        {'name': 'pluto', 'gravity': 0.6},
    ]
    for celestial_body in celestial_bodies:
        if body == celestial_body['name']:
            return mass * celestial_body['gravity']

# Part 3: Gravity
def pull(m1, m2, d):
    return (6.674 * 10 ** -11) * ((m1 * m2) / (d**2))
