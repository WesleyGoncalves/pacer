from enum import Enum


# @app.template_filter()
def to_string(obj):
    if isinstance(obj, Enum):
        return obj.value

    # Jinja uses default behavior
    return obj
