# coding: utf8

from rust.core.api import ApiResource, Resource
from rust.core.decorator import param_required
from rust.core.paginator import TargetPage

from business.topic.topic_repository import TopicRepository
from business.topic.fill_topic_service import FillTopicService
from business.topic.encode_topic_service import EncodeTopicService


@Resource('topic.active_topics')
class AActiveTopics(ApiResource):
	"""
	热门话题列表
	"""
	@param_required(['user', '?with_options:json', '?page:int', '?count_per_page:int', '?filters:json'])
	def get(self):
		"""
		获取热门话题列表
		"""
		user = self.params['user']
		target_page = TargetPage(self.params)
		filters = self.params.get('filters')
		topics = TopicRepository(user).get_active_topics(filters, target_page)

		fill_option = self.params.get('with_options', {'with_activity': False, 'with_dynamic': False})
		FillTopicService(user).fill(topics, fill_option)

		return {
			'topics': [EncodeTopicService(user).encode(topic) for topic in topics],
			'page_info': target_page.to_dict() if target_page else {}
		}
