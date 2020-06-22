'''
Type annotations are stores in the __annotations__ attribute of the function.
No checks, enforcement, validation, or any other actions is performed.
In other words, annotations have no meaning to the Python interpreter.
They are just metadata that may be used by tools.
A static type checker is required to catch the type annotation error without
running the code. Mypy is one of the most common tool.
'''
def clip(text: str, max_len: int = 80) -> str:
    """Return text clipped at the last space before or after max_len
    """
    end = None
    if len(text) > max_len:
        # Search from 0 to max_len
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            # Search from max_len to end of the text
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after

    # If no spaces are found, set end to the end of the text
    if end is None:
        end = len(text)
    
    return text[:end].rstrip()


if __name__ == "__main__":
    print(clip("hello world", 5))
    # mypy clip.py should report a type hint error for below:
    #   error: Argument 2 to "clip" has incompatible type "str"; expected "int"
    print(clip("hello", "world"))