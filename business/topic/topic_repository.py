# coding: utf8

from peewee import fn

from rust.core import business

from business.topic.topic import Topic

from db.topic import models as topic_models


class TopicRepository(business.Service):

	def get_topic_by_id(self, topic_id):
		db_model = topic_models.Topic.select().dj_where(id=topic_id).first()
		if db_model:
			return Topic(db_model)

	def get_topics(self, filters=None, target_page=None):
		"""
		获取话题列表
		"""
		db_models = topic_models.Topic.select().dj_where(is_banned=False)
		if filters:
			db_models = db_models.dj_where(**filters)

		if target_page:
			db_models = target_page.paginate(db_models)

		db_models = db_models.order_by('-id')
		return [Topic(db_model) for db_model in db_models]
	
	def get_banned_topics(self, filters=None, target_page=None):
		"""
		获取被禁用的话题列表
		"""
		db_models = topic_models.Topic.select().dj_where(is_banned=True)
		if filters:
			db_models = db_models.dj_where(**filters)

		if target_page:
			db_models = target_page.paginate(db_models)

		db_models = db_models.order_by('-id')
		return [Topic(db_model) for db_model in db_models]

	def get_active_topics(self, filters=None, target_page=None):
		"""
		获取热门的话题列表
		"""

		# # # # # #
		# 人数版本 #
		# # # # # #

		# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
		# record_db_models = topic_models.TopicActivity.select(                         #
		# 	topic_models.TopicActivity,                                                 #
		# 	fn.COUNT(fn.DISTINCT(topic_models.TopicActivity.user_id)).alias('activity') #
		# ).group_by(topic_models.TopicActivity.topic_id).order_by(                     #
		# 	fn.COUNT(fn.DISTINCT(topic_models.TopicActivity.user_id)).desc()            #
		# )                                                                             #
		# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

		# # # # # #
		# 人次版本 #
		# # # # # #

		record_db_models = topic_models.TopicActivity.select(
				topic_models.TopicActivity,
				fn.COUNT(topic_models.TopicActivity.id).alias('activity')
			).group_by(topic_models.TopicActivity.topic_id).order_by(
				fn.COUNT(topic_models.TopicActivity.id).desc()
			)
		topic_ids = [record_db_model.topic_id for record_db_model in record_db_models]

		db_models = topic_models.Topic.select().dj_where(id__in=topic_ids, is_banned=True)


		if filters:
			db_models = db_models.dj_where(**filters)

		if target_page:
			db_models = target_page.paginate(db_models)

		id2topic = {db_model.id: Topic(db_model) for db_model in db_models}
		return [id2topic[topic_id] for topic_id in topic_ids]