# coding: utf8

from rust.core import db as models

DYNAMIC_RESOURCE_TYPE = {
	'IMAGE': 0,
	'AUDIO': 1,
	'VIDEO': 2
}

DYNAMIC_RESOURCE_TYPE2TEXT = {
	DYNAMIC_RESOURCE_TYPE['IMAGE']: 'image',
	DYNAMIC_RESOURCE_TYPE['AUDIO']: 'audio',
	DYNAMIC_RESOURCE_TYPE['VIDEO']: 'video'
}


class Dynamic(models.Model):
	"""
	动态
	"""
	user_id = models.IntegerField(default=0)  # 发布人的user_id
	content = models.TextField(default='')  # 消息内容
	topic_id = models.IntegerField(default=0)  # 话题的id
	longitude = models.FloatField(default=0)  # 发布地点的经度
	latitude = models.FloatField(default=0)  # 发布地点的纬度
	created_at = models.DateTimeField(auto_now_add=True) # 创建时间
	is_deleted = models.BooleanField(default=False)  # 是否删除

	class Meta(object):
		table_name = 'dynamic_dynamic'


class DynamicResource(models.Model):
	"""
	动态资源
	"""
	dynamic_id = models.IntegerField(default=0, index=True)  # 动态id
	url = models.CharField(max_length=1024)  # 资源url
	size = models.CharField(max_length=64, default='')  # 资源大小
	type = models.IntegerField(default=DYNAMIC_RESOURCE_TYPE['IMAGE'])  # 资源类型

	class Meta(object):
		table_name = 'dynamic_resource'


class DynamicApproval(models.Model):
	"""
	动态点赞
	"""
	dynamic_id = models.IntegerField(default=0, index=True)  # 动态id
	user_id = models.IntegerField(default=0, index=True)  # 点赞者的user_id

	class Meta(object):
		table_name = 'dynamic_approval'


class DynamicComment(models.Model):
	"""
	动态评论
	"""
	dynamic_id = models.IntegerField(default=0, index=True)  # 动态id
	user_id = models.IntegerField(default=0, index=True)  # 评论者的user_id
	content = models.TextField(default='')  # 评论内容
	created_at = models.DateTimeField(auto_now_add=True) # 创建时间

	class Meta(object):
		table_name = 'dynamic_comment'
