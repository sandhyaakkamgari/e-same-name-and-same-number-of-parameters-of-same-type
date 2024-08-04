class MyClass:
    def my_method(self, x, y):
        print("First method:", x + y)

    def my_method(self, x, y):  # This method overrides the previous one
        print("Second method:", x * y)

obj = MyClass()
obj.my_method(2, 3)