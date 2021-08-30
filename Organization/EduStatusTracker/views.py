from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .DatabaseConfig.dbconfig import getconnection
# Create your views here.

def showloginpage(request):
    return render(request, "login/login.html" )


@csrf_exempt
def forgotpassword(request):
    registrationid = request.POST.get('registrationid')
    boardtype = request.POST.get('boardtype')
    if len(registrationid) > 0 and len(boardtype) > 0:
        if False:
            return displaysecurityquestion();
        else:
            return displayinvalidcredential();

    else:
        print("error")
        return displayrequiredfield();


    return JsonResponse(responseData)

@csrf_exempt
def verifyRegistrationId(request):
    registrationid=request.POST.get('registrationid').strip()
    boardtype=request.POST.get('boardtype').strip()
    if len(registrationid)>0 and len(boardtype)>0:
          print("coming")
          #here check with db credentials!
          if True:

              return displaysecurityquestion();
          else:
              return displayinvalidcredential();


    else:
        print("error")
        return displayrequiredfield()

    return JsonResponse(responseData,safe=False)










#displaying proper model based on error! -------------------------------- Starts.....----------------
def displayrequiredfield():
 responseData = {
    'header': 'WARNING ! Field is required',
    'body': '<div id="cross"></div>',
    'modalcode': 'feildrequired'
}

 return JsonResponse(responseData)

def displayinvalidcredential():
    responseData = {
        'header': ' Invalid Access ! Not Allowed !',
        'body': '<div id="cross"></div>',
        'modalcode':'invalid'
    }

    return JsonResponse(responseData)

def displaysecurityquestion():
    responseData = {
        'header': 'Please ANSWER the Security- Questions!',
        'body': '<div class="form-group form-input"> <input type="text" name="question1" id="question1" placeholder="" value="" required /><label for="question1" class="form-label">question1</label></div>',
        'modalcode':'securityque'
    }

    return JsonResponse(responseData)

def displaywrongsecurityquestion():
    responseData = {
        'header': 'Wrong ANSWERS!',
        'body': '<div id="cross"></div>',
        'modalcode':'wronganswer'
    }
    return JsonResponse(responseData)

def displaysomethingwentwrong():
    responseData = {
        'header': 'OOPS ! Something went wrong !',
        'body': '<div id="cross"></div>',
        'modalcode':'somethingwrong'
    }
    return JsonResponse(responseData)


#-------ENDS.....-------------------------------------------------