from starcraft_gather_manager.typeclass.source import Source

class GameReplays(Source):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(GameReplays, cls).__new__(cls)
            cls._instance._name = "gamereplays"
            cls._instance._metadata = {"site_description": "GameReplays.org"}
            cls._instance._limit = 300  # Example limit
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
        Construct the URL for GameReplays.

        :param specifier: Replay ID.
        :return: The full download URL.
        """
        return f"https://www.gamereplays.org/starcraft2/replays.php?game=33&show=download&&id={specifier}"

