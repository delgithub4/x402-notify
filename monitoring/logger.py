from core.logging_config import logger


class MonitoringLogger:

    def info(
        self,
        message,
    ):

        logger.info(message)
