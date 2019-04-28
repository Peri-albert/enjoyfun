# coding: utf8

from rust.core import business

from db.dynamic import models as dynamic_models

class Dynamic(business.Model):

	__slots__ = (
		'id',
		'content',
		'longitude',
		'latitude',
		'created_at',
		'is_deleted'
	)

	def __init__(self, db_model=None):
		super(Dynamic, self).__init__(db_model)

	@property
	def user_id(self):
		return self.context['db_model'].user_id

	@property
	def topic_id(self):
		return self.context['db_model'].topic_id

	def update_resources(self, resources):
		"""
		更新动态资源
		"""
		dynamic_models.DynamicResource.delete().dj_where(dynamic_id=self.id).execute()
		rows = []
		for resource in resources:
			rows.append({
				'dynamic_id': self.id,
				'url': resource['url'],
				'size': resource['size'],
				'type': dynamic_models.DYNAMIC_RESOURCE_TYPE[resource['type'.upper()]]
			})
		dynamic_models.DynamicResource.insert_many(rows).dj_where(dynamic_id=self.id).execute()
