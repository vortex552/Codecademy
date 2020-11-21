train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

# function calculates temp in fahrenheit
def f_to_c(f_temp): 
  (f_temp - 32) * 5/9
  return (f_temp - 32) * 5/9
# variable f100_in_celsius is defined
f100_in_celsius = f_to_c(100)
# prints output in celcius
print(f100_in_celsius)

# function calculates temp in celcius
def c_to_f(c_temp): 
  32 + 9/5 * c_temp
  return   32 + 9/5 * c_temp
# prints output in fahrenheit
print(c_to_f(0))

# function for force
def get_force(mass, acceleration):
  mass * acceleration
  return mass * acceleration
# variable mass, acceleration and train_force are defined
mass = train_mass
acceleration = train_acceleration
train_force = get_force(mass, acceleration)
# prints output trainforce 
print(train_force)
# prints puts out string with the variable trainforce
print("The GE train supplies " + str(train_force) + " Newtons of force.")

# function for energy
def get_energy(mass, c = 3*10**8):
  mass * c**2
  return mass * c**2
# defines mass and bom_energy
mass = bomb_mass
bomb_energy = get_energy(mass, c = 3*10**8)
# prints the energy in Joules
print(bomb_energy)
# prints the bomb_energy in string
print("A 1kg bomb supplies " + str(bomb_energy ) +" Joules.")

# function for work (in physics term)
def get_work(mass, acceleration, train_distance):
  mass * acceleration * distance
  return mass * acceleration * distance
# Defines variable distance, mass, acceleration and train_work
acceleration = train_acceleration
mass = train_mass
distance = train_distance
train_work = mass * acceleration * distance
# prints train_work
print(train_work)
# prints train_work and distance in a string
print("The GE train does " + str(train_work) + " Joules of work over " + str(distance) + " meters.")
