# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


# Part 1: Greet Template
def greet(name, greeting_template='Hello, <name>!'):
    return greeting_template.replace('<name>', name)


# Part 2: Force
def force(mass, body='earth'):
    bodies = {
        'sun': 274,
        'jupiter': 24.9,
        'neptune': 11.2,
        'saturn': 10.4,
        'earth': 9.8,
        'uranus': 8.9,
        'venus': 8.9,
        'mars': 3.7,
        'mercury': 3.7,
        'moon': 1.6,
        'pluto': 0.6,
    }
    return mass * bodies[body]


# Part 3: Gravity
def pull(m1, m2, d):
    return (6.674 * 10 ** -11) * ((m1 * m2) / d**2)
