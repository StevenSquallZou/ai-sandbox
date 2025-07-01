from log.logging_config import get_logger


log = get_logger(__name__)
log.info("Started")

DAY = 365

def test():
    global DAY
    DAY += 1
    log.info(f"DAY in method: {DAY}")

test()

log.info(f"DAY: {DAY}")

log.info("Ended")
