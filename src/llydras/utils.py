from typing import Any

def _validate_arguments(**kwargs: Any) -> tuple[str, Any]:
    non_none_kwargs = {key: value for key, value in kwargs.items() if value is not None}

    if len(non_none_kwargs) == 0:
        raise ValueError('Must have at least one non-None argument.')
    elif len(non_none_kwargs) > 1:
        raise ValueError(f'Too many arguments given: {tuple(kwargs_no_null.keys())}')

    return next(iter(non_none_kwargs.items()))