#!/usr/bin/env python
#-*-coding: utf-8 -*-

"""
    items.py
    ~~~~~~~~
    Retrieve Archive.org items

    :copyright: (c) 2015 by Internet Archive
    :license: see LICENSE for more details.
"""

from flask import render_template, Response, request
from flask.views import MethodView
from views import rest_api, paginate
from api import item, items, mimetype, download

class Items(MethodView):
    @rest_api
    @paginate()
    def get(self, page=1, limit=100):
        return items(page=page, limit=limit)


class Item(MethodView):
    @rest_api
    def get(self, iid):
        return item(iid)


class Metadata(MethodView):
    @rest_api
    def get(self, iid):
        return item(iid)['metadata']


class Reviews(MethodView):
    @rest_api
    def get(self, iid):
        return item(iid)['reviews']


class Files(MethodView):
    @rest_api
    def get(self, iid):
        return item(iid)['files']


class File(MethodView):
    def get(self, iid, filename):
        """Download the specified file
        """
        return Response(download(iid, filename),
                        mimetype=mimetype(filename))


urls = (
    '/<iid>/metadata', Metadata,
    '/<iid>/reviews', Reviews,
    '/<iid>/files/<filename>', File,
    '/<iid>/files', Files,
    '/<iid>', Item,
    '', Items
    )
