# Base class for all sale items
class SaleItem:
  # Constructor with parameters for item ID, name, and unit price
  def __init__(self, item_id, name, unit_price):
    self.item_id = item_id
    self.name = name
    self.unit_price = unit_price

  # Method to calculate the total cost of a given quantity of the item
  def calculate_total(self):
    # Implementation may differ depending on the type of sale item
    pass

# Derived class for standard items
class StandardItem(SaleItem):
  # Constructor with additional parameter for quantity
  def __init__(self, item_id, name, unit_price, quantity):
    # Inherit members from base class
    super().__init__(item_id, name, unit_price)
    self.quantity = quantity

  # Method to calculate the total cost by multiplying quantity by unit price
  def calculate_total(self):
    return self.quantity * self.unit_price

# Class for discounted items
class DiscountedItem(SaleItem):
  # Constructor with additional parameters for discount percentage and quantity
  def __init__(self, item_id, name, unit_price, discount_percentage, quantity):
    # Inherit members from base class
    super().__init__(item_id, name, unit_price)
    self.discount_percentage = discount_percentage
    self.quantity = quantity

  # Method to calculate the total cost by applying a discount based on discount percentage
  def calculate_total(self):
    # Calculate total cost before discount
    total_cost = self.quantity * self.unit_price
    # Apply discount based on discount percentage
    return total_cost * (1 - self.discount_percentage/100)

# Class for service items
class ServiceItem(SaleItem):
  # Constructor with additional parameter for hourly rate
  def __init__(self, item_id, name, hourly_rate):
    # Inherit members from base class
    super().__init__(item_id, name, None)
    self.hourly_rate = hourly_rate

  # Method to calculate the total cost based on hours of service provided
  def calculate_total(self, hours):
    return self.hourly_rate * hours
#====================================
# Create a standard item
standard_item = StandardItem(1, "Shirt", 20.99, 2)
# Calculate the total cost
print("Total cost of " + standard_item.name + " is $" + str(standard_item.calculate_total()))

# Create a discounted item
discounted_item = DiscountedItem(2, "Socks", 5.99, 15, 3)
# Calculate the total cost
print("Total cost of " + discounted_item.name + " is $" + str(discounted_item.calculate_total()))

# Create a service item
service_item = ServiceItem(3, "Car wash", 20)
# Calculate the total cost for 2 hours of service
print("Total cost of " + service_item.name + " is $" + str(service_item.calculate_total(2)))
