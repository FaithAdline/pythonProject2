from customer import Customer
from restaurant import Restaurant
from review import Review




customer1 = Customer("FAVY", "NJERI")
restaurant1 = Restaurant("FIVE STAR")
review1 = Review(customer1, restaurant1, 5)

print(customer1.full_name())  # Should print "FAVY NJERI"
print(restaurant1.get_name())  # Should print "FIVE STAR"
# print(review1.rating())  # Should print 5
print(Customer.all())  # Should print a list with customer1
print(Review.all())  # Should print a list with review1
