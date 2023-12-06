# TODO: IMPLEMENT RETRIEVAL AUGMENTED GENERATION USING DATABASES AND VECTORES
# TODO: REFINE BASIC RAG

"""
This module enables the model to access external knowledge sources which enable factual consistency,
improved reliability of the generated responses, and helps to mitigate the problem of "hallucination".
"""

import pandas as pd
import numpy as np
import tqdm
from openai import OpenAI
import ast

client = OpenAI()
MODEL = "text-embedding-ada-002"


def chunk(filepath, sep="\n\n"):
    """
    Chunks contents of file based on the separator.
    Returns the list of chunks.
    """
    with open(filepath) as f:
        contents = f.read().split(sep)[:-1]
    return contents


def embed(v: str):
    """
    :param v: The content to be encoded.
    :return: The content's numerical representation as a 1d array.
    """
    embedding = client.embeddings.create(
        model=MODEL,
        input=v
    )
    return embedding


def create_df(filepath):
    """
    Saves the embeddings generated from the contents of filepath to
    E/e.csv.

    :param filepath: file of contents
    :return: pandas dataframe object
    """
    chunks = chunk(filepath, ch="\n\n")
    data = {
        "text": chunks,
    }
    df = pd.DataFrame(data)
    df["embedding"] = df.text.apply(embed)
    df["norm"] = df.embedding.apply(np.linalg.norm)
    df.to_csv("E/e.csv")

    return df


def f(q, e, norms, k=3):
    """
    Assumes q is a 1d numpy array and e is a 2d numpy array.
    Calculates the distance between vector q and each of the vectors in e.
    Returns the indices of the k most similar vectors.
    """
    dot = np.dot(q, e)

    d = dot / (np.linalg.norm(np.array(q)) * np.array(norms))
    d = d.squeeze()
    return np.argpartition(d, -k)[-k:]


def augment(qry, db):
    q = client.embeddings.create(
        model=MODEL,
        input=qry,
    )

    e = db["embeddings"]
    e = np.array(e)
    e = e.T
    relevant_docs = f(q, e, db["norm"], 3)

    setting = ""
    for i in range(relevant_docs):
        setting += db["text"].loc[i]
    return setting


if __name__ == '__main__':
    df = create_df("../docs/guide.txt")
    query = """The ECO 4 scheme"""
    context = basic_rag(query, df)

    print(f"""
    \n\n{context}\n\n
    """)
