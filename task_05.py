#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Input blood pressure and get your result."""


BLOODPRESS = int(raw_input('What is your blood pressure? '))

if BLOODPRESS <= 89:
    BP_STATUS = 'Low'
elif BLOODPRESS > 89 and BLOODPRESS <= 119:
    BP_STATUS = 'Ideal'
elif BLOODPRESS > 119 and BLOODPRESS <= 139:
    BP_STATUS = 'Warning'
elif BLOODPRESS > 139 and BLOODPRESS <= 159:
    BP_STATUS = 'High'
elif BLOODPRESS > 159:
    BP_STATUS = 'Emergency'

print 'Your status is currently: {}!'.format(BP_STATUS)
