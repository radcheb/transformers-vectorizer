import numpy as np


class Vectorizer:
    """

    """

    def __init__(self):
        self.model = None

    def load(self):
        """
        Load the model into memory.
        :return:
        """
        pass

    def to_vector(self, text: str) -> np.ndarray:
        """
        Transform single text to vector.
        :param text:
        :return:
        """
        pass

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
        else:
            return vector
