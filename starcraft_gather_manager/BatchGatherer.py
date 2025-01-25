from asyncio import gather, Semaphore
from gather_manager import GatherManager
from log_manager.db_logger import db_logger
from log.impl_process_replay import LogDownload

class BatchGatherer:
    def __init__(self, storage, factories, logger, max_concurrent_tasks=4):
        """
        Initialize the BatchGatherer.

        :param storage: Storage instance for saving gathered data.
        :param factories: List of Factory instances that generate gatherables.
        :param logger: Logging instance for tracking gather operations.
        :param max_concurrent_tasks: Maximum number of concurrent gathering tasks.
        """
        self.storage = storage
        self.factories = factories
        self.logger = logger
        self.semaphore = Semaphore(max_concurrent_tasks)

    async def gather(self):
        """
        Orchestrates the gathering process across all factories.
        """
        try:
            tasks = []

            for factory in self.factories:
                gatherables = factory.generate_gatherables()
                for gatherable in gatherables:
                    coroutine = self._process_gatherable(gatherable)
                    tasks.append(coroutine)

            results = await gather(*tasks, return_exceptions=True)

            # Log results if needed
            print(f"Gathering completed. {len(results)} items processed.")

        except Exception as e:
            print(f"Batch gather process failed: {e}")
            raise

    async def _process_gatherable(self, gatherable):
        """
        Process a single Gatherable instance using a GatherManager.

        :param gatherable: The Gatherable to process.
        """
        async with self.semaphore:
            manager = GatherManager(storage=self.storage)

            try:
                jitter = random.uniform(0, 0.3)  # Add jitter to distribute tasks
                await sleep(jitter)

                await manager.gather(gatherable=gatherable, storage=self.storage)

                # Optionally log success
                self.logger.log_post_action_success("gather", gatherable=gatherable)

            except Exception as e:
                # Optionally log failure
                self.logger.log_post_action_failure("gather", gatherable=gatherable, exception=e)
                raise

