import re
from django import forms
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse


def validate_normal_form(field, field_data, field_qs, model, form, request, view_type='create', predata=None):
    if view_type == 'update':
        if not predata == field_data:
            if field_qs.exists():
                form.add_error(
                    f'field', forms.ValidationError(
                        f"This {field} is already exists! Please try another one."
                    )
                )
                return 0
            else:
                messages.add_message(
                    request, messages.SUCCESS,
                    "Updated successfully!"
                )
            return 1
        else:
            messages.add_message(
                request, messages.SUCCESS,
                "Updated successfully!"
            )
    else:
        if field_qs.exists():
            form.add_error(
                field, forms.ValidationError(
                    f"This {field} is already exists! Please try another one."
                )
            )
            return 0
        else:
            messages.add_message(
                request, messages.SUCCESS,
                "Created successfully!"
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
