from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Context():
    """
    The Context defines the interface of interest to clients.
    """

    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    
    # to update protected class member
    @property
    def strategy(self) -> Strategy:
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """
        self._strategy = strategy

    def apply_sorting(self) -> None:
        
        print("Context: Sorting data using the strategy (not sure how it'll do it)")
        result = self._strategy.apply_sorting(["a", "b", "c", "d", "e"])
        print(",".join(result))


# interface
class Strategy(ABC):
    @abstractmethod
    def apply_sorting(self, data: List):
        pass

# concrete classes
class AscendingSortStrategy(Strategy):
    def apply_sorting(self, data: List) -> List:
        print("In AscendingSortStrategy")
        return sorted(data)

class DescendingSortStrategy(Strategy):
    def apply_sorting(self, data: List) -> List:
        print("In DescendingSortStrategy")
        return reversed(sorted(data))


if __name__ == "__main__":
    context = Context(AscendingSortStrategy())
    print("Client: Strategy is set to AscendingSortStrategy")
    context.apply_sorting()
    print()

    print("Client: Strategy is set to reverse sorting.")
    context.strategy = DescendingSortStrategy()
    context.apply_sorting()