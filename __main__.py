import storage_bridge
import gather_manager

# Example Plan: Each factory instantiates its own Source and Strategy
plan = [
    Factory(source=SC2ReplayStats(), strategy=ScrapeUpward(step=250)),
    Factory(source=SC2ReplayStats(), strategy=ScrapeDownward(step=250)),
    Factory(source=SpawningTool(), strategy=ScrapeUpward(step=250)),
    Factory(source=SpawningTool(), strategy=ScrapeDownward(step=250)),
    Factory(source=GameReplays(), strategy=ScrapeUpward(step=250)),
    Factory(source=GameReplays(), strategy=ScrapeDownward(step=250)),
]

