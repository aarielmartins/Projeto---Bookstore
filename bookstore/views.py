from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import subprocess
import git

@csrf_exempt
def update(request):
    if request.method == "POST":
        try:
            repo = git.Repo('/home/aarielmartins/Projeto---Bookstore')
            origin = repo.remotes.origin
            origin.fetch()
            origin.pull()
            subprocess.run(['touch', '/var/www/aarielmartins_pythonanywhere_com_wsgi.py'])
            return HttpResponse("Updated code on PythonAnywhere successfully!")
        except git.exc.InvalidGitRepositoryError:
            return HttpResponse("Invalid Git repository", status=500)
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}", status=500)
    else:
        return HttpResponse("Method not allowed", status=405)