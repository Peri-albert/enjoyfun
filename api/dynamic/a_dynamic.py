# coding: utf8

from rust.core.business import ParamObject
from rust.core.api import ApiResource, Resource
from rust.core.decorator import param_required
from rust.core.exceptions import BusinessError

from business.dynamic.dynamic_repository import DynamicRepository
from business.dynamic.dynamic_factory import DynamicFactory
from business.dynamic.fill_dynamic_service import FillDynamicService
from business.dynamic.encode_dynamic_service import EncodeDynamicService


@Resource('dynamic.dynamic')
class ADynamic(ApiResource):
	"""
	动态
	"""
	@param_required(['user', 'id:int', '?with_options:json'])
	def get(self):
		"""
		根据动态id获取动态
		"""
		user = self.params['user']
		dynamic = DynamicRepository(user).get_dynamic_by_id(self.params['id'])

		fill_option = self.params.get('with_options', {'with_resource': False, 'with_approval': False, 'with_comment': False})
		FillDynamicService(user).fill([dynamic], fill_option)

		return EncodeDynamicService(user).encode(dynamic)

	@param_required(['user', 'content', 'topic_id', 'longitude', 'latitude', '?resources:json'])
	def put(self):
		"""
		发布动态
		"""
		user = self.params['user']
		param_object = ParamObject({
			'user_id': user.id,
			'content': self.params['content'],
			'topic_id': self.params['topic_id'],
			'longitude': self.params['longitude'],
			'latitude': self.params['latitude']
		})
		dynamic = DynamicFactory(user).create(param_object)

		if self.params.get('resources'):
			dynamic.update_resources(self.params['resources'])

		return {
			'id': dynamic.id
		}

	@param_required(['user', 'id:int', '?content', '?topic_id', '?longitude', '?latitude', '?resources:json'])
	def post(self):
		"""
		修改动态(限管理员或本人操作)
		"""
		user = self.params['user']
		dynamic = DynamicRepository(user).get_dynamic_by_id(self.params['id'])
		if not user.is_manager or user.id != dynamic.user_id:
			raise BusinessError(u'操作无权限')
		param_object = ParamObject({
			'content': self.params['content'],
			'topic_id': self.params['topic_id'],
			'longitude': self.params['longitude'],
			'latitude': self.params['latitude']
		})
		DynamicFactory(user).update(param_object)

		if self.params.get('resources'):
			dynamic.update_resources(self.params['resources'])

		return {}

	@param_required(['user', 'id:int'])
	def delete(self):
		"""
		删除动态(限管理员或本人操作)
		"""
		user = self.params['user']
		dynamic = DynamicRepository(user).get_dynamic_by_id(self.params['id'])
		if not user.is_manager or user.id != dynamic.user_id:
			raise BusinessError(u'操作无权限')
		param_object = ParamObject({
			'id': self.params['id']
		})
		DynamicFactory(user).delete(param_object)
		return {}
