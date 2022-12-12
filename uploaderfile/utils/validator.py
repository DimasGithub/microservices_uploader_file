from django.utils.translation import ugettext_lazy as _

def check_required_fields(required_fields, exist_fields):
    """
    :param `required_fields` is list of fields to require.
    :param `exist_fields` is list of current fields.

    :return dict of `error_fields`, eg:
    {
        "market": [
            "This field is required."
        ],
        "finance": [
            "Incorrect type. Expected finance value, received str."
        ]
    }

    :usage example:
        required_fields = [{'field': 'plan', 'type': int},
                           {'field': 'finance', 'type': int},
                           {'field': 'conclusion', 'type': int}]
        error_fields = check_required_fields(required_fields, request.data)
        if len(error_fields) > 0:
            response = {'status': status.HTTP_400_BAD_REQUEST}
            response.update(**error_fields)
            return Response(response, status=response.get('status'))
    """
    error_fields_dict = {}

    for field_data in required_fields:
        if isinstance(field_data, dict):
            field_name = field_data.get('field')
            field_type = field_data.get('type')
            field_request = exist_fields.get(field_name)
            error_fields_list = []

            if (field_name not in exist_fields) or (field_request is None) or (field_request == ''):
                error_fields_list.append(_('This field is required.'))
            # jika float diijinkan juga client mengirimkan int
            elif not (isinstance(field_request, field_type) or (field_type is float and isinstance(field_request, int))):
                error_fields_list.append(_('Incorrect type. Expected %(type1)s value, received %(type2)s.')
                                         % {'type1': field_type.__name__, 'type2': type(field_request).__name__})

            if len(error_fields_list) > 0:
                error_fields_dict.update({field_name: error_fields_list})

    return error_fields_dict