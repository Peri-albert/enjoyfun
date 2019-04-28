# coding: utf8

from rust.core import db as models


class Topic(models.Model):
	"""
	话题
	"""
	name = models.CharField(default='', max_length=128)  # 名称
	avatar = models.TextField(default='')  # 头像
	description = models.TextField(default='')  # 描述
	created_at = models.DateTimeField(auto_now_add=True)  # 创建时间
	is_banned = models.BooleanField(default=False)  # 禁用情况

	class Meta(object):
		table_name = 'topic_topic'


class TopicActivity(models.Model):
	"""
	话题热度
	"""
	topic_id = models.IntegerField(default=0, index=True)  # 话题id
	user_id = models.IntegerField(default=0, index=True)  # 用户id

	class Meta(object):
		table_name = 'topic_activity'
