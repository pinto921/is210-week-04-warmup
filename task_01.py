#!/usr/bin/env python
#-*- coding: utf-8
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
      """returns a string with winks and nudges.

     Args:
        wink (str): a srtring to be repeated by the number assigned to numwink.
        numwink (int,optional): The number of times wink and nudge will be
                               repeated. Default: 2

     Returns:
        str: concatenate winks and nudges for number of times assigned to numwink to the end of the string.

     Exxamples:

            >>> know_what_i_mean('wink')
            'Know what I mean? wink wink, nudge nudge'


            >>> know_what_i_mean('wink ',1)
            'know what I mean?wink, nudge'
        """
      wink = (wink * numwink).strip()
      nudges = ('nudge ' * numwink).strip()
      retstr = 'know what I mean? {}, {}'. format(winks, nudges)
      retstr = 'Know what I mean? {0}, {1}'.format(winks,nudges)
      return retstr
