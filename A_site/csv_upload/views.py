from django.shortcuts import render
####
def index(request):
    return render(request, 'csv_upload/csv_upload.html')
