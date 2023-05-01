from django.forms import inlineformset_factory, ChoiceField, ModelForm
from .models import Order, Item


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ('id', 'product', 'quantity', 'unit_price', 'subtotal')
        widgets = {'quantity': ChoiceField(choices=[(i, str(i)) for i in range(1, 6)]).widget}


OrderItemFormSet = inlineformset_factory(
    Order,
    Item,
    form=ItemForm,
    extra=10,
    can_delete=True,
)