from log.logging_config import get_logger
import os


log = get_logger(__name__)

# os.environ.get():
# Safely retrieves the value of an environment variable.
# Returns None if the variable is not set, avoiding a KeyError.
def test_os_environ():
    deepseek_api_key = os.environ["deepseek_api_key"]

    log.info(f"test_os_environ -> deepseek_api_key: {deepseek_api_key}")


# os.environ["VAR_NAME"]:
# Directly accesses the variable.
# Raises a KeyError if the variable is not set.
def test_os_environ_get():
    deepseek_api_key = os.environ.get("deepseek_api_key")

    log.info(f"test_os_environ_get -> deepseek_api_key: {deepseek_api_key}")


log.info("Started")

# test_os_environ()
test_os_environ_get()

log.info("Ended")
