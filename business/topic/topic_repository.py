# coding: utf8

from rust.core import business

from business.topic.topic import Topic

from db.topic import models as topic_models

class TopicRepository(business.Service):

	def get_topic_by_id(self, topic_id):
		db_model = topic_models.Topic.select().dj_where(id=topic_id).first()
		if db_model:
			return Topic(db_model)

