from typing import Protocol

class Source(Protocol):
    @property
    def name(self) -> str:
        """The name of the source (e.g., 'sc2replaystats')."""

    @property
    def base_url(self) -> str:
        """The base URL for constructing download links."""

    @property
    def metadata(self) -> dict:
        """Optional metadata about the source."""

    def construct_url(self, specifier: str) -> str:
        """
        Construct the full URL for a given specifier.

        :param specifier: The unique identifier for the resource.
        :return: Full URL as a string.
        """
