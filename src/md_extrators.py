from re import findall


image_regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
url_regex = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"


def extract_markdown_images(text: str):
    alt_texts = findall(image_regex, text)
    return alt_texts


def extract_markdown_urls(text: str):
    urls = findall(url_regex, text)
    return urls
