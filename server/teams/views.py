from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Team, User
from .forms import CreateTeamForm, JoinTeamForm

# Create your views here.

# Main Team Page
def team(request):
    user_id = 7

    user_info = User.objects.get(pk=user_id)

    if user_info.team_id is not None:
        team_info = Team.objects.get(pk=user_info.team_id.team_id)
        team_members = User.objects.filter(team_id = user_info.team_id.team_id)
    else:
        team_info = ''
        team_members = ''


    return render(request, "team.html", {
        'user_info': user_info,
        'team_info': team_info,
        'team_members': team_members
    }) 

# Create new team
def create_team(request):
    user_id = 7
    user_info_obj = User.objects.get(pk=user_id)
    # Only admin user who doesn't have a team created can access this page
    if user_info_obj.is_admin and user_info_obj.team_id is None:

        if request.method == "POST":
                form = CreateTeamForm(request.POST)
                if form.is_valid():
                    # Save the new team in Team table 
                    new_team = Team(name=request.POST['name']) 
                    new_team.save()
                    # Assign team_id to the created user
                    user_info_obj = User.objects.get(pk=user_id)
                    team_obj= Team.objects.get(name = request.POST['name'])
                    user_info_obj.team_id = team_obj
                    user_info_obj.save()
                    return HttpResponseRedirect(reverse("teams:team"))
                else:
                    err = 'Error creating new team'
                    return render(request, "create_team.html", {'form': form, 'err': err})
        
        return render(request, "create_team.html", {'form': CreateTeamForm()})
    
    else:
        return HttpResponseRedirect(reverse("teams:team"))


# Join a team
def join_team(request):
    user_id = 7
    user_info_obj = User.objects.get(pk=user_id)
    # Only non-admin who doesn't have a team joined can access this page
    if not user_info_obj.is_admin and user_info_obj.team_id is None:

        if request.method == "POST":
            form = JoinTeamForm(request.POST)
            if form.is_valid():
                # Get the team_id of the join_code &&& Save the team_id into joined user 
                try:
                    team_obj= Team.objects.get(join_code = request.POST['join_code'])
                    user_info_obj = User.objects.get(pk=user_id)
                    user_info_obj.team_id = team_obj
                    user_info_obj.save()
                except:
                    err = 'Invalid Join Code'
                    return render(request, "join_team.html", {'form': form, 'err': err})
                return HttpResponseRedirect(reverse("teams:team"))
            else:
                err = 'Error joining a team'
                return render(request, "join_team.html", {'form': form, 'err': err})

        return render(request, "join_team.html", {'form': JoinTeamForm()})
    
    else:
        return HttpResponseRedirect(reverse("teams:team"))

# Edit a team
def edit_team(request, team_id):
    user_id = 7
    user_info_obj = User.objects.get(pk=user_id)

    # Only an admin who has created the team with this particular team_id can edit the team
    try: # For cases where user has team_id None
        if user_info_obj.is_admin and user_info_obj.team_id.team_id == team_id:

            team_to_edit = get_object_or_404(Team, team_id=team_id)

            if request.method == "GET":
                context = {'form': CreateTeamForm(request.POST or None, instance=team_to_edit), 'form_type_edit':'edit', 'team_id': team_id}
                return render(request, "create_team.html", context) 

            elif request.method == "POST":
                form = CreateTeamForm(request.POST, instance=team_to_edit) 
                if form.is_valid():
                    # form.save()
                    ##!! Assumption: Edit a team, old hash
                    # Change the team name 
                    team_obj= Team.objects.get(team_id = team_id)
                    team_obj.name = request.POST['name']
                    team_obj.save()

                    return HttpResponseRedirect(reverse("teams:team"))
                else:
                    err = 'Error editing the team'
                    return render(request, "create_team.html", {'form': form, 'err': err})
            
                
        else:
            return HttpResponseRedirect(reverse("teams:team"))
    
    except AttributeError:
        return HttpResponseRedirect(reverse("teams:team"))



# Delete a team
def delete_team(request, team_id):
    user_id = 7
    user_info_obj = User.objects.get(pk=user_id)
    # Only an admin who has created the team with this particular team_id can delete the team
    if user_info_obj.is_admin and user_info_obj.team_id.team_id == team_id:

        team_to_del = Team.objects.get(pk=team_id)
        if team_to_del:
            # Delete the team from the Team model (all the team_id of the users joined in this team will be set to Null from the model definition)
            team_to_del.delete()
            message = 'Team successfully deleted'
            return HttpResponseRedirect(reverse("teams:team"))
            # return render(request, "team.html", {'message': message})
        else:
            err = 'Error deleting the team'
            return HttpResponseRedirect(reverse("teams:team"))
            # return render(request, "team.html", {'err': err})
    
    else:
        return HttpResponseRedirect(reverse("teams:team"))

# Leave a team
def leave_team(request, team_id):
    user_id = 7
    user_info_obj = User.objects.get(pk=user_id)
    # Only a non-admin who has joined the team with this particular team_id can leave the team
    if not user_info_obj.is_admin and user_info_obj.team_id.team_id == team_id:
        user_info_obj.team_id = None
        user_info_obj.save()
        return HttpResponseRedirect(reverse("teams:team"))

    else:
        return HttpResponseRedirect(reverse("teams:team"))



