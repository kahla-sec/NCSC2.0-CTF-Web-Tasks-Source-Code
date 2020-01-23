from django.shortcuts import render
from .forms import TesterForm
import subprocess

def curl(link):
    proc = subprocess.Popen(['curl', link, '--max-time', '3'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    return {'stdout':stdout,'stderr':stderr}

def testerHome(request):
        blacklist = ['file', '127.0.0.1', 'localhost', 'uwsgi_file','config','dir','flushall']
        try:
            if request.method == 'POST':
                form = TesterForm(request.POST)
                if form.is_valid():
                    for word in blacklist:
                        message = ""
                        if word == form.cleaned_data['Input']:
                            message = "Please Don't Try to hack me little script kiddie"
                            form = TesterForm()
                            return render(request, 'tester.html', {'message': message,'form':form.as_p()})
                    try:
                        link = form.cleaned_data['Input']
                        res = curl(link)
                        message = "This is the result after fetching the url"
                        return render(request, 'tester.html', {'message': message, 'result': res['stdout'].decode(), 'form': form.as_p()})
                    except Exception:
                        message = "An error has occured check your syntax "
                        form = TesterForm()
                        return render(request, "tester.html", {'message': message, 'result':result,'form':form.as_p()})
            else:
                message = ""
                form = TesterForm()
                return render(request, 'tester.html', {'message': message, 'form': form.as_p()})
        except Exception:
            message = "An error has occured check your syntax"
            form = TesterForm()
            return render(request, "tester.html", {'message': message, 'form': form.as_p()})

