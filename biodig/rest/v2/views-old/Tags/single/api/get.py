import base.util.ErrorConstants as Errors
from base.models import Tag
from django.core.exceptions import ObjectDoesNotExist
from renderEngine.WebServiceObject import WebServiceObject

class GetAPI:
    
    def __init__(self, user=None, fields=None):
        self.user = user
        self.fields = fields
    
    '''
        Gets all the tags in the database that are private
    '''
    def getTag(self, tagKey, isKey=True):
        metadata = WebServiceObject()
        
        try:            
            if (isKey):
                tag = Tag.objects.get(pk__exact=tagKey)
            else:
                tag = tagKey
        except (ObjectDoesNotExist, ValueError):
            raise Errors.INVALID_TAG_GROUP_KEY
        except Exception:
            raise Errors.INTERNAL_ERROR
        
        if not tag.readPermissions(self.user):
            raise Errors.AUTHENTICATION

        metadata.limitFields(self.fields)
                
        metadata.put('name', tag.name)
        metadata.put('color', tag.color)
        metadata.put('group', tag.group)
        metadata.put('dateCreated', tag.dateCreated.strftime("%Y-%m-%d %H:%M:%S"))
        metadata.put('lastModified', tag.lastModified.strftime("%Y-%m-%d %H:%M:%S"))
        metadata.put('user', tag.user)
        metadata.put('isPrivate', tag.isPrivate)
        
        return metadata