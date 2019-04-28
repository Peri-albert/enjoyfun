# coding: utf8

from rust.core.business import ParamObject
from rust.core.api import ApiResource, Resource
from rust.core.decorator import param_required
from rust.core.exceptions import BusinessError

from business.topic.topic_repository import TopicRepository
from business.topic.topic_factory import TopicFactory
from business.topic.fill_topic_service import FillTopicService
from business.topic.encode_topic_service import EncodeTopicService
from business.topic.visit_service import VisitService


@Resource('topic.topic')
class ATopic(ApiResource):
	"""
	话题
	"""
	@param_required(['user', 'id:int', '?with_options:json'])
	def get(self):
		"""
		根据id获取话题
		"""
		user = self.params['user']
		topic = TopicRepository(user).get_topic_by_id(self.params['id'])

		fill_option = self.params.get('with_options', {'with_activity': False, 'with_dynamic': False})
		FillTopicService(user).fill([topic], fill_option)

		return EncodeTopicService(user).encode(topic)

	@param_required(['user', 'name', 'avatar', 'description'])
	def put(self):
		"""
		创建话题(限管理员操作)
		"""
		if not self.params['user'].is_manager:
			raise BusinessError(u'操作无权限')
		user = self.params['user']
		param_object = ParamObject({
			'name': self.params['name'],
			'avatar': self.params['avatar'],
			'description': self.params['description']
		})
		topic = TopicFactory(user).create(param_object)
		visit_history = ParamObject({
			'topic_id': topic.id,
			'user_id': user.id
		})
		VisitService(user).visit(visit_history)
		return {
			'id': topic.id
		}

	@param_required(['user', 'id:int', '?name', '?avatar', '?description'])
	def post(self):
		"""
		修改话题（限管理员操作）
		"""
		if not self.params['user'].is_manager:
			raise BusinessError(u'操作无权限')
		user = self.params['user']
		param_object = ParamObject({
			'id': self.params['id'],
			'name': self.params.get('name'),
			'avatar': self.params.get('avatar'),
			'description': self.params.get('description')
		})
		TopicFactory(user).update(param_object)
		return {}
