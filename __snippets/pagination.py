from flask import request


def _make_url_query(args):
    """
    Helper function to return a query url string from a dict
    """
    return '?' + '&'.join('%s=%s' % (key, args[key]) for key in args)

def get_paginated_list(results, url=None, args={}):
    """
    Returns a paginated response object

    results - list of results to paginate
    url - url of the request
    args - args passed to the request as query parameters
    """
    # auto-get url
    if url is None:
        url = request.base_url
    # get page bounds
    start = args.get('start', 1)
    limit = args.get('limit', 20)
    # check if page exists
    count = len(results)
    if count < start and ((count > 0) or (count == 0 and start > 1)):
        raise NotFoundError(
            message='Start position \'{}\' out of bound'.format(start))
    # make response
    obj = {}
    obj['start'] = start
    obj['limit'] = limit
    obj['count'] = count
    # make URLs
    # make previous url
    args_copy = args.copy()
    if start == 1:
        obj['previous'] = ''
    else:
        args_copy['start'] = max(1, start - limit)
        args_copy['limit'] = start - 1
        obj['previous'] = url + _make_url_query(args_copy)
    # make next url
    args_copy = args.copy()
    if start + limit > count:
        obj['next'] = ''
    else:
        args_copy['start'] = start + limit
        obj['next'] = url + _make_url_query(args_copy)
    # finally extract result according to bounds
    obj['results'] = results[(start - 1):(start - 1 + limit)]
    return obj
