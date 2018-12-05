'''
Created on Dec 4, 2018

@author: maleone

'''

import re
from datetime import datetime
from collections import defaultdict

class Record:
	def __init__(self, line):
		p_guard = '\[([^\]]*)\]\s+Guard\s\#(\d+)\s+begins shift'
		p_wake =  '\[([^\]]*)\]\s+wakes up'
		p_sleep = '\[([^\]]*)\]\s+falls asleep'

		m = re.search(p_guard, line)
		if m:
			self.type = 'guard'
			self.time = datetime.strptime(m.group(1), '%Y-%m-%d %H:%M')
			self.id = m.group(2)
			return
		else:
			m = re.search(p_wake, line)
			if m:
				self.type = 'wake'
				self.time = datetime.strptime(m.group(1), '%Y-%m-%d %H:%M')
				return
			else:
				m = re.search(p_sleep, line)
				if m:
					self.type='sleep'
					self.time = datetime.strptime(m.group(1), '%Y-%m-%d %H:%M')
					return


records = []

guards = defaultdict(lambda: defaultdict(int))

def process(rec, state):
	if state['state'] == 'initial':
		state['guard'] = rec.id
		state['state'] = 'on_duty'
	elif state['state'] == 'on_duty':
		if rec.type == 'sleep':
			state['sleep_start'] = rec.time.minute
			state['state'] = 'sleeping'
		elif rec.type == 'guard':
			state['guard'] = rec.id
			state['state'] = 'on_duty'
		else:
			print 'Unexpected record type while on_duty. Should be sleep'
	elif state['state'] == 'sleeping':
		if rec.type == 'wake':
			for x in range(int(state['sleep_start']), rec.time.minute) :
				guards[state['guard']][x]+=1
			state['state'] = 'awake'
			del state['sleep_start']
		else:
			print 'Unexpected record type while sleeping. Should be wake'
	elif state['state'] == 'awake':
		if rec.type == 'sleep':
			state['sleep_start'] = rec.time.minute
			state['state'] = 'sleeping'
		elif rec.type == 'guard':
			state['guard'] = rec.id
			state['state'] = 'on_duty'
		else:
			print "Unexpected record type while awake. Should be sleep or guard"

with open('./data/Day04') as f:
	for line in f:
		records.append(Record(line))
	records = sorted(records, key=lambda r: r.time)

	state = {'state': 'initial'}
	for rec in records:
		process(rec, state)

	top_guard = None
	top_count = 0
	for guard in guards.keys():
		top_guard_total_min = 0
		for k in guards[guard].keys():
			top_guard_total_min+=  guards[guard][k]
		if top_guard_total_min > top_count:
			top_count = top_guard_total_min
			top_guard = guard

	top_min_count = 0
	top_min = 0
	for _min in guards[top_guard].keys():
		if guards[top_guard][_min] > top_min_count:
			top_min = _min
			top_min_count = guards[top_guard][_min]

	print "Part 1:", int(top_guard) * top_min
	
	top_min = 0
	top_min_count = 0
	top_guard = None
	for guard in guards.keys():
		for _min in guards[guard].keys():
			if guards[guard][_min] > top_min_count:
				top_min_count = guards[guard][_min]
				top_min = _min
				top_guard = guard
	print "Part 2:", int(top_guard) * top_min



