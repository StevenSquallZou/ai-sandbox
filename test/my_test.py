from log.logging_config import get_logger


log = get_logger(__name__)
log.info("Started")

# log.info("Hello World !!!")
log.info(f"__name__: {__name__}")
log.info(f"__file__: {__file__}")

log.info("Ended")
