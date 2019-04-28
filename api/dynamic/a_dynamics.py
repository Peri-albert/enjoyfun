# coding: utf8

from rust.core.api import ApiResource, Resource
from rust.core.decorator import param_required
from rust.core.paginator import TargetPage

from business.dynamic.dynamic_repository import DynamicRepository
from business.dynamic.fill_dynamic_service import FillDynamicService
from business.dynamic.encode_dynamic_service import EncodeDynamicService


@Resource('dynamic.dynamics')
class ADynamics(ApiResource):
	"""
	动态列表
	"""
	@param_required(['user', '?with_options:json', '?page:int', '?count_per_page:int', '?filters:json'])
	def get(self):
		"""
		获取动态列表
		"""
		user = self.params['user']
		target_page = TargetPage(self.params)
		filters = self.params.get('filters')

		dynamics = DynamicRepository(user).get_dynamics(filters, target_page)

		fill_option = self.params.get('with_options', {'with_resource': False, 'with_approval': False, 'with_comment': False})
		FillDynamicService(user).fill(dynamics, fill_option)

		return {
			'dynamics': [EncodeDynamicService(user).encode(dynamic) for dynamic in dynamics],
			'page_info': target_page.to_dict() if target_page else {}
		}
