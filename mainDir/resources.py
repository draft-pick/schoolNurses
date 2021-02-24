from import_export import resources
from .models import *


class StudentsReource(resources.ModelResource):
    class meta:
        model = Students
        widgets = {
            'keySchool': {'school_id': 1},
        }
