# coding: utf8

from rust.core.business import ParamObject
from rust.core.api import ApiResource, Resource
from rust.core.decorator import param_required
from rust.core.paginator import TargetPage

from business.dynamic.dynamic_repository import DynamicRepository
from business.dynamic.fill_dynamic_service import FillDynamicService
from business.dynamic.encode_dynamic_service import EncodeDynamicService


@Resource('dynamic.nearby_dynamics')
class ANearbyDynamics(ApiResource):

	@param_required(['user', 'longitude', 'latitude', '?with_options:json', '?page:int', '?count_per_page:int', '?filters:json'])
	def get(self):
		user = self.params['user']
		param_object = ParamObject({
			'account_longitude': self.params['longitude'],
			'account_latitude': self.params['latitude']
		})
		target_page = TargetPage(self.params)
		filters = self.params.get('filters')

		dynamics = DynamicRepository(user).get_nearby_dynamics(param_object, filters, target_page)

		fill_option = self.params.get('with_options', {'with_resource': False, 'with_approval': False, 'with_comment': False})
		FillDynamicService(user).fill(dynamics, fill_option)

		return {
			'dynamics': [EncodeDynamicService(user).encode(dynamic) for dynamic in dynamics],
			'page_info': target_page.to_dict() if target_page else {}
		}