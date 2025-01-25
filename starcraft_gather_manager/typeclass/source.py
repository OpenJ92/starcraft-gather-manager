class LimitException(Exception):
    """Raised when the limit for a source is exceeded."""
    pass


class Source(Protocol):
    _limit: int  # The maximum allowed gatherables
    _count: int  # The current count of gatherables produced

    @property
    def name(self) -> str:
        """The name of the source (e.g., 'sc2replaystats')."""

    @property
    def metadata(self) -> dict:
        """Optional metadata about the source."""

    def url_formatter(self, specifier: str) -> str:
        """
        Construct the full URL for a given specifier.

        :param specifier: The unique identifier for the resource.
        :return: Full URL as a string.
        """

    @property
    def limit(self) -> int:
        """The maximum allowed gatherables for this source."""
        return self._limit

    def reduce_limit(self, count: int):
        """
        Reduce the available limit for this source.

        :param count: The number of gatherables to produce.
        :raises LimitException: If the requested count exceeds the remaining limit.
        """
        if not hasattr(self, "_count") or not hasattr(self, "_limit"):
            raise NotImplementedError("Source must define '_count' and '_limit' attributes.")

        if self._count + count > self._limit:
            raise LimitException(
                f"Source '{self.name}' exceeded its daily limit. "
                f"Limit: {self._limit}, Current Count: {self._count}, Requested: {count}"
            )
        self._count += count

    def remaining_limit(self) -> int:
        """
        Return the remaining limit for this source.
        """
        if not hasattr(self, "_count") or not hasattr(self, "_limit"):
            raise NotImplementedError("Source must define '_count' and '_limit' attributes.")

        return self._limit - self._count

