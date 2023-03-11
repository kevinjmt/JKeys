from msilib.schema import ListView
from django.views import generic
from JKeys.models import Login, IdCard, CreditCard
from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import LoginForm, IDCardForm, CreditCardForm

# View for the Website Home Page
class WebSite(generic.ListView):
    # HTML link to file
    template_name = "jkeys/home.html"
    # objectname in the HTML file in home page
    context_object_name = "websitelist"

    # Function to get all objects in the database and
    # show them thanks to the forloop
    def get_queryset(self):
        result = []
        for ids in Login.objects.filter(user_id_id=self.request.user.id).order_by('modified').reverse()[:3]:
            result.append((ids, 'id'))
        for idcard in IdCard.objects.filter(user_id_id=self.request.user.id).order_by('modified').reverse()[:3]:
            result.append((idcard, 'idcard'))
        for creditcard in CreditCard.objects.filter(user_id_id=self.request.user.id).order_by('modified').reverse()[:3]:
            result.append((creditcard, 'creditcard'))
        return result



########## LOGINS ##########

# View for the Website Home Page
class LoginHome(generic.ListView):
    # HTML link to file
    template_name = "jkeys/login/home.html"
    # objectname in the HTML file in home page
    context_object_name = "loginlist"

    # Function to get all objects in the database and
    # show them thanks to the forloop
    def get_queryset(self):
        return Login.objects.all().order_by('name').filter(user_id_id=self.request.user.id)

# View for the Detail Page of an Element
class LoginPage(generic.DetailView):
    # HTML link to file
    template_name = "jkeys/login/login.html"
    # Takes Id Model
    model = Login


# View for the Create Page of an Element
class CreateLogin(generic.FormView):
    # HTML link to file
    template_name = "jkeys/login/createlogin.html"
    # Fields ready to be filled in the CreateView
    # fields = ["name", "card_number"]
    # Takes Id Model
    form_class = LoginForm
    # On success (of creating an object), go to Home Page
    success_url = "/logins"

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('loginhome'))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login = form.CreateLogin(self.request.user)
        return HttpResponseRedirect(reverse('loginhome'))



# View for the Edit Page of an Element
class EditLogin(generic.FormView):
    # HTML link to file
    template_name = "jkeys/login/editlogin.html"
    # Fields ready to be filled in the CreateView
    # fields = ["name", "card_number"]
    # Takes Id Model
    form_class = LoginForm
    # On success (of creating an object), go to Home Page
    success_url = "/logins"

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('idcardhome'))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login = form.EditLogin(Login.objects.get(pk=self.kwargs['pk']))
        return HttpResponseRedirect(reverse('loginhome'))


    def get_context_data(self, **kwargs):
        id = Login.objects.get(pk=self.kwargs['pk'])
        return {
            'object':id
        }



# View for the Delete Page of an Element
class DeleteLogin(generic.DeleteView):
    # HTML link to file
    template_name = "jkeys/login/deletelogin.html"
    # On success (of deleting), go to Home Page
    success_url = "/logins"
    # Takes Id Model
    model = Login


########## IDCARDS ##########

# View for the Website Home Page
class IDCardHomePage(generic.ListView):
    # HTML link to file
    template_name = "jkeys/idcard/home.html"
    # objectname in the HTML file in home page
    context_object_name = "idcardlist"

    # Function to get all objects in the database and
    # show them thanks to the forloop
    def get_queryset(self):
        return IdCard.objects.all().order_by('name').filter(user_id_id=self.request.user.id)

# View for the Detail Page of an Element
class IDCardPage(generic.DetailView):
    # HTML link to file
    template_name = "jkeys/idcard/idcard.html"
    # Takes Id Model
    model = IdCard


# View for the Create Page of an Element
class CreateIDCard(generic.FormView):
    # HTML link to file
    template_name = "jkeys/idcard/createidcard.html"
    # Fields ready to be filled in the CreateView
    # fields = ["name", "card_number"]
    # Takes Id Model
    form_class = IDCardForm
    # On success (of creating an object), go to Home Page
    success_url = "/idcards"

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('idcardhome'))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        credit_card = form.CreateIdCard(self.request.user)
        return HttpResponseRedirect(reverse('idcardhome'))


