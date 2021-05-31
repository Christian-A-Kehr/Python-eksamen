
class NoOneValueError(ValueError):
    
    def __init__(self, *args, **kwargs):
        ValueError.__init__(self, *args, **kwargs)

class new_spec_found(ValueError):
    
    def __init__(self, *args, **kwargs):
        ValueError.__init__(self, *args, **kwargs)
