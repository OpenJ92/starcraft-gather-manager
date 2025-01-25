from starcraft_gather_manager.typeclass.source import Source

class SC2ReplayStats(Source):
    def __init__(self):
        self._name = "sc2replaystats"
        self._metadata = {"site_description": "SC2 replay stats website"}

    @property
    def name(self) -> str:
        return self._name

    @property
    def metadata(self) -> dict:
        return self._metadata

    def url_formatter(self, specifier: str) -> str:
        """
        Construct the URL for SC2ReplayStats.

        :param specifier: Replay ID.
        :return: The full download URL.
        """
        return f"https://sc2replaystats.com/download/{specifier}"
