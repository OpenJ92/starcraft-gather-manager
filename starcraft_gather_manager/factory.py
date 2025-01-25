class Factory:
    def __init__(self, source: Source, strategy: Strategy):
        """
        Initialize the Factory.

        :param source: A class implementing the Source protocol.
        :param strategy: A class implementing the Strategy protocol.
        """
        self.source = source
        self.strategy = strategy

    def generate_gatherables(self) -> List[DownloadLink]:
        """
        Generate DownloadLink gatherables by applying the strategy to the source.

        :return: List of DownloadLink gatherables.
        """
        ids = self.strategy.produce_ids()  # Generate IDs from the strategy
        gatherables = []

        for id in ids:
            gatherable = DownloadLink(
                url_formatter=self.source.construct_url,  # URL formatter from the source
                specifier=id,  # Unique ID for the resource
                metadata={"source_name": self.source.name, **self.source.metadata}  # Source metadata
            )
            gatherables.append(gatherable)

        return gatherables

