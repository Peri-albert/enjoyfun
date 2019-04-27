# coding: utf8

from rust.core import business

from db.topic import models as topic_models


class VisitService(business.Service):
	"""
	访问服务(记录人次)
	"""
	def vist(self, param_object):
		"""
		访问话题
		"""
		topic_models.TopicActivity.create(
			topic_id=param_object.topic_id,
			user_id=param_object.user_id
		)