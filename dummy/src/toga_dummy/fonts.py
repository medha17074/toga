from .utils import LoggedObject, not_required


@not_required  # Testbed coverage is complete for this class
class Font(LoggedObject):
    def __init__(self, interface):
        super().__init__()
        self.interface = interface

    def __eq__(self, other):
        return all(
            [
                self.interface.family == other.interface.family,
                self.interface.size == other.interface.size,
                self.interface.weight == other.interface.weight,
                self.interface.variant == other.interface.variant,
                self.interface.style == other.interface.style,
            ]
        )
