COS 101 ASSIGNMENT
Five Basic Physics Formulas
Name: Acha Princewill Isioma
Martric number: BHU/26/04/05/010

Formula 1: Speed
Speed = Distance / Time

def calculate_speed(distance, time):
    if time == 0:
        return "Time cannot be zero"

    return distance / time


Formula 2: Force
Force = Mass x Acceleration

def calculate_force(mass, acceleration):
    return mass * acceleration


Formula 3: Weight
Weight = Mass x Gravitational Acceleration

def calculate_weight(mass):
    gravity = 9.81
    return mass * gravity


Formula 4: Density
Density = Mass / Volume

def calculate_density(mass, volume):
    if volume == 0:
        return "Volume cannot be zero"

    return mass / volume


Formula 5: Kinetic Energy
Kinetic Energy = 1/2 x Mass x Velocity²

def calculate_kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2


Displaying the results

print("COS 101 - FIVE PHYSICS FORMULAS")
print("--------------------------------")

print("1. Speed:", calculate_speed(100, 5), "m/s")

print("2. Force:", calculate_force(10, 5), "N")

print("3. Weight:", calculate_weight(10), "N")

print("4. Density:", calculate_density(20, 5), "kg/m³")

print("5. Kinetic Energy:",
      calculate_kinetic_energy(10, 4), "J")