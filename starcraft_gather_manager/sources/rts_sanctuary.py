from starcraft_gather_manager.typeclass.source import Source

class RTSSanctuary(Source):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(RTSSanctuary, cls).__new__(cls)
            cls._instance._name = "rts-sanctuary"
            cls._instance._metadata = {"site_description": "RTS-Sanctuary (inaccessible)"}
            cls._instance._limit = 0  # No available resources
            cls._instance._count = 0
        return cls._instance

    @property
    def name(self) -> str:
        return self._name

    @property
    def metadata(self) -> dict:
        return self._metadata

    def url_formatter(self, specifier: str) -> str:
        raise NotImplementedError("RTS-Sanctuary is currently inaccessible.")
