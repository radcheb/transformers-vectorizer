from transformers_vectorizer.cammembert_vectorizer import CamembertVectorizer


def test_camembert_vectors():
    camembert_vectorizer = CamembertVectorizer()
    camembert_vectorizer.load()
    text = "J'aime le camembert!"
    vectors = camembert_vectorizer.to_vectors([text])
    assert len(vectors) == 1
    assert vectors[0].shape == (10, 768)
