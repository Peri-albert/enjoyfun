# coding: utf8
from math import radians, cos, sin, asin, sqrt, pi

from rust.core import business

from business.dynamic.dynamic import Dynamic

from db.dynamic import models as dynamic_models

EARTH_RADIUS = 6371393

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

	def get_deleted_dynamics(self, filters=None, target_page=None):
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

	def get_nearby_dynamics(self, param_object, filters=None, target_page=None):
		"""
		获取附近的动态列表
		"""
		account_longitude = param_object.account_longitude
		account_latitude = param_object.account_latitude
		angle = 0
		distance = 3000
		max_longitude = account_longitude
		min_longitude = account_longitude
		max_latitude = account_latitude
		min_latitude = account_latitude

		while angle <= 2:
			dynamic_longitude = account_longitude *	distance * sin(angle) / (EARTH_RADIUS * cos(account_latitude) * 2 * pi / 360)
			dynamic_latitude = account_latitude + cos(angle) / (EARTH_RADIUS * 2 * pi /360)

			if dynamic_longitude < min_longitude:
				min_longitude = dynamic_longitude
			elif dynamic_longitude > max_longitude:
				max_longitude = dynamic_longitude

			if dynamic_latitude < min_latitude:
				min_latitude = dynamic_latitude
			elif dynamic_latitude > max_latitude:
				max_latitude = dynamic_latitude

			angle += 0.01 * pi

		db_models = dynamic_models.Dynamic.select().dj_where(
			is_deleted=False,
			longitude__in=[min_longitude, max_longitude],
			latitude__in=[min_latitude, max_latitude]
		)
		if filters:
			db_models = db_models.dj_where(**filters)

		if target_page:
			db_models = target_page.paginate(db_models)

		db_models = db_models.order_by('-id')
		return [Dynamic(db_model) for db_model in db_models]