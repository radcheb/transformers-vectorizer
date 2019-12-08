"""

"""
import logging
from transformers_vectorizer.cammembert_vectorizer import CamembertVectorizer

__version__ = "0.0.1"

logger = logging.getLogger(__name__)  # pylint: disable=invalid-name

VECTORIZERS = {
    "CAMMEMBERT": CamembertVectorizer,
    "BERT": None
}


def from_name(name: str):
    """
    Get vectorizer by its name
    :param name:
    :return:
    """
    logger.info("Will load {}", name)
    return VECTORIZERS[name]()
