from starcraft_gather_manager.typeclass.source import Source

class SC2ReplayStats(Source):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SC2ReplayStats, cls).__new__(cls)
            cls._instance._name = "sc2replaystats"
            cls._instance._metadata = {"site_description": "SC2 replay stats website"}
            cls._instance._limit = 500  # Daily limit
            cls._instance._count = 0    # Tracks how many gatherables have been produced today
        return cls._instance

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
