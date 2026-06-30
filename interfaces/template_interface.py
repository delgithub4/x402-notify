from abc import ABC, abstractmethod


class TemplateInterface(ABC):

    @abstractmethod
    def render(
        self,
        template,
        data,
    ):
        ...
