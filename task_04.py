#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" check for how many kittens"""

def too_many_kittens

"""

    Args:
         kittens (int): the number of kittens
         litterboxes (int): the number of available litterboxes
         catfood (bool): whether or not any catfood exists

    Returns:
          bool: if the number of kittens is bigger than the number of litterboxes
          or there is no catfood available, return true. Else return false.

    Examples:
        >>> too_many_kittens(12, 12, False)
        True

        >>> too_many_kittens(13, 12, True)
        True

        >>> too_many_kittens(12, 13, True)
        False

        """

        return not (litterbox >= kittens and catfood)
    
        
