# -*- coding: utf-8 -*-
from flask import Blueprint
from common.libs.Helper import ops_render,iPagination,getCurrentDate

route_stat = Blueprint( 'stat_page',__name__ )

@route_stat.route( "/index" )
def index():
    return ops_render( "stat/index.html" )

@route_stat.route( "/food" )
def food():
    return ops_render( "stat/food.html" )

@route_stat.route( "/members" )
def memebr():
    return ops_render ("stat/members.html" )

@route_stat.route( "/share" )
def share():
    return ops_render( "stat/share.html" )
