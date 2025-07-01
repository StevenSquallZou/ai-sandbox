import os
import yaml
from langchain_core.prompts import ChatPromptTemplate
from log.logging_config import get_logger
from langchain_openai.chat_models.base import BaseChatOpenAI


# Initialize logger
log = get_logger(__name__)


def load_config():
    base_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_path, "../config/config.yaml")
    log.info(f"config path: {config_path}")

    with open(config_path, "r", encoding="utf-8") as config_file:
        return yaml.safe_load(config_file)


def print_config(config, prefix=""):
    for key, value in config.items():
        if isinstance(value, dict):
            print_config(value, prefix=f"{prefix}{key}.")
        else:
            log.info(f"{prefix}{key}: {value}")


def main():
    log.info("langchain_prompt started")

    try:
        config = load_config()
        # log.info("configurations: ")
        # print_config(config)

        log.info(f"api_base_url: {config["ai"]["api_base_url"]}")

        api_key_env_var = config["ai"]["api_key_env_var"]
        # log.info(f"api_key: {os.environ[api_key_env_var]}")

        print("creating ChatOpenAI instance...")
        llm = BaseChatOpenAI(
            model='deepseek-chat',  # 使用DeepSeek聊天模型
            openai_api_key=os.environ[api_key_env_var],  # 替换为你的API易API密钥
            openai_api_base=config["ai"]["api_base_url"],  # API易的端点
            max_tokens=1024  # 设置最大生成token数
        )
        print("created ChatOpenAI instance")

        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are helpful assistant."),
            ("user", "{input}"),
        ])

        chain = prompt | llm

        print("invoking chain...")
        result = chain.invoke({"input": "写一篇关于AI技术的文章, 100字以内"})
        print(f"AI response: {result}")

    except KeyError as e:
        log.error(f"Missing environment variable or config key: {e}")
    except FileNotFoundError as e:
        log.error(f"Configuration file not found: {e}")
    except Exception as e:
        log.error(f"An unexpected error occurred: {e}")

    log.info("langchain_prompt ended")


if __name__ == "__main__":
    main()