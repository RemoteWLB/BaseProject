from django.shortcuts import render
from twitter.models import MappTree, Twitter
from core.main import get_post_detail
from twitter.serializers import MappTreeSerializer, TwitterSerializer
from utils.apiview import SelfBaseAPIView, SelfListAPIView
from utils.response import SuccessResponse

# Create your views here.

class MappTreeView(SelfBaseAPIView, SelfListAPIView):
    serializer_class = MappTreeSerializer
    
    def get(self, request):
        user_id = 0
        node_id = request.data.get("node_id")
        if not node_id:
            node, created = MappTree.objects.get_or_create(user_id=user_id, is_root=True, defaults={
                "node_type": 1,
                "node_name": "/",
                "path_name": "/",
            })
            node_id = node.uuid
        else:
            node = MappTree.objects.get(uuid=node_id)
        queryset = MappTree.objects.filter(parent_id=node_id).order_by("-id")
        page = self.paginate_queryset(queryset)
        node_serializer = self.serializer_class(node, many=False)
        list_serializer = self.serializer_class(page, many=True)
        return SuccessResponse(1, 'success', {
            'list': list_serializer.data,
            'node': node_serializer.data,
            'total': self.total(),
        }, 0)
    
    def post(self, request):
        user_id = 0
        parent_id = request.data.get("parent_id")
        node_name = request.data.get("node_name") + "/"
        if parent_id:
            parent = MappTree.objects.get(uuid=parent_id)
            path_name = parent.path_name + node_name
            is_root = False
        else:
            path_name = "/"
            is_root = True
            
        node, _ = MappTree.objects.get_or_create(user_id=user_id, parent_id=parent_id, node_name=node_name, 
            **{
                "node_type": 1,
                "path_name": path_name,
                "is_root": is_root
            })
        node_serializer = self.serializer_class(node)
        return SuccessResponse(1, 'success', {"node": node_serializer.data}, 0)
    
class TwitterView(SelfBaseAPIView, SelfListAPIView):
    serializer_class = TwitterSerializer
    
    def get(self, request):
        instance_key = request.data.get("instance_key")
        twitter = Twitter.objects.get(uuid=instance_key)
        
        twitter_serializer = self.serializer_class(twitter)
        
        return SuccessResponse(1, 'success', {
            "twitter": twitter_serializer.data,
        }, 0)
    
    def post(self, request):
        user_id = 0
        url = request.data.get("url")
        parent_id = request.data.get("parent_id")
        node_name = request.data.get("node_name")
        
        if parent_id:
            parent = MappTree.objects.get(uuid=parent_id)
            path_name = parent.path_name + node_name
        else:
            parent, created = MappTree.objects.get_or_create(user_id=user_id, is_root=True, defaults={
                "node_type": 1,
                "node_name": "/",
                "path_name": "/",
            })
            parent_id = parent.uuid
            path_name = parent.path_name + node_name
        
        twitter = self.create_twitter(url)
        node, _ = MappTree.objects.get_or_create(user_id=user_id, parent_id=parent_id, instance_key=twitter.uuid, defaults={
                "node_type": 2,
                "path_name": path_name,
                "node_name": node_name,
            })
        node_serializer = MappTreeSerializer(node)
        twitter_serializer = self.serializer_class(twitter)
        
        return SuccessResponse(1, 'success', {
            "node": node_serializer.data,
            "twitter": twitter_serializer.data,
        }, 0)
        
        
    
    def create_twitter(self, url:str):
        data = get_post_detail(url)
        if "text" in data:
            del data["text"]
        twitter, created = Twitter.objects.get_or_create(t_id=data["t_id"], defaults=data)
        return twitter
