class tcolors():
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


class name_join(object):

    def __init__(self, fornavne):
        self.fornavne = fornavne

    def list_names(self):
        for some_names in self.fornavne:
            print tcolors.WARNING + "Navnet er: "+ tcolors.ENDC +" %s" % some_names


drengenavne = name_join([
                    tcolors.OKBLUE + 'Alexander',
                    tcolors.OKBLUE + 'Erik',
                    tcolors.OKBLUE + 'Adam',
                    tcolors.OKBLUE + 'Noah',
                    tcolors.OKBLUE +'Dennis'])

pigenavn = name_join([
                    tcolors.FAIL + 'Magrete',
                    tcolors.FAIL + 'Julie',
                    tcolors.FAIL + 'Stine',
                    tcolors.FAIL +  'Daisy'])


drengenavne.list_names()
pigenavn.list_names()
