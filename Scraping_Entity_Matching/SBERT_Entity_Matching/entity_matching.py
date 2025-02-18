from sentence_transformers import SentenceTransformer, util


def compare_names_with_sentence_bert(names1, names2):
    # Load the model
    model = SentenceTransformer('sentence-transformers/multi-qa-MiniLM-L6-cos-v1')

    # Encode all names in names2
    names2_emb = model.encode(names2)

    sbert_results = []
    sbert_similarity_result = []
    similarity = []


    for name1 in names1:
        # Encode name1
        name1_emb = model.encode(name1)
        names2_emb = model.encode(names2)

        max_similarity = -1  # Initialize max similarity score
        most_similar_name = None
        most_similar_index = None

        # Compare name1 with all names in names2
        # Compute dot score between query and all document embeddings
        scores = util.dot_score(name1_emb , names2_emb)[0].cpu().tolist()

        # Combine docs & scores
        doc_score_pairs = list(zip(names2, scores))

        # Sort by decreasing score
        doc_score_pairs = sorted(doc_score_pairs, key=lambda x: x[1], reverse=True)


        sbert_results.append(doc_score_pairs)
        sbert_similarity_result.append(doc_score_pairs[0][0])
        similarity.append(doc_score_pairs[0][1])
        index = names2.index(doc_score_pairs[0][0])

    return sbert_results, sbert_similarity_result, similarity
