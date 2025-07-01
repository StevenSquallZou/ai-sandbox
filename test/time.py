from log.logging_config import get_logger
import time


log = get_logger(__name__)
log.info("Started")

start_time = time.time()
end_time = time.time()
elapsed_time = end_time - start_time
log.info(f"Time taken: {elapsed_time:.6f} seconds")

log.info("Ended")
