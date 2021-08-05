from os.path import basename

from django.shortcuts import render
from django.http import HttpResponse
from .models import File
from .forms import UploadFileForm
from django.http import HttpResponseRedirect


# Create your views here.

def index(response):
    return render(response, "main/base.html", {"name": "testare"})


def home(response):
    return render(response, "main/home.html", {"name": "testare"})


def my_files(response):
    user = response.user
    user_id = user.id
    user_files = File.objects.all().filter(file_user_id=user_id)
    for file in user_files:
        print(str(file))
    return render(response, "main/files.html", {"files": user_files})


def handle_uploaded_file(f, file_user_id):
    file_name = basename(f.name).split(".")[0]
    file_extension = basename(f.name).split(".")[1]
    file_type = ""
    if file_extension == "txt":
        file_type = "input"
    if file_extension == "py":
        file_type = "script"

    new_file = File.create(file_user_id, file_name, file_extension, file_type)
    new_file.save()

    prefix = "C:\\Users\\stars\\Desktop\\GAD_PROJECT\\PythonServerlessApplication\\"
    if file_extension == "txt":
        with open(prefix + str(file_user_id) + "\\Inputs\\" + str(file_name) + "." + str(file_extension), 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

    if file_extension == "py":
        with open(prefix + str(file_user_id) + "\\Scripts\\" + str(file_name) + "." + str(file_extension), 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)


def upload_file(request):
    user_id = request.user.id
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'], user_id)
            return HttpResponseRedirect('/files')
    else:
        form = UploadFileForm()
    return render(request, 'main/upload.html', {'form': form})
