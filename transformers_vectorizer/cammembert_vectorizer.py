import torch

from transformers_vectorizer.Vectorizer import Vectorizer

REPO = 'pytorch/fairseq'
MODEL = 'camembert.v0'


class CamembertVectorizer(Vectorizer):

    def load(self):
        """
        Load Camembert model from FAIR repo
        :return:
        """
        camembert = torch.hub.load(REPO, MODEL)
        camembert.eval()  # disable dropout (or leave in train mode to finetune)
        self.model = camembert

    def to_vector(self, text):
        """
        Encode text than extract vector
        :param text:
        :return:
        """
        with torch.no_grad():
            tokens = self.model.encode(text)
            return self.model.extract_features(tokens).numpy().squeeze(0)
