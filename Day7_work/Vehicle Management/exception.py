class VehicleError(Exception):
    """Base class for vehicle -related exceptions."""
    pass

class OwnerAlreadyExistsError(VehicleError):
    """raised when trying to add an owner that already exit ."""
    def __init__(self,owner_name):
        message =f"Owner: '{owner_name}' already exists."
        super().__init__(message)

class InvalidbatteryCapacityError(VehicleError):
    """ Raised when the battery capacity is invalid"""
    def __init__(self, capacity):
        super().__init__(f"Invalid battery capacity:{capacity}. Must be a positive number.")

