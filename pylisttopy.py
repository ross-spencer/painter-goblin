#!/usr/bin/python
# -*- coding: utf-8 -*-


class ListToPy:

    # arbitrary list to output
    arb_list = []
    varname = ''
    fname = ''

    HEADER = "#!/usr/bin/python" + "\n" + "# -*- coding: utf-8 -*- \n\n"

    def __init__(self, arblist, varname, fname):
        self.arb_list = arblist
        self.varname = varname
        self.fname = fname.replace('.py', '') + '.py'

    def list_to_py(self):
        with open(self.fname, 'wb') as f:
            f.write(self.HEADER)
            f.write(self.varname + " = ")
            f.write(
                '[' + ', \\\n'.join('"' + str(x) + '"' for x in self.arb_list) + ']' + "\n")
