from biodig.base.exceptions import BadRequestException
from rest_framework.views import APIView
from rest_framework.response import Response

from biodig.rest.v2.Tags.forms import MultiGetForm, PostForm, PutForm, DeleteForm, SingleGetForm

class TagList(APIView):
    '''
       Class for rendering the view for creating TagGroups and
       searching through the TagGroups.
    '''

    def get(self, request):
        '''
            Method for getting multiple TagGroups either through search
            or general listing.
        '''
        form = MultiGetForm(request.QUERY_PARAMS)
        
        if not form.is_valid():
            raise BadRequestException()

        return Response(form.submit(request))

    def post(self, request):
        '''
            Method for creating a new TagGroup.
        '''
        params = { key : val for key, val in request.DATA }
        params.update(request.QUERY_PARAMS)
        form = PostForm(params)

        if not form.is_valid():
            raise BadRequestException()

        return Response(form.submit(request))


class TagSingle(APIView):
    '''
       Class for rendering the view for getting a TagGroup, deleting a TagGroup
       and updating a TagGroup. 
    '''

    def get(self, request, tag_group_id):
        '''
            Method for getting multiple TagGroups either thorugh search
            or general listing.
        '''
        params = { key : val for key, val in request.QUERY_PARAMS }
        params['tag_group_id'] = tag_group_id
        form = SingleGetForm(params)
        
        if not form.is_valid():
            raise BadRequestException()

        return Response(form.submit(request))

    def put(self, request, tag_group_id):
        '''
            Method for updating a TagGroup's information.
        '''
        params = { key : val for key, val in request.QUERY_PARAMS }
        params.update(request.DATA)
        params['tag_group_id'] = tag_group_id
        form = PutForm(params)
        
        if not form.is_valid():
            raise BadRequestException()

        return Response(form.submit(request))

    def delete(self, request, tag_group_id):
        '''
            Method for deleting a a TagGroup.
        '''
        params = { key : val for key, val in request.QUERY_PARAMS }
        params['tag_group_id'] = tag_group_id
        form = DeleteForm(params)
        
        if not form.is_valid():
            raise BadRequestException()

        return Response(form.submit(request))
