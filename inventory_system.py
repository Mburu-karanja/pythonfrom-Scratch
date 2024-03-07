# Base class for all products in the inventory
class Product:
  # Constructor with parameters for product ID, name, and quantity in stock
  def __init__(self, product_id, name, quantity_in_stock):
    self.product_id = product_id
    self.name = name
    self.quantity_in_stock = quantity_in_stock

  # Method to calculate the total value of the product in stock
  def calculate_value(self)

# Derived class for simple products
class SimpleProduct(Product):
  # Constructor with additional parameter for unit price
  def __init__(self, product_id, name, quantity_in_stock, unit_price):
    # Inherit members from base class
    super().__init__(product_id, name, quantity_in_stock)
    self.unit_price = unit_price

  # Method to calculate the total value by multiplying quantity in stock by unit price
  def calculate_value(self):
    return self.quantity_in_stock * self.unit_price

# Class for perishable products
class PerishableProduct(Product):
  # Constructor with additional parameters for unit price and expiry date
  def __init__(self, product_id, name, quantity_in_stock, unit_price, expiry_date):
    # Inherit members from base class
    super().__init__(product_id, name, quantity_in_stock)
    self.unit_price = unit_price
    self.expiry_date = expiry_date

  # Method to calculate the total value by considering the remaining shelf life and applying a discount
  def calculate_value(self):
    # Calculate remaining shelf life in days
    remaining_shelf_life = self.expiry_date - date.today()
    # Apply discount based on remaining shelf life
    if remaining_shelf_life.days <= 7:
      # Discount of 10% for products with less than or equal to 7 days remaining
      return self.quantity_in_stock * self.unit_price * 0.9
    else:
      # No discount for products with more than 7 days remaining
      return self.quantity_in_stock * self.unit_price

# Class for digital products
class DigitalProduct(Product):
  # Constructor with additional parameter for price
  def __init__(self, product_id, name, quantity_in_stock, price):
    # Inherit members from base class
    super().__init__(product_id, name, quantity_in_stock)
    self.price = price

  # Method to calculate the total value based on the current price
  def calculate_value(self):
    return self.quantity_in_stock * self.price

# Create a simple product
simple_product = SimpleProduct(1, "Book", 10, 10.99)
# Calculate the total value
print("Total value of " + simple_product.name + " is $" + str(simple_product.calculate_value()))

# Create a perishable product
perishable_product = PerishableProduct(2, "Milk", 20, 2.99, date(2022, 12, 31))
# Calculate the total value
print("Total value of " + perishable_product.name + " is $" + str(perishable_product.calculate_value()))

# Create a digital product
digital_product = DigitalProduct(3, "Ebook", 50, 7.99)
# Calculate the total value
print("Total value of " + digital_product.name + " is $" + str(digital_product.calculate_value()))
