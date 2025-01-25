from typing import Protocol, List

class Strategy(Protocol):
    def produce_ids(self) -> List[str]:
        """
        Generate a list of IDs based on the strategy.

        :return: A list of unique identifiers.
        """

