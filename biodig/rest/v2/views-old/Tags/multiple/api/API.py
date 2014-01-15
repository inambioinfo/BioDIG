import base.util.ErrorConstants as Errors
import base.util.Util as Util
from get import GetAPI
from post import PostAPI

'''
    Gets the information for a tag given its key
    
    @param request: Django Request object to be used to parse the query
'''
def getTags(request):
    # read in optional parameters and initialize the API
    offset = Util.getInt(request.GET, 'offset', 0)
    limit = Util.getInt(request.GET, 'limit', 10)

    unlimited = request.GET.get('unlimited', False)
    fields = Util.getDelimitedList(request.GET, 'fields')
    
    getAPI = GetAPI(limit, offset, request.user, fields, unlimited)
    
    # read in parameters for limiting search
    lastModified = request.GET.get('lastModified', None)
    dateCreated = request.GET.get('dateCreated', None)
    isPrivate = request.GET.get('isPrivate', None)
    user = Util.getDelimitedList(request.GET, 'user')
    group = Util.getDelimitedList(request.GET, 'group')
    color = Util.getDelimitedList(request.GET, 'color')
    name = Util.getDelimitedList(request.GET, 'name')
    
    return getAPI.getTags(name, color, group, dateCreated, lastModified, user, isPrivate)
        

'''
    Creates a new tag and returns the newly created tag information
    
    @param request: Django Request object to be used to parse the query
'''
def createTag(request):
    imageKey = request.POST.get('imageId', None)
    if not imageKey:
        raise Errors.MISSING_PARAMETER.setCustom('imageId')
        
    # get the name
    name = request.POST.get('name', None)
    if not name:
        raise Errors.MISSING_PARAMETER.setCustom('name')  
    
    # get optional parameter
    fields = Util.getDelimitedList(request.POST, 'fields')
    
    postAPI = PostAPI(request.user, fields)
    return postAPI.createTagGroup(imageKey, name)
    
    
    