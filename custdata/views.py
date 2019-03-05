from django.shortcuts import render
import csv, io
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import Customers


@permission_required('admin.can_add_log_entry')
def contact_upload(request):
	template = 'contact_upload.html'

	prompt = {'order': 'Order of the CSV'}  # remove this later
	

	if request.method == "GET":
		return render(request, template, prompt)

	csv_file = request.FILES['file']

	if not csv_file.name.endswith('.csv'):
		messages.error(request, 'This is not a csv file')

	data_set = csv_file.read().decode('UTF-8')
	io_string = io.StringIO(data_set)
	next(io_string)   ## skip the first line as it contains the field names
	for column in csv.reader(io_string, delimiter=',', quotechar="|"):
		_, created = Customers.objects.update_or_create(
			first_name=column[1],
			last_name=column[2],
			address_1=column[3],
			address_2=column[4],
			city=column[5],
			state=column[6],
			zip_code=column[7]
			)
		context = {}
		return render(request, template, context)

# # open the file for reading
# with open('test_data.csv', 'r') as csv_file:
# 	csv_reader = csv.DictReader(csv_file)

# 	# next(csv_reader)  # skip the field names
# 	# open a new file for writing
# 	with open('new_test_data.csv', 'w', newline='') as new_file:
# 		# Only include field names you want in new file. "extrasaction" parameter below allows this to happen without errors.
# 		fieldnames = ['first_name', 'last_name', 'address_1', 'address_2', 'city', 'state', 'zip_code', 'cust_notes']
# 		csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, extrasaction='ignore', delimiter=',')

# 		csv_writer.writeheader()  # delete this line and it won't include the field names in the new file

# 		# write the new line in new file
# 		for line in csv_reader:
# 			csv_writer.writerow(line)