"""Lerning Pylint, Get Perfect Score

My main goal is to eventially make this code 10/10 on pylint
"""

class MyIten:
    """
    My Iten Class
    """
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_item(self):
        """
        Get Item
        """
        return self.name, self.price

    def change_price(self, price):
        """
        Change Price
        """
        self.price = price

    def change_name(self, name):
        """
        Change Name
        """
        self.name = name

def main():
    """
    Main Function
    """
    item = MyIten("Apple", 2.5)
    print(item.get_item())
    item.change_price(3.0)
    print(item.get_item())
    item.change_name("Banana")
    print(item.get_item())

if __name__ == "__main__":
    main()
