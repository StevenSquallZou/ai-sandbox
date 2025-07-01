from log.logging_config import get_logger


log = get_logger(__name__)

while True:
    user_input = input("\nPlease enter your input: ")
    log.info(f"User input: {user_input}")
