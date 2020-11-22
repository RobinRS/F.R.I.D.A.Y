from abc import abstractmethod
from .require_attributes import require_attributes


class Function_Module(metaclass=require_attributes("name", "help_description")):
    """
    A recognized Function_Module accepted by F.R.I.D.A.Y. with a defined response.
    name and help_description must be implemented in all subclasses.
    """
    name = None
    help_description = None