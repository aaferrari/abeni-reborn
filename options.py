
class Options:
    def __init__(self):
        self.Readapprc()
        import sys

    def Readapprc(self):
        import string, sys, os
        appdir = os.path.abspath(os.path.join(os.getcwd(), sys.path[0]))
        f = open('%s/pybuilderrc' % appdir)
        line = f.readline()
        while line:
            if string.find(line, 'debug') != -1:
                self.debug = string.strip(string.split(line, '=')[1])
            line = f.readline()
        f.close()


    def Prefs(self):
        pref = {}
        pref['debug'] = self.debug

        return pref
