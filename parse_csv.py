import csv

with open('names.csv', 'r') as csv_file:
	csv_reader = csv.DictReader(csv_file)

	# code to write to a csv file
	with open('test.csv', 'w') as new_file:
		
		csv_writer = csv.writer(new_file, delimiter='\t')

		# code to read csv file
		# next(csv_reader) # skip the first line with the field names
		for line in csv_reader:
			csv_writer.writerow(line)

