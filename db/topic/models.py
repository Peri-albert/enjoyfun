# coding: utf8

from rust.core import db as models

class Topic(models.Model):
	"""
	注释
	"""
	name = models.CharField(default='', max_length=128) #注释
	created_at = models.DateTimeField(auto_now_add=True) #创建时间

	class Meta(object):
		table_name = 'topic_topic'

