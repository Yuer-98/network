# coding=utf-8
import json
from flask import Flask
from flask import jsonify,make_response
from flask_restful import Resource,reqparse
from apis.basic_operation import excute

class DivideAPI(Resource):
	'''
	操作步骤七（telnet完成）：将Router fa0/0划分为两个子接口
	'''
	def post(self):
		parse = reqparse.RequestParser()
		parse.add_argument('ip',type=str,help='错误的ip',default='192.168.5.1')
		parse.add_argument('username',type=str,help='错误的username',default='root')
		parse.add_argument('password',type=str,help='错误的password',default='123456')
		args = parse.parse_args()
		# 从前端请求中解析参数
		ip = args.get('ip')
		username = args.get('username')
		password = args.get('password')

		# 这里调用（操作/验证）脚本
		# 将Router fa0/0划分为两个子接口
		excute(ip, username, password, './scripts/Router.txt')
		# 以下为实例代码
		token = 'opearte step 7 : telnet complete：divide Router fa0/0'
		response = make_response(jsonify(code=0,data={'token':token},message='OK'))
		return response
