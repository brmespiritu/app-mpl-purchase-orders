import csv
from django.utils.encoding import smart_str
from django.http import HttpResponse, StreamingHttpResponse
import datetime

class Echo:
    """An object that implements just the write method of the file-like
    interface.
    """
    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value

def convert_value(val):
    if val:
        return smart_str(val)
    return ''

def stream_content(modeladmin, request, queryset):
    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer, delimiter=',')
    opts = modeladmin.model._meta
    field_names = [field.name for field in opts.fields if field.name != 'id']
    yield writer.writerow(field_names)
    for obj in queryset:
        row = [convert_value(getattr(obj, field)()) if callable(getattr(obj, field)) else convert_value(getattr(obj, field)) for field in field_names]
        yield writer.writerow(row)


## Export to CSV
def export_csv(modeladmin, request, queryset):
    filename = str(modeladmin).split('.')[1].replace('Admin', 's')
    filename += '_'+datetime.datetime.now().strftime('%Y-%b-%d')+'.csv'
    response = StreamingHttpResponse(stream_content(modeladmin, request, queryset),
                                     content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename='+filename
    return response
export_csv.short_description = u"Export CSV"
