import os
import yaml
from openai import OpenAI
from log.logging_config import get_logger
import time


# Initialize logger
log = get_logger(__name__)


def print_config(config, prefix=""):
    for key, value in config.items():
        if isinstance(value, dict):
            print_config(value, prefix=f"{prefix}{key}.")
        else:
            log.info(f"{prefix}{key}: {value}")


def load_config():
    base_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_path, "../config/config.yaml")
    log.info(f"config path: {config_path}")

    with open(config_path, "r", encoding="utf-8") as config_file:
        return yaml.safe_load(config_file)


# Initialize OpenAI client
def initialize_ai_client(api_key, base_url):
    return OpenAI(api_key=api_key, base_url=base_url)


def call_ai(ai_client, config, user_input):
    log.info("AI thinking...")
    start_time = time.time()

    response = ai_client.chat.completions.create(
        model=config["ai"]["model"],
        messages=[
            {"role": "system", "content": config["ai"]["system_content"]},
            {"role": "user", "content": user_input},
        ],
        stream=False,
        max_tokens=config["ai"]["max_tokens"],
        temperature=config["ai"]["temperature"],
        n=config["ai"]["n"],
        top_p=config["ai"]["top_p"],
        presence_penalty=config["ai"]["presence_penalty"],
        response_format={"type": config["ai"]["response_format"]},
        seed=config["ai"]["seed"],
    )

    end_time = time.time()
    elapsed_time = end_time - start_time

    log.info(f"AI answer ({elapsed_time:.2f} seconds): \n")
    for index, choice in enumerate(response.choices):
        log.info(f"choice {index}: \n{choice.message.content}\n")


# Process user input and get AI response
def process_user_input(ai_client, config):
    exit_commands = {"exit", "quit", "q"}

    while True:
        log.info("------------------------------------------------------------------------------------")
        user_input = input("Ask AI a question: ")
        if user_input.lower() in exit_commands:
            log.info("Exiting...")
            break

        call_ai(ai_client, config, user_input)


# one-time hardcoded input for testing
def process_hardcoded_input(ai_client, config):
    # user_input = "写一首关于秋天的诗"
    # user_input = "描述一个梦想中的度假胜地"
    # user_input = "生成描述夏天的句子"
    # user_input = "讨论一下数据转型的意义"
    # user_input = "简短的描述小学生的一天"

    # response_format:
    # Prompt must contain the word 'json' in some form to use 'response_format' of type 'json_object'
    # user_input = "用json格式输出一个用Python写的冒泡排序算法"
    # user_input = "输出一个用Python写的冒泡排序算法" # default response format is markdown

    # seed:
    user_input = "用100个字以内给我将一个宇宙是如何开始的故事"

    log.info(f"user_input: {user_input}")

    call_ai(ai_client, config, user_input)


def multiple_process_hardcoded_input(ai_client, config, times):
    for i in range(times):
        log.info(f"running loop index: {i}")

        process_hardcoded_input(ai_client, config)


def main():
    log.info("sdk_call started")

    try:
        config = load_config()
        log.info("configurations: ")
        print_config(config)

        api_key_env_var = config["ai"]["api_key_env_var"]
        api_key = os.environ[api_key_env_var]
        # log.info(f"api_key: {api_key}")

        ai_client = initialize_ai_client(api_key, config["ai"]["api_base_url"])
        # process_user_input(ai_client, config)
        # process_hardcoded_input(ai_client, config)
        multiple_process_hardcoded_input(ai_client, config, 1)

    except KeyError as e:
        log.error(f"Missing environment variable or config key: {e}")
    except FileNotFoundError as e:
        log.error(f"Configuration file not found: {e}")
    except Exception as e:
        log.error(f"An unexpected error occurred: {e}")

    log.info("sdk_call ended")


if __name__ == "__main__":
    main()
