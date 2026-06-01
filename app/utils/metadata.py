
def create_metadata_dict(file_name : str, page_number : int) -> dict[str, str | int]:
    return {
        'Document' : file_name, 
        'Page' : page_number
    }