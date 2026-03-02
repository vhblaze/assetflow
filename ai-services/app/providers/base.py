from abc import ABC, abstractmethod

class BaseProvider(ABC):
    @abstractmethod
    def chat(self, system_prompt: str, user_prompt: str, max_tokens: int = 220) -> str:
        raise NotImplementedError