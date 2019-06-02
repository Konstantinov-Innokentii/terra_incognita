# -*- coding: utf_8 -*-

from flask_restful import Api, Resource, abort

from .blueprint import blueprint


class NoResource(Resource):

    def get(self, path):
        abort(404)


api_v1 = Api(blueprint)
api_v1.add_resource(NoResource, '/<path:path>')
