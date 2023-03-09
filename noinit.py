class _NoInit:
    def __init__(self):
        raise Exception(f"'{self.__class__.__name__}' is a static class not meant to be instantiated")