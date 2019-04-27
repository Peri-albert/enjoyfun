# coding: utf8

from rust.core import business

from business.dynamic.dynamic import Dynamic

from db.dynamic import models as dynamic_models


class DynamicRepository(business.Service):
	"""
	获取Account对象的repository
	"""
	def get_dynamic_by_id(self, dynamic_id):
		"""
		根据id获取account对象
		"""
		db_model = dynamic_models.Dynamic.select().dj_where(id=dynamic_id, is_deleted=False).first()
		if db_model:
			return Dynamic(db_model)

	def get_dynamics(self, filters=None, target_page=None):
		"""
		获取动态列表
		"""
		db_models = dynamic_models.Dynamic.select().dj_where(is_deleted=False)
		if filters:
			db_models = db_models.dj_where(**filters)

		if target_page:
			db_models = target_page.paginate(db_models)

		db_models = db_models.order_by('-id')
		return [Dynamic(db_model) for db_model in db_models]

	def get_dynamics(self, filters=None, target_page=None):
		"""
		获取动态列表
		"""
		db_models = dynamic_models.Dynamic.select().dj_where(is_deleted=True)
		if filters:
			db_models = db_models.dj_where(**filters)

		if target_page:
			db_models = target_page.paginate(db_models)

		db_models = db_models.order_by('-id')
		return [Dynamic(db_model) for db_model in db_models]

