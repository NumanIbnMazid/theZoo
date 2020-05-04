import re
from django import forms
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
import datetime


def validate_normal_form(field=None, field_qs=None, form=None, request=None, validation_message=None, success_message=None):
    if not field_qs == None:
        if field_qs.exists():
            if validation_message == None:
                validation_message = f"This {field} is already exists! Please try another one."
            form.add_error(
                field, forms.ValidationError(
                    validation_message
                )
            )
            return 0
    if success_message == None:
        if 'update' in request.path or 'edit' in request.path:
            success_message = "Data Updated Successfully !!!"
        elif 'create' in request.path or 'add' in request.path:
            success_message = "Data Created Successfully !!!"
        else:
            success_message = "Data Manipulated Successfully !!!"
    messages.add_message(
        request, messages.SUCCESS,
        success_message
    )
    return 1


def get_simple_object(key='slug', model=None, self=None):
    try:
        if key == 'id':
            id = self.kwargs['id']
            instance = model.objects.get(id=id)
        else:
            slug = self.kwargs['slug']
            instance = model.objects.get(slug=slug)
    except model.DoesNotExist:
        raise Http404('Not found!!!')
    except model.MultipleObjectsReturned:
        if key == 'id':
            id = self.kwargs['id']
            instance = model.objects.filter(id=id).first()
        else:
            slug = self.kwargs['slug']
            instance = model.objects.filter(slug=slug).first()
    except:
        raise Http404("Something went wrong !!!")
    return instance


def delete_simple_object(request, key, model):
    url = reverse('home')
    # user = request.user
    if request.method == "POST":
        if key == 'id':
            id = request.POST.get("id")
            qs = model.objects.filter(id=id)
        else:
            slug = request.POST.get("slug")
            qs = model.objects.filter(slug=slug)
        if qs.exists():
            # if qs.first().user == user.profile:
            qs.delete()
            messages.add_message(request, messages.SUCCESS,
                                 "Deleted successfully!")
            url = request.META.get('HTTP_REFERER', '/')
        else:
            messages.add_message(request, messages.WARNING,
                                 "Not found!")
    return HttpResponseRedirect(url)


def simple_context_data(context, model, page_title=None, update_url=None, delete_url=None, namespace=None):
    context['page_title'] = page_title
    context['list_objects'] = model.objects.all()
    context['fields_count'] = len(model._meta.get_fields())
    context['fields'] = dict([(f.name, f.verbose_name)
                              for f in model._meta.fields + model._meta.many_to_many])
    context['update_url'] = update_url
    context['delete_url'] = delete_url
    context['namespace'] = namespace
    return context


def validate_chars(field_data, allowed_chars=None, max_length=50):
    if not field_data == None:
        pattern = allowed_chars
        characters_to_remove = '^[]+$'
        for character in characters_to_remove:
            pattern = pattern.replace(character, "")
        if not allowed_chars == None:
            allowed_chars = re.match(allowed_chars, field_data)
            if not allowed_chars:
                raise forms.ValidationError(
                    f"Only [{pattern}] these characters are allowed!"
                )
        length = len(field_data)
        if length > max_length:
            raise forms.ValidationError(
                f"Maximum {max_length} characters allowed. Currently using {length}!"
            )
    return field_data


def simple_form_widget(self=None, field=None, maxlength=50, step=None, pattern=None, placeholder=None):
    field_name = ' '.join(field.split('_')).title()
    allowed_chars = pattern
    print(pattern)
    if not pattern == None:
        characters_to_remove = '^[]{1,}$'
        for character in characters_to_remove:
            allowed_chars = allowed_chars.replace(character, "")
    if not placeholder == None:
        placeholder = placeholder
    else:
        placeholder = f'Enter {field_name}...'
    self.fields[field].widget.attrs.update({
        'id': f'{field}_id',
        'placeholder': placeholder,
        'maxlength': maxlength,
        'step': step,
        'pattern': pattern
    })
    if not pattern == None:
        self.fields[field].help_text = f"Only [{allowed_chars}] these characters are allowed."


# Dynamic Field Model

# def get_fields(self):
#     def get_dynamic_fields(field):
#         if field.name == 'x':
#             return (field.name, self.x.title)
#         else:
#             value = "-"
#             if not field.value_from_object(self) == None and not field.value_from_object(self) == "":
#                 value = field.value_from_object(self)
#             return (field.name, value)
#     return [get_dynamic_fields(field) for field in self.__class__._meta.fields]


def get_dynamic_fields(field=None, self=None):
    if field.name == 'x':
        return (field.name, self.x.title)
    else:
        value = "-"
        if not field.value_from_object(self) == None and not field.value_from_object(self) == "":
            value = field.value_from_object(self)
        return (field.name, value)


# ----- Many to Many Field and Others -----
# def get_fields(self):
#     def get_dynamic_fields(field):
#         if field.name == 'equipments':
#             if field.get_internal_type() == 'ManyToManyField':
#                 value = ','.join([str(elem)
#                                     for elem in self.equipments.all()])
#             else:
#                 value = self.equipments.name
#             return (field.name, value)
#         elif field.name == 'x':
#             return (field.name, self.x.title)
#         else:
#             value = "-"
#             if not field.value_from_object(self) == None and not field.value_from_object(self) == "":
#                 value = field.value_from_object(self)
#             return (field.name, value)
#     return [get_dynamic_fields(field) for field in (self.__class__._meta.fields + self.__class__._meta.many_to_many)]


# --- Lookup in Many to Many ---
# def get_fields(self):
#     opts = EquipmentSet._meta
#     for f in sorted(opts.fields + opts.many_to_many):
#         print(f'{f.name}: {f}')
#     pass


def get_report(context=None, context_name=None, model=None, query=None, date_from_filtered=None, date_to_filtered=None):
    if not date_from_filtered == "" and date_to_filtered == "":
        date_to_filtered = datetime.datetime.now()
    if date_from_filtered == "":
        date_from_filtered = None
    if date_to_filtered == "":
        date_to_filtered = None

    if not query == None and not date_from_filtered == None:
        context['selected_object_list'] = model.objects.search(
            query).filter(created_at__range=(date_from_filtered, date_to_filtered)
                          )
    elif not query == None and date_from_filtered == None:
        context['selected_object_list'] = model.objects.search(query)
    elif query == None and not date_from_filtered == None:
        context['selected_object_list'] = model.objects.filter(created_at__range=(date_from_filtered, date_to_filtered)
                                                     )
    else:
        context['selected_object_list'] = model.objects.all()
    return context
