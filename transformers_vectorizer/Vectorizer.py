import numpy as np


class Vectorizer:
    """

    """

    def __init__(self):
        self.model = None
        self.tokenizer = None

    def load(self):
        """
        Load the model into memory.
        :return:
        """

    def to_vector(self, text: str) -> np.ndarray:
        """
        Transform single text to vector.
        :param text:
        :return:
        """

    def to_vectors(self, text_list: list) -> list:
        """
        Get vector list from text list.
        :param text_list:
        :return:
        """
        return [self.to_list(self.to_vector(t)) for t in text_list]

    def to_list(self, vector):
        if isinstance(vector, np.ndarray):
            rs = vector.tolist()
            if isinstance(rs, np.ndarray):
                rs = [self.to_list(e) for e in rs]
            return rs
        return vector
