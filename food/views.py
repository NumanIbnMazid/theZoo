from .forms import FoodForm, AnimalFoodForm
from .models import Food, AnimalFood
from util.view_imports import *


# ------------------- Food -------------------

@method_decorator(login_required, name='dispatch')
class FoodCreateView(CreateView):
    template_name = 'snippets/manage.html'
    form_class = FoodForm

    def form_valid(self, form):
        name = form.instance.name
        field_qs = Food.objects.filter(
            name__iexact=name
        )
        result = validate_normal_form(
            field='name', field_qs=field_qs,
            form=form, request=self.request
        )
        if result == 1:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('food:add_food')

    def get_context_data(self, **kwargs):
        context = super(
            FoodCreateView, self
        ).get_context_data(**kwargs)
        return simple_context_data(
            context=context, model=Food,
            page_title='Create Food',
            update_url='food:update_food',
            delete_url='food:delete_food',
            namespace='food'
        )


@method_decorator(login_required, name='dispatch')
class FoodUpdateView(UpdateView):
    template_name = 'snippets/manage.html'
    form_class = FoodForm

    def get_object(self):
        return get_simple_object(key='id', model=Food, self=self)

    def form_valid(self, form):
        name = form.instance.name
        field_qs = Food.objects.filter(
            name__iexact=name
        ).exclude(id=self.get_object().id)
        result = validate_normal_form(
            field='name', field_qs=field_qs,
            form=form, request=self.request
        )
        if result == 1:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('food:add_food')

    def get_context_data(self, **kwargs):
        context = super(
            FoodUpdateView, self
        ).get_context_data(**kwargs)
        return simple_context_data(
            context=context, model=Food,
            page_title='Update Food',
            update_url='food:update_food',
            delete_url='food:delete_food',
            namespace='food'
        )


@csrf_exempt
def delete_food(request):
    return delete_simple_object(request=request, key='id', model=Food)


# ------------------- AnimalFood -------------------

@method_decorator(login_required, name='dispatch')
class AnimalFoodCreateView(CreateView):
    template_name = 'snippets/manage.html'
    form_class = AnimalFoodForm

    def form_valid(self, form):
        field_qs = None
        result = validate_normal_form(
            field='animal', field_qs=field_qs,
            form=form, request=self.request
        )
        if result == 1:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('food:add_animal_food')

    def get_context_data(self, **kwargs):
        context = super(
            AnimalFoodCreateView, self
        ).get_context_data(**kwargs)
        return simple_context_data(
            context=context, model=AnimalFood,
            page_title='Create Animal Food',
            update_url='food:update_animal_food',
            delete_url='food:delete_animal_food',
            namespace='animal_food'
        )


@method_decorator(login_required, name='dispatch')
class AnimalFoodUpdateView(UpdateView):
    template_name = 'snippets/manage.html'
    form_class = AnimalFoodForm

    def get_object(self):
        return get_simple_object(key='id', model=AnimalFood, self=self)

    def form_valid(self, form):
        field_qs = None
        result = validate_normal_form(
            field='animal', field_qs=field_qs,
            form=form, request=self.request
        )
        if result == 1:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('food:add_animal_food')

    def get_context_data(self, **kwargs):
        context = super(
            AnimalFoodUpdateView, self
        ).get_context_data(**kwargs)
        return simple_context_data(
            context=context, model=AnimalFood,
            page_title='Update Animal Food',
            update_url='food:update_animal_food',
            delete_url='food:delete_animal_food',
            namespace='animal_food'
        )


@csrf_exempt
def delete_animal_food(request):
    return delete_simple_object(request=request, key='id', model=AnimalFood)

