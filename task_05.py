#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""checking for required or optional defaults"""
def defaults(my_required, my_optional=True):
    """check for similarities"

    Args:
        my_required (bool): either True or False.
        my_optional (bool, optional): either True or False. Default: True.

    Returns:
        bool: if my_required is the same object as my_optional, return True.
        if not, return False


    Examples:

        >>> defaults(True)
        True

        >>> defaults(True, False)
        False

        >>> defaults(False, False)
        True

        """

    return my_optional is my_required
