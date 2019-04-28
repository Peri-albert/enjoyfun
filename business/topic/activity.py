# coding: utf8

from rust.core import business


class Activity(business.Model):
	"""
	活跃度
	"""
	__slots__ = (
		'id'
	)

	def __init__(self, db_model=None):
		super(Activity, self).__init__(db_model)

	@property
	def user_id(self):
		return self.context['db_model'].user_id

	@property
	def topic_id(self):
		return self.context['db_model'].topic_id
