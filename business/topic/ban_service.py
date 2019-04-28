# coding: utf8

from rust.core import business

from db.topic import models as topic_models


class BanService(business.Service):
	"""
	禁用话题服务
	"""
	def ban(self, param_object):
		"""
		禁用话题
		"""
		topic_models.Topic.update(
			is_banned = True
		).dj_where(id=param_object.topic_id).execute()

	def unban(self, param_object):
		"""
		解禁话题
		"""
		topic_models.Topic.update(
			is_banned = False
		).dj_where(id=param_object.topic_id).execute()
