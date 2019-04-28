# coding: utf8

from rust.core.api import ApiResource, Resource
from rust.core.decorator import param_required
from rust.core.paginator import TargetPage
from rust.core.exceptions import BusinessError

from business.dynamic.dynamic_repository import DynamicRepository
from business.dynamic.fill_dynamic_service import FillDynamicService
from business.dynamic.encode_dynamic_service import EncodeDynamicService


@Resource('dynamic.deleted_dynamics')
class ADeletedDynamics(ApiResource):
	"""
	删除的动态列表(限管理员操作)
	"""
	@param_required(['user', '?with_options:json', '?page:int', '?count_per_page:int', '?filters:json'])
	def get(self):
		"""
		获取已删除的动态列表(限管理员操作)
		"""
		if not self.params['user'].is_manager:
			raise BusinessError(u'操作无权限')
		user = self.params['user']
		target_page = TargetPage(self.params)
		filters = self.params.get('filters')

		dynamics = DynamicRepository(user).get_deleted_dynamics(filters, target_page)

		fill_option = self.params.get('with_options', {'with_resource': False, 'with_approval': False, 'with_comment': False})
		FillDynamicService(user).fill(dynamics, fill_option)

		return {
			'dynamics': [EncodeDynamicService(user).encode(dynamic) for dynamic in dynamics],
			'page_info': target_page.to_dict() if target_page else {}
		}
