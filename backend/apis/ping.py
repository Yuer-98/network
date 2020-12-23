import json
from flask import Flask
from flask import jsonify,make_response
from flask_restful import Resource,reqparse

class PingAPI(Resource):
	'''
	验证步骤五（telnet完成）：验证Router可以ping通PC1和PC2，证明可以相互ping通。
	'''
	def get(self):
		token = '验证步骤五（telnet完成）：验证Router可以ping通PC1和PC2，证明可以相互ping通。'
		response = make_response(jsonify(code=0,data={'token':token},message='OK'))
		return response