#!/usr/bin/env python

import HtmlCalendar

if __name__ == "__main__":
	# print(dir(HtmlCalendar))
	cal = HtmlCalendar.MonthlyCalendar()
	print(cal.create())

