from pprint import pprint
import json 
import config as cf
"""
Introduction: this is a script to find the average error of the a 3d printer to the measurment of the design
"""

#assigning a catergory to the data
data = {
	"height": cf.height, 
	"width": cf.width, 
	"inner_diameter": cf.inner_diameter, 
	"thickness": cf.thickness}

#extract all key in dict for illiteration, the keys are used for selecting data
#and print result with a catergory 
keywords = list(data.keys())

f = 4
for k in keywords:
	d = data[k]

	diff = []
	for i in d:
		default = i[0]
		min_diff = abs(round(default - min(i[1]), f))
		max_diff = abs(round(default - max(i[1]),  f))
		# print(min_diff, max_diff)
		diff.append([min_diff, max_diff])

	# print("diff", diff)
	average_diff = []
	
	min_diff = [min(i) for i in diff]
	# print("min diff", min_diff)
	average_min_diff = sum(min_diff)/len(min_diff)

	max_diff = [max(i) for i in diff]
	average_max_diff = sum(max_diff)/len(max_diff)
	average_diff.append([average_min_diff, average_max_diff])

	# print(min_diff)
	# print(max_diff)
	# print(f"{k}")

	result = {"category": k,
			  "min_diff:": min(min_diff),
			  "max_diff": max(max_diff),
			  "average_min_diff": average_min_diff,
			  "average_max_diff": average_max_diff,
			}

	print(json.dumps(result, indent=4))