import time


class PerformanceMonitor:

    async def measure(
        self,
        coroutine,
    ):

        started = time.perf_counter()

        result = await coroutine

        return {
            "elapsed": time.perf_counter() - started,
            "result": result,
        }
