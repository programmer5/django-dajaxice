from django.http import QueryDict


def deserialize_form(data):
    """
    Create a new QueryDict from a serialized form.
    """
    try:
    	return QueryDict(query_string=unicode(data).encode('utf-8'))
    except Exception as e:
    	return QueryDict(query_string=data.encode('utf-8'))
    
