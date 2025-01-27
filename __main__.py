import storage_bridge
import gather_manager

async def run(storage, session_factory):
    """
    Main function to initialize sources, construct plans, and execute gather/inject operations.

    :param storage: Storage instance for handling file saving.
    :param session_factory: Session factory for database operations.
    """
    # Context management for sources and log manager in a stacked async with
    async with SC2ReplayStats() as sc2_source, \
               SpawningTool() as spawning_tool_source, \
               GameReplays() as game_replays_source, \
               BatchLogManager(session_factory=session_factory, max_buffer_size=100) as log_manager:

        # Define strategies
        upward_strategy = ScrapeUpward(step=250)
        downward_strategy = ScrapeDownward(step=250)

        # Construct the plan
        plan = [
            Factory(source=sc2_source, strategy=upward_strategy),
            Factory(source=sc2_source, strategy=downward_strategy),
            Factory(source=spawning_tool_source, strategy=upward_strategy),
            Factory(source=spawning_tool_source, strategy=downward_strategy),
            Factory(source=game_replays_source, strategy=upward_strategy),
            Factory(source=game_replays_source, strategy=downward_strategy),
        ]

        # Initialize BatchGatherer
        batch_gatherer = BatchGatherer(
            storage=storage,
            plan=plan,
            logger=log_manager,
            max_concurrent_tasks=10
        )

        # Execute gathering and logging operations
        print("Starting gather process...")
        await batch_gatherer.gather()

        # Uncomment if BatchInjector is used
        # batch_injector = BatchInjector(session_factory=session_factory, logger=log_manager)
        # print("Starting injection process...")
        # await batch_injector.inject()

    print("All operations completed.")

