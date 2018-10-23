class ImproperlyConfigured(Exception):
    """ Raised when some part of the VeriPy application is improperly configured.
    This could be that the page fixtures are invalid, or that the application
    cannot reasonably make judgements about the specified environment variables,
    or if the application is configured multiple times in a conflicting manner.
    """
    pass
