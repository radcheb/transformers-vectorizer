# pylint: disable=invalid-name,not-callable,no-member
import torch

from transformers import CamembertTokenizer, CamembertModel

from transformers_vectorizer.Vectorizer import Vectorizer

MODEL_NAME = 'camembert-base'


class CamembertVectorizer(Vectorizer):

    def load(self):
        """
        Load Camembert model from FAIR repo
        :return:
        """
        self.tokenizer = CamembertTokenizer.from_pretrained(MODEL_NAME)
        self.model = CamembertModel.from_pretrained(MODEL_NAME)
        self.model.eval()

    def to_vector(self, text):
        """
        Encode text than extract vector
        :param text:
        :return:
        """
        with torch.no_grad():
            input_ids = torch.tensor(self.tokenizer.encode(text)).unsqueeze(0)
            outputs = self.model(input_ids)
            avg_features = torch.mean(outputs[0], 1).squeeze(0)
            return avg_features.numpy()
