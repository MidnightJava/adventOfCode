'''
Created on Dec 21, 2017

@author: maleone
'''

rules = []
art = ['.#.', '..#', '###']
# art = []
# art.append('12345678')
# art.append('abcdefgh')
# art.append('ijklmnop')
# art.append('qrstuvwx')
# art.append('yz!@#$%^')
# art.append('&*()_+=]')
# art.append('];,."`-{')
# art.append('}\|<>/,.')

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
		self.inp = inp
		self.outp = outp
		self.size = len(inp)

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
	rules = set()
	mtx = create_mtx(rule.inp)
	for _ in xrange(4):
		mtx = rotate_mtx(mtx)
		rules.add(Rule(create_rule_part(mtx), rule.outp))
		rules.add(Rule(create_rule_part(flip_mtx('h', mtx)), rule.outp))
		rules.add(Rule(create_rule_part(flip_mtx('v', mtx)), rule.outp))
	return list(rules)


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
	rules = []
# 	print "RULE"
# 	print_rule(rule)
# 		print "ROTATE " , i
# 		new_rule = rotate_rule(i, rule)
# 		print_rule(new_rule)
	rules.extend(rotate_rule(rule))
# 	print "FLIP HORIZONTAL"
	new_rule = flip_rule('h', rule)
# 	print_rule(new_rule)
	rules.append(flip_rule('h', rule))
# 	print "FLIP VERTICAL"
	new_rule = flip_rule('v', rule)
# 	print_rule(new_rule)
	rules.append(flip_rule('v', rule))
	return rules

def slice_matrix(mtx, y, x, size):
	mtx = mtx[y:y+size][::]
	for i in xrange(len(mtx)):
		mtx[i] = mtx[i][x:x+size]
	return mtx

def transform(mtx):
	p = create_rule_part(mtx)
	for rule in rules:
		if p == rule.inp:
			return create_mtx(rule.outp)
	print "No rule for", p

def set_submatrix(mtx, submtx, y, x, size):
	for y in xrange(y, y+size):
		l = list(mtx[y])
		for i in xrange(x, x + size):
			l[i] = submtx[y][i]
		mtx[y] = "".join(l)

with open("data/Day21") as f:
	for line in f:
		inp, outp = line.strip().split(' => ')
		rule = Rule(inp, outp)
		rules.append(rule)
		rules.extend(get_trans_rules(rule))
	rules = list(set(rules))

# for rule in rules:
# 	print rule.inp


# print "rule"
# rule = rules[0]
# print_rule(rule)
# print
# print "rotate 1"
# print_rule(rotate_rule(1, rule))
# print
# print "rotate 2"
# print_rule(rotate_rule(2, rule))
# print
# print "rotate 3"
# print_rule(rotate_rule(3, rule))
# print
# print "flip horizontal"
# print_rule(flip_rule('h', rule))
# print
# print "flip vertical"
# print_rule(flip_rule('v', rule))
# print

for _ in xrange(5):
	if len(art) % 2 == 0:
		new_size = len(art) + len(art) / 2
		new_art = ["*" * new_size for _ in xrange(new_size)]

		for i in xrange(0, new_size, 3):
			for j in xrange(0, new_size, 3):
				mtx = slice_matrix(art, i, j, 2)
				mtx = transform(mtx)
				set_submatrix(new_art, mtx, i+1, j+1, 3)
		art = new_art
	elif len(art) % 3 == 0:
		new_size = len(art) + len(art) / 3
		new_art = ["*" * new_size for _ in xrange(new_size)]
		for i in xrange(0, new_size, 2):
			for j in xrange(0, new_size, 2):
				mtx = slice_matrix(art, i, j, 3)
				mtx = transform(mtx)
				set_submatrix(new_art, mtx, i, j, 4)
		art = new_art

for line in art:
	print line
