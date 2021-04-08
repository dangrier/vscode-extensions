from typing import Any, Callable, Dict, Generic, Optional, Sequence, Type, TypeVar, Union

from django.forms.forms import BaseForm
from django.forms.models import BaseModelForm
from django.views.generic.base import ContextMixin, TemplateResponseMixin, View
from django.views.generic.detail import BaseDetailView, SingleObjectMixin, SingleObjectTemplateResponseMixin
from typing_extensions import Literal

from django.http import HttpRequest, HttpResponse

_FormT = TypeVar("_FormT", bound=BaseForm)

class AbstractFormMixin(ContextMixin):
    initial: Dict[str, Any] = ...
    form_class: Optional[Type[BaseForm]] = ...
    success_url: Optional[Union[str, Callable[..., Any]]] = ...
    prefix: Optional[str] = ...
    def get_initial(self) -> Dict[str, Any]: ...
    def get_prefix(self) -> Optional[str]: ...
    def get_form_kwargs(self) -> Dict[str, Any]: ...
    def get_success_url(self) -> str: ...

class FormMixin(Generic[_FormT], AbstractFormMixin):
    def get_form_class(self) -> Type[_FormT]: ...
    def get_form(self, form_class: Optional[Type[_FormT]] = ...) -> BaseForm: ...
    def form_valid(self, form: _FormT) -> HttpResponse: ...
    def form_invalid(self, form: _FormT) -> HttpResponse: ...

class ModelFormMixin(AbstractFormMixin, SingleObjectMixin):
    fields: Optional[Union[Sequence[str], Literal["__all__"]]] = ...
    def get_form_class(self) -> Type[BaseModelForm]: ...
    def get_form(self, form_class: Optional[Type[BaseModelForm]] = ...) -> BaseModelForm: ...
    def form_valid(self, form: BaseModelForm) -> HttpResponse: ...
    def form_invalid(self, form: BaseModelForm) -> HttpResponse: ...

class ProcessFormView(View):
    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse: ...
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse: ...
    def put(self, *args: str, **kwargs: Any) -> HttpResponse: ...

class BaseFormView(FormMixin[_FormT], ProcessFormView): ...
class FormView(TemplateResponseMixin, BaseFormView[_FormT]): ...
class BaseCreateView(ModelFormMixin, ProcessFormView): ...
class CreateView(SingleObjectTemplateResponseMixin, BaseCreateView): ...
class BaseUpdateView(ModelFormMixin, ProcessFormView): ...
class UpdateView(SingleObjectTemplateResponseMixin, BaseUpdateView): ...

class DeletionMixin:
    success_url: Optional[str] = ...
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse: ...
    def delete(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse: ...
    def get_success_url(self) -> str: ...

class BaseDeleteView(DeletionMixin, BaseDetailView): ...
class DeleteView(SingleObjectTemplateResponseMixin, BaseDeleteView): ...