'''
Created on Dec 21, 2017

@author: maleone
'''
from _collections import defaultdict
from collections import Counter


rules = []
art = ['.#.', '..#', '###']

def print_rule(rule, outp=False):
	print "********* FROM ********"
	print rule.inp
	for line in create_mtx(rule.inp):
		print line
	if (outp):
		print "********* TO ********"
		print rule.outp
		for line in create_mtx(rule.outp):
			print line
		print


class Rule(object):

	def __init__(self, inp, outp):
		self.inp = str(inp)
		self.outp = str(outp)
		self.size = len(inp)

	#These functions are apparently meaningless to the interpreter. Even if we return true,
	#there are multiple duplicates in rules
	def __cmp__(self, other):
		#And here we prove the methods never get called
		print "***************************************************************************************"
		return self.inp.strip() == other.inp.strip() and self.outp.strip() == other.outp.strip()
	
	def __eq__(self, other):
		print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
		return self.inp.strip() == other.inp.strip() and self.outp.strip() == other.outp.strip()

def create_mtx(rule_part):
	lines = rule_part.split('/')
	mtx = []
	for line in lines:
		mtx.append(line)
	return mtx

def create_rule_part(mtx):
	s = ''
	for line in mtx:
		s+= "".join(line) + '/'
	return s[:-1]

def rotate_mtx(mtx):
	new_mtx = []
	for i in xrange(len(mtx)):
		line = []
		for j in xrange(len(mtx)-1, -1, -1):
			line.append(mtx[j][i])
		new_mtx.append(line)
	return new_mtx

def rotate_rule(rule):
	mtx = create_mtx(rule.inp)
	mtx = rotate_mtx(mtx)
	return Rule(create_rule_part(mtx), rule.outp)

def flip_mtx(direc, mtx):
	new_mtx = []
	if direc == 'h':
		for line in mtx:
			new_mtx.append(line[::-1])
	else:
		for i in xrange(1, len(mtx) + 1):
			new_mtx.append(mtx[len(mtx) -i])
	return new_mtx

def flip_rule(axis, rule):
	mtx = create_mtx(rule.inp)
	mtx = flip_mtx(axis, mtx)
	return Rule(create_rule_part(mtx), rule.outp)


def get_trans_rules(rule):
	_rules = set()
	flip = flip_rule('v', rule)
	for _ in xrange(4):
		_rules.add(rule)
		_rules.add(flip)
		rule = rotate_rule(rule)
		flip = rotate_rule(flip)
	return list(set(_rules))

def slice_matrix(mtx, y, x, size):
	mtx = mtx[y:y+size][::]
	for i in xrange(len(mtx)):
		mtx[i] = mtx[i][x:x+size]
	return mtx

def transform(mtx):
	p = create_rule_part(mtx)
	matches = set()
	for rule in rules:
		if p == rule.inp:
# 			return create_mtx(rule.outp)
#Matching rules have identical inp and outp values, but for some reason python still sees them as dups
			matches.add(rule)
	if len(matches) > 1:
		print len(matches), "rules match"
		print "MATCHES"
		for r in matches:
			print_rule(r, True)
		print "MATCHES"
	return create_mtx(matches.pop().outp)

	print "No rule for", p

def set_submatrix(mtx, submtx, y, x, size):
	a = 0
	for x in xrange(x, x+size):
		l = list(mtx[x])
		b = 0
		for i in xrange(y, y + size):
			l[i] = submtx[a][b]
			b+= 1
		mtx[x] = "".join(l)
		a+= 1
def print_mtx(mtx):
	for line in mtx:
		print line

with open("data/Day21") as f:
	for line in f:
		inp, outp = line.strip().split(' => ')
		rule = Rule(inp, outp)
		rules.extend(get_trans_rules(rule))
	#Fruitless attempts to have no dups in my rules set
	rules = list(set(rules))
	rulesdict = defaultdict(int)
	for rule in rules:
		rulesdict[rule]+= 1
	rules = set()
	for k,v in rulesdict.iteritems():
		if v == 1:
			rules.add(k)
	#And here we see dups. For some reason, the Rule class is not subject to equality comparison
	for rule in rules:
		print rule.inp, " => ", rule.outp

for _ in xrange(5):
	if len(art) % 3 == 0:
		new_size = len(art) + len(art) / 3
		new_art = ["*" * new_size for _ in xrange(new_size)]
		submatrices = []
		for i in xrange(0, len(art), 3):
			for j in xrange(0, len(art), 3):
				mtx = slice_matrix(art, i, j, 3)
				mtx = transform(mtx)
				submatrices.append(mtx[::])
		for i in xrange(0, new_size, 4):
			for j in xrange(0, new_size, 4):
				set_submatrix(new_art, submatrices.pop(0), i, j, 4)
				
		for row in new_art :
			new_art = [[new_art[j][i] for j in range(len(new_art))] for i in range(len(new_art[0]))]
		art = new_art[::]
	elif len(art) % 2 == 0:
		new_size = len(art) + len(art) / 2
		new_art = ["*" * new_size for _ in xrange(new_size)]
		submatrices = []
		for i in xrange(0, len(art), 2):
			for j in xrange(0, len(art), 2):
				mtx = slice_matrix(art, i, j, 2)
				mtx = transform(mtx)
# 				print "Sub Matrix"
# 				print_mtx(mtx)
				submatrices.append(mtx[::])
		for i in xrange(0, new_size, 3):
			for j in xrange(0, new_size, 3):
				set_submatrix(new_art, submatrices.pop(0), i, j, 3)
# 		print "Matrix"
# 		print_mtx(new_art)
		for row in new_art :
			new_art = [[new_art[j][i] for j in range(len(new_art))] for i in range(len(new_art[0]))]
		art = new_art[::]

count = 0
for line in art:
	print line
	counter = Counter(line)
	count+= counter['#']

print "Part1:", count

#135 too low
#363 too high
