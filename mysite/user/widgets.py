from django.forms import DateInput
class DatePicker(DateInput):

    input_type = "date"
    
    def format_value(self, value):
        return value.isoformat() if value is not None and hasattr(value, "isoformat") else ""