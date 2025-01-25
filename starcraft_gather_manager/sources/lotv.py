from starcraft_gather_manager.typeclass.source import Source

class SpawningTool(Source):
    def __init__(self):
        self._name = "spawningtool"
        self._metadata = {"site_description": "SpawningTool website"}

    @property
    def name(self) -> str:
        return self._name

    @property
    def metadata(self) -> dict:
        return self._metadata

    def url_formatter(self, specifier: str) -> str:
        """
        Construct the URL for SpawningTool.

        :param specifier: Replay ID.
        :return: The full download URL.
        """
        return f"https://lotv.spawningtool.com/{specifier}/download/"

