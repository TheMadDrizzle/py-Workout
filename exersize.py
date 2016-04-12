# 
# Workout Testbed
# - Exersize list to pull and build
# 12APR16
# Drew Davis
#

import mastery


class Exersize(object):
    def __init__(self, name, week, mastery):
        self.name = name
        self.mastery = mastery
        self.week = week