# View for the Edit Page of an Element
class EditIDCard(generic.FormView):
    # HTML link to file
    template_name = "jkeys/idcard/editidcard.html"
    # Fields ready to be filled in the CreateView
    # fields = ["name", "card_number"]
    # Takes Id Model
    form_class = IDCardForm
    # On success (of creating an object), go to Home Page
    success_url = "/idcards"

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('idcardhome'))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        credit_card = form.EditIdCard(IdCard.objects.get(pk=self.kwargs['pk']))
        return HttpResponseRedirect(reverse('idcardhome'))


    def get_context_data(self, **kwargs):
        id = IdCard.objects.get(pk=self.kwargs['pk'])
        return {
            'object':id
        }


# View for the Delete Page of an Element
class DeleteIDCard(generic.DeleteView):
    # HTML link to file
    template_name = "jkeys/idcard/deleteidcard.html"
    # On success (of deleting), go to Home Page
    success_url = "/idcards"
    # Takes Id Model
    model = IdCard



########## CREDIT CARDS ##########

# View for the Website Home Page
class CreditCardHome(generic.ListView):
    # HTML link to file
    template_name = "jkeys/creditcard/home.html"
    # objectname in the HTML file in home page
    context_object_name = "creditcards"

    # Function to get all objects in the database and
    # show them thanks to the forloop
    def get_queryset(self):
        return CreditCard.objects.all().order_by('name').filter(user_id_id=self.request.user.id)

# View for the Detail Page of an Element
class CreditCardPage(generic.DetailView):
    # HTML link to file
    template_name = "jkeys/creditcard/creditcard.html"
    # Takes Id Model
    model = CreditCard


# View for the Create Page of an Element
class CreateCreditCard(generic.FormView):
    # HTML link to file
    template_name = "jkeys/creditcard/createcreditcard.html"
    # Fields ready to be filled in the CreateView
    # fields = ["name", "card_number"]
    # Takes Id Model
    form_class = CreditCardForm
    # On success (of creating an object), go to Home Page
    success_url = "/creditcards"

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('creditcardhome'))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        credit_card = form.CreateCreditCard(self.request.user)
        return HttpResponseRedirect(reverse('creditcardhome'))

    # Save element when 'Save' Button clicked
    """def save_element(request):
        # Each field saved in a new Id if POSTed
        # (if the user created a new Id)
        if request.method == "POST":
            name = request.POST.get('name')
            card_number = request.POST.get('card_number')
            user_id = request.request.user.id

            # Create object directly from the texts field
            # stored in the variables as on top
            CreditCard.objects.create(name=name, card_number=card_number)
        # Return the render of the Home Page when finished saving
        return render(request, 'jkeys/creditcard/home.html')"""


# View for the Edit Page of an Element
class EditCreditCard(generic.FormView):
    # HTML link to file
    template_name = "jkeys/creditcard/editcreditcard.html"
    # Fields ready to be filled in the CreateView
    # fields = ["name", "card_number"]
    # Takes Id Model
    form_class = CreditCardForm
    # On success (of creating an object), go to Home Page
    success_url = "/creditcards"

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('creditcardhome'))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        credit_card = form.EditCreditCard(CreditCard.objects.get(pk=self.kwargs['pk']))
        return HttpResponseRedirect(reverse('creditcardhome'))

    def get_context_data(self, **kwargs):
        id = CreditCard.objects.get(pk=self.kwargs['pk'])
        return {
            'object':id
        }

    """def get_queryset(self):
        return CreditCard.objects.get(self.kwargs["pk"])"""


    # Save element when 'Save' Button clicked
    """def save_element(request):
        # Each field saved in a new Id if POSTed
        # (if the user created a new Id)
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            link = request.POST.get('link')

            # Create object directly from the texts field
            # stored in the variables as on top
            Login.objects.create(name=name, email=email, password=password, link=link)

        # Return the render of the Home Page when finished saving
        return render(request, 'jkeys/login/login.html')"""


# View for the Delete Page of an Element
class DeleteCreditCard(generic.DeleteView):
    # HTML link to file
    template_name = "jkeys/login/deletelogin.html"
    # On success (of deleting), go to Home Page
    success_url = "/"
    # Takes Id Model
    model = CreditCard