import os as _os

# available frameworks
_VALID_FRAMEWORKS = ('tensorflow', 'pytorch')

# use tensorflow as default
_FRAMEWORK = 'tensorflow'

if 'DEEPTIME_FRAMEWORK' in _os.environ:
    _framework = _os.environ['DEEPTIME_FRAMEWORK']
    if _framework not in _VALID_FRAMEWORKS:
        raise ValueError("Found environment variable DEEPTIME_FRAMEWORK={fw} but only {valids} are valid choices."
                         .format(fw=_framework, valids=_VALID_FRAMEWORKS))
    _FRAMEWORK = _framework

if _FRAMEWORK == 'tensorflow':
    from .tensorflow_backend import *
elif _FRAMEWORK == 'pytorch':
    from .pytorch_backend import *
else:
    raise ValueError("Selected framework is {} although only frameworks {} are available."
                     .format(_FRAMEWORK, _VALID_FRAMEWORKS))


def framework():
    """
    Yields the used framework
    :return: one of 'tensorflow' and 'pytorch'
    """
    return _FRAMEWORK
