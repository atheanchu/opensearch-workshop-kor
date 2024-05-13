mapping = {
    "settings": {
        "index": {
            "knn": True,
            "knn.space_type": "consinesimil",
        }
    },
    "mapping": {
        "properties": {
            "id": {"type": "long"},
            "position": {"type": "keyword"},
            "years_of_experience": {"type": "long"},
            "created_at": {"type": "date"},
            "created_at": {"type": "date"},
            "text_embeddings": {
                "type": "knn_vector",
                "dimension": 4096,
            },
        }
    },
}


query = {
    "size": 30,
    "query": {
        "bool": {
            "must": {
                "knn": {
                    "text_embeddings": {
                        "vector": input_vector,
                        "k": 300,
                    },
                },
            },
            "filter": [
                {"term": {"company_name.keyword": "(주) 리멤버"}},
                {"term": {"position.keyword": "Manager"}},
                {"term": {"years_of_experience": {"gte": 3}}},
            ],
        },
    },
}
