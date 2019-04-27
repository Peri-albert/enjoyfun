# coding: utf8

from rust.core import business

from business.dynamic.dynamic import Dynamic
from db.dynamic import models as dynamic_models


class DynamicFactory(business.Service):
	"""
	动态工厂
	"""
	def create(self, param_object):
		"""
		创建Dynamic对象
		"""
		db_model = dynamic_models.Dynamic.create(
			user_id = param_object.user_id,
			content = param_object.content,
			topic_id = param_object.topic_id,
			longitude = param_object.longitude,
			latitude = param_object.latitude
		)

		return Dynamic(db_model)

	def update(self, param_object):
		"""
		更新Dynamic对象
		"""
		db_model = dynamic_models.Dynamic.select().dj_where(id=param_object.id).first()
		modified = False
		if param_object.content is not None and db_model.content != param_object.content:
			db_model.content = param_object.content
			modified = True

		if param_object.topic_id is not None and db_model.topic_id != param_object.topic_id:
			db_model.topic_id = param_object.topic_id
			modified = True

		if param_object.longitude is not None and db_model.longitude != param_object.longitude:
			db_model.longitude = param_object.longitude
			modified = True

		if param_object.latitude is not None and db_model.latitude != param_object.latitude:
			db_model.latitude = param_object.latitude
			modified = True

		modified and db_model.save()

	def delete(self, param_object):
		"""
		逻辑删除Dynamic对象
		"""
		dynamic_models.Dynamic.update(
			is_deleted=True
		).dj_where(id=param_object.id).execute()

