class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Game(metaclass=SingletonMeta):
    def __init__(self, player1, player2) -> None:
        self.player1 = player1
        self.player2 = player2


if __name__ == "__main__":
    # The client code.

    s1 = Game("A", "B")
    s2 = Game("C", "D")  # useless as it uses the original game instance with Player A and B hence ensures Single Instance of Game class
    
    print(s1.player1)
    print(s2.player1)

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")

"""

Certainly! Let's break down the line instance = super().__call__(*args, **kwargs) in the context of the SingletonMeta metaclass.

In Python, super() is used to access methods and attributes of a superclass from a subclass. In this case, super().__call__(*args, **kwargs) refers to the __call__ method of the superclass of SingletonMeta, which is type.

Here's what's happening in that line:

super() returns a proxy object that delegates method calls to the parent class of the current object (i.e., type in this case).

__call__ is the method called when you treat a class like a function (i.e., when you create an instance of the class by calling it like a function).

*args and **kwargs are used to capture any positional and keyword arguments passed to the constructor of the class.

So, super().__call__(*args, **kwargs) is effectively calling the __call__ method of the parent class (type) with the arguments *args and **kwargs. This is how instances of the Game class are created.

When this line is executed within the __call__ method of SingletonMeta, it ensures that the instance of the class is created by calling the superclass's __call__ method, thus creating a new instance of the class with the provided arguments (*args and **kwargs).

Overall, this line is responsible for creating a new instance of the class whenever it's called, while still ensuring that only one instance of the class exists, as per the Singleton pattern, by delegating the creation of instances to the superclass's __call__ method.

"""