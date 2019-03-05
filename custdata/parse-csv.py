import csv

# # open the file for reading
with open('test_data.csv', 'r') as csv_file:
	csv_reader = csv.DictReader(csv_file)

	# next(csv_reader)  # skip the field names
	# open a new file for writing
	with open('new_test_data.csv', 'w', newline='') as new_file:
		# Only include field names you want in new file. "extrasaction" parameter below allows this to happen without errors.
		fieldnames = ['first_name', 'last_name', 'address_1', 'address_2', 'city', 'state', 'zip_code', 'cust_notes']
		csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, extrasaction='ignore', delimiter=',')

		csv_writer.writeheader()  # delete this line and it won't include the field names in the new file

		# write the new line in new file
		for line in csv_reader:
			csv_writer.writerow(line)
