from abc import ABC, abstractmethod
import logging


class FileParser(ABC):
    def __init__(self, file_path : str):
        self.file_path = file_path
        self.logger = logging.getLogger(__name__)

    def parse(self) -> dict:
        self.logger.info("Parsing file %s", self.file_path)
        variables = self._parse()
        self.logger.debug("Parsed variables %s", variables)
        self.logger.info("Finished parsing file %s", self.file_path)
        return variables

    @abstractmethod
    def _parse(self) -> dict:
        pass




