class Restaurant:
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name
        self.reviews = []

    def get_name(self):
        return self.restaurant_name

    def add_review(self, review):
        self.reviews.append(review)

    def get_reviews(self):
        return self.reviews

    def get_customers(self):
        return list(set(review.customer for review in self.reviews))
