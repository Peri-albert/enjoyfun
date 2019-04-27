# coding: utf8

from rust.core import business
from rust.core.exceptions import BusinessError

from business.topic.topic import Topic
from db.topic import models as topic_models

class TopicFactory(business.Service):

	def create(self, param_object):
		#首先检查重名
		if topic_models.Topic.select().dj_where(name=param_object.name).first():
			raise BusinessError('existed')

		db_model = topic_models.Topic.create(
			name = param_object.name
		)

		return Topic(db_model)

	def update(self, param_object):
		# 首先检查重名
		db_model = topic_models.Topic.select().dj_where(id=param_object.id).first()
		if db_model.name != param_object.name:
			if topic_models.Topic.select().dj_where(name=param_object.name).first():
				raise BusinessError('existed')

			db_model.name = param_object.name

		db_model.save()

	def delete(self, param_object):
		topic_models.Topic.delete().dj_where(id=param_object.id).execute()

