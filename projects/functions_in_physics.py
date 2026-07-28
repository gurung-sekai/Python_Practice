# Given values
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Convert Fahrenheit to Celsius 
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5 / 9 
    return c_temp 

# Convert Celsius to Fahrenheit
def c_to_f(c_temp):
    f_temp = c_temp * 9 / 5 + 32
    return f_temp


# Calculate force
def get_force(mass, acceleration):
    return mass * acceleration


# Calculate energy using E = mc²
def get_energy(mass, c=3 * 10**8):
    return mass * c**2


# Calculate work
def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    return force * distance


# Calculate the results
f100_in_celsius = f_to_c(100)
c0_in_fahrenheit = c_to_f(0)
train_force = get_force(train_mass, train_acceleration)
bomb_energy = get_energy(bomb_mass)
train_work = get_work(train_mass, train_acceleration, train_distance)


# Print the results
print(f"100 degrees Fahrenheit is {f100_in_celsius} degrees Celsius.")
print(f"0 degrees Celsius is {c0_in_fahrenheit} degrees Fahrenheit.")
print(f"The GE train supplies {train_force} Newtons of force.")
print(f"A 1kg bomb supplies {bomb_energy} Joules.")
print(
    f"The GE train does {train_work} Joules of work "
    f"over {train_distance} meters."
)