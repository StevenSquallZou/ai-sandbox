import logging
import sys


def get_logger(logger_name):
    log = logging.getLogger(logger_name)
    log.setLevel(logging.INFO)

    # Define log format
    log_format = '%(asctime)s [%(levelname)-5s] %(name)s - %(message)s'
    formatter = logging.Formatter(log_format, datefmt='%Y-%m-%d %H:%M:%S')

    # log lower levels to stdout
    stdout_handler = logging.StreamHandler(stream=sys.stdout)
    stdout_handler.addFilter(lambda rec: rec.levelno <= logging.INFO)
    stdout_handler.setFormatter(formatter)
    log.addHandler(stdout_handler)

    # log higher levels to stderr (red)
    stderr_handler = logging.StreamHandler(stream=sys.stderr)
    stderr_handler.addFilter(lambda rec: rec.levelno > logging.INFO)
    stderr_handler.setFormatter(formatter)
    log.addHandler(stderr_handler)

    return log
