def ground_shipping_cost(weight):
  if weight <= 2:
    return 20 + 1.5 * weight
  if (weight > 2) and (weight <= 6):
    return 20 + 3 * weight
  if (weight > 6) and (weight <= 10):
    return 20 + 4 * weight
  if (weight > 10):
    return 20 + 4.75 * weight

premium_ground_shipping = 125

def drone_shipping_cost(weight):
  if weight <= 2:
    return 4.5 * weight
  if (weight > 2) and (weight <= 6):
    return 9 * weight
  if (weight > 6) and (weight <= 10):
    return 12 * weight
  if (weight > 10):
    return 14.25 * weight

def cheapest_shipping(weight):
  if ground_shipping_cost(weight) > drone_shipping_cost(weight) and drone_shipping_cost(weight) < premium_ground_shipping:
    print("Drone shipping is cheapest and costs " + str(drone_shipping_cost(weight)) + "$.")
  if ground_shipping_cost(weight) < drone_shipping_cost(weight) and ground_shipping_cost(weight) < premium_ground_shipping:
    print("Ground shipping is cheapest and costs " + str(ground_shipping_cost(weight)) + "$.")
  if premium_ground_shipping < ground_shipping_cost(weight) or premium_ground_shipping < drone_shipping_cost(weight):
    print("Premium ground shipping is cheapest and costs " + str(premium_ground_shipping) + "$.")

print(cheapest_shipping(41.5))
