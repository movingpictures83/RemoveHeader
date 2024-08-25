class RemoveHeaderPlugin:
    def input(self, inputfile):
        self.infile = open(inputfile, 'r')

    def run(self):
        pass

    def output(self, outputfile):
        self.outfile = open(outputfile, 'w')
        self.infile.readline()
        for line in self.infile:
            self.outfile.write(line)
