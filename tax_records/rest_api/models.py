from django.db import models

# Create your models here.

class Record(models.Model):
    street_number = models.IntegerField(default=None, null=True)
    route = models.CharField(default='', max_length=128)
    city = models.CharField(default='', max_length=128)
    county = models.CharField(default='', max_length=128)
    state = models.CharField(default='', max_length=128)

    raw_name = models.CharField(default='', max_length=128)
    first_name = models.CharField(default='', max_length=128)
    last_name = models.CharField(default='', max_length=128)

    link = models.CharField(default='', max_length=128)
    sbl = models.CharField(default='', max_length=128)
    swis = models.CharField(default='', max_length=128)

    @staticmethod
    def get_by_components(data):
        records = Record.objects.all()

        for key in data:
            if key in [f.name for f in Record._meta.get_fields()]:
                records = records.filter(**{key + '__icontains': data[key]})

        return records

    @staticmethod
    def get_single_result(data):
        components = {}
        for field in [f.name for f in Record._meta.get_fields()]:
            if field in data:
                components[field] = data[field]
                records = Record.get_by_components(components)

                if len(records) == 1:
                    return records

        return None
