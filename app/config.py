from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    telegram_bot_token: str
    telegram_admin_username: str
    log_path: str = "./logs/{time:YYYY-MM-DD!UTC}.log"
    parse_mode: str = "HTML"

settings = Settings()
