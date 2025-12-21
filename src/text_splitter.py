from langchain_text_splitters import RecursiveCharacterTextSplitter


def get_recursive_text_splitter(
    chunk_size: int = 800,
    chunk_overlap: int = 100
) -> RecursiveCharacterTextSplitter:
    """
    Returns a LangChain RecursiveCharacterTextSplitter
    using the latest recommended import.
    """

    return RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=[
            "\n\n",  # paragraphs
            "\n",    # lines
            " ",     # words
            ""       # characters (fallback)
        ],
    )