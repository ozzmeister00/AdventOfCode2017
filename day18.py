import collections

class InstructionParser(object):
    def __init__(self, instructionSet):
        self.instructionSet = instructionSet
        self.instructions = {'set':self.set,
                             'add':self.add,
                             'mul':self.multiply,
                             'mod':self.mod,
                             'snd':self.snd,
                             'rcv':self.recover,
                             'jgz':self.jgz
                             }

        self.lastSoundPlayed = 0
        self.registers = collections.defaultdict(int)

    def run(self):
        i = 0
        while 0 <= i < len(self.instructionSet):
            i += self.handleInstruction(self.instructionSet[i])

    def handleInstruction(self, instructionLine):
        cmd = instructionLine.split(' ')[0]
        return self.instructions[cmd](instructionLine.split(' ')[1:])

    def getValue(self, inVal):
        try:
            return int(inVal)
        except ValueError:
            return self.registers[inVal]

    def set(self, args):
        self.registers[args[0]] = self.getValue(args[1])
        return 1

    def add(self, args):
        self.registers[args[0]] = self.getValue(args[1])
        return 1

    def multiply(self, args):
        self.registers[args[0]] *= self.getValue(args[1])
        return 1

    def mod(self, args):
        self.registers[args[0]] = self.registers[args[0]] % self.getValue(args[1])
        return 1

    def snd(self, args):
        self.lastSoundPlayed = self.getValue(self.registers[args[0]])
        return 1

    def recover(self, args):
        if self.lastSoundPlayed:
            self.registers[args[0]] = self.lastSoundPlayed
            raise Exception('Breaking because last sound played was greater than 0: ', self.lastSoundPlayed)
        return 1

    def jgz(self, args):
        if self.registers[args[0]] > 0:
            return self.getValue(args[1])
        return 1


testInput = '''set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2'''

puzzleInput = '''set i 31
set a 1
mul p 17
jgz p p
mul a 2
add i -1
jgz i -2
add a -1
set i 127
set p 316
mul p 8505
mod p a
mul p 129749
add p 12345
mod p a
set b p
mod b 10000
snd b
add i -1
jgz i -9
jgz a 3
rcv b
jgz b -1
set f 0
set i 126
rcv a
rcv b
set p a
mul p -1
add p b
jgz p 4
snd a
set a b
jgz 1 3
snd b
set f 1
add i -1
jgz i -11
snd a
jgz f -16
jgz a -19'''

processor = InstructionParser(puzzleInput.split('\n'))

processor.run()

