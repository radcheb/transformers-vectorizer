from transformers_vectorizer.cammembert_vectorizer import CamembertVectorizer


def test_camembert_vectors():
    camembert_vectorizer = CamembertVectorizer()
    camembert_vectorizer.load()
    text = "J'aime le camembert!"
    vectors = camembert_vectorizer.to_vectors([text])
    assert len(vectors) == 1
    assert len(vectors[0]) == 768
