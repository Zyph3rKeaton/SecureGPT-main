from dataclasses import dataclass
import sys
from typing import Optional
import argparse
from loguru import logger
from pentestgpt.test_connection import main as test_connection
from pentestgpt.utils.pentest_gpt import pentestGPT

@dataclass
class PentestConfig:
    log_dir: str
    reasoning_model: str
    parsing_model: str
    use_logging: bool
    use_api: bool

class PentestGPTCLI:
   
    DEFAULT_CONFIG = {
        "log_dir": "logs",
        "reasoning_model": "gpt-4-o",
        "parsing_model": "gpt-4-o",
    }
    
    VALID_MODELS = {
        "reasoning": ["gpt-4", "gpt-4-turbo"],
        "parsing": ["gpt-4-turbo", "gpt-3.5-turbo-16k"]
    }

    def __init__(self):
        self.parser = self._create_parser()

    def _create_parser(self) -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(description="PentestGPT")
        
        parser.add_argument(
            "--log_dir",
            type=str,
            default=self.DEFAULT_CONFIG["log_dir"],
            help="Path to the log directory for storing conversations"
        )
        
        parser.add_argument(
            "--reasoning_model",
            type=str,
            default=self.DEFAULT_CONFIG["reasoning_model"],
            choices=self.VALID_MODELS["reasoning"],
            help="Model for higher-level cognitive tasks"
        )
        
        parser.add_argument(
            "--parsing_model",
            type=str,
            default=self.DEFAULT_CONFIG["parsing_model"],
            choices=self.VALID_MODELS["parsing"],
            help="Model for structural and grammatical language processing"
        )
        
        parser.add_argument(
            "--logging",
            action="store_true",
            default=False,
            help="Enable data collection through langfuse logging"
        )
        
        parser.add_argument(
            "--useAPI",
            action="store_true",
            default=True,
            help="Deprecated: Set to False only for testing with cookie"
        )
        
        return parser

    def parse_args(self) -> PentestConfig:
        args = self.parser.parse_args()
        return PentestConfig(
            log_dir=args.log_dir,
            reasoning_model=args.reasoning_model,
            parsing_model=args.parsing_model,
            use_logging=args.logging,
            use_api=args.useAPI
        )

def check_connection() -> bool:
    try:
        return test_connection()
    except Exception as e:
        logger.error(f"Connection test failed: {e}")
        return False

def run_pentest(config: PentestConfig) -> None:
    try:
        pentest_handler = pentestGPT(
            reasoning_model=config.reasoning_model,
            parsing_model=config.parsing_model,
            useAPI=config.use_api,
            log_dir=config.log_dir,
            use_langfuse_logging=config.use_logging
        )
        pentest_handler.main()
    except Exception as e:
        logger.error(f"PentestGPT execution failed: {e}")
        sys.exit(1)

def main():
    cli = PentestGPTCLI()
    config = cli.parse_args()
    
    if not check_connection():
        logger.error("Connection test failed. Exiting...")
        sys.exit(1)
    
    run_pentest(config)

if __name__ == "__main__":
    main()
