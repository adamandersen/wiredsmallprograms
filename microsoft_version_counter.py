# -*- coding: utf-8 -*-

# make some colors to the print, make me feel good seeing it
class tcolors():
    HEADER = '\033[95m' # PINK
    OKBLUE = '\033[94m' # BLUE
    OKGREEN = '\033[92m' # GREEN
    WARNING = '\033[93m' # YELLOW
    FAIL = '\033[91m' # RED
    ENDC = '\033[0m' # NO COLOR

# the empty box windows object
class windows(object):

    # initiate the object by putting in data from windows inside stuffed_in_objects
    def __init__(self, stuffed_in_objects):
        self.stuffed_in_objects = stuffed_in_objects

    # do some printing and counting with the data imported
    def show_windows(self):

        # counter start to show how many versions there is
        counter = 0

        # print a top header
        print "\n" +tcolors.WARNING + '-' * 90
        print "\n\t\t\tAdam's Microsoft Counter 2016\n"
        print tcolors.WARNING + '-' * 90

        # loop through both key and item values from dictanary data import
        for versions, date in self.stuffed_in_objects.items():
            # do some printing to show the data nicely
            print tcolors.OKBLUE + "\tRelease version:" + tcolors.OKGREEN + versions + tcolors.HEADER + "\t\tRelase date:"+ tcolors.FAIL + date

            # increment the counter for each outputed version/release date
            counter += 1
        # print a footer with the total amount of versions
        print tcolors.WARNING + '-' * 90
        print "\n\t\t\tOverall released versions by Microsoft: %d\n"  % counter
        print tcolors.WARNING + '-' * 90 + "\n"

# this is the data import by a dictanary key, items
# variable verions places the data inside the class windows object. It fills the
# emtpy box with data
versions = windows({
                    "Windows 1.01": "20 November 1985",
                    "Windows 1.02": "May 1986",
                    "Windows 1.03": "August 1986",
                    "Windows 1.04": "April 1987",
                    "Windows 2.04": "9 December 1987",
                    "Windows 2.10": "27 May 1988",
                    "Windows 2.11": "13 March 1989",
                    "Windows 3.0": "22 May 1990",
                    "Windows 3.1": "April 1992",
                    "Windows NT 3.1": "27 july 1993",
                    "Windows NT 3.2": "November 1993",
                    "Windows NT 3.5": "22 November 1994",
                    "Windows NT 3.51": "30 May 1995",
                    "Windows 95": "24 August 1995",
                    "Windows NT 4.0": "24 August 1996",
                    "Windows 98": "25 June 1998",
                    "Windows 2000": "17 February 2000",
                    "Windows ME": "14 September 2000",
                    "Windows XP": "25 October 2001",
                    "Windows XP x64": "25 April 2005",
                    "Windows Vista": "30 January 2007",
                    "Windows 7": "22 Oktober 2009",
                    "Windows 8": "26 Oktober 2012",
                    "Windows 8.1": "17 Oktober 2013",
                    "Windows 10": "29 July 2015"})

# call the class to do magic
versions.show_windows()
