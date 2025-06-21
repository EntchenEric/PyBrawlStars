def parse_tag(tag: str) -> str:
    new_tag = tag
    if not tag.startswith("#"):
        new_tag = "#" + tag

    new_tag = new_tag.replace("#", "%23")

    return new_tag