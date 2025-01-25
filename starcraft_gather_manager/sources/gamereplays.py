from starcraft_gather_manager.typeclass.source import Source

class GameReplaysSource:
    def __init__(self):
        self._name = "gamereplays"
        self._metadata = {"site_description": "GameReplays.org"}

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

