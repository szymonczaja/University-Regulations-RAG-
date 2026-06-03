from app.schemas.query import Source

def retrieve(results) -> list:
    source_list = []
    for i, (doc, meta) in enumerate(zip(results['documents'][0], results['metadatas'][0])):
        source = Source(document=meta['document'], page=meta['page'], section=meta['section'], content_preview=doc)
        source_list.append(source)
    return source_list

