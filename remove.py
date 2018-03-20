#-*- coding: utf-8 -*-

import os as o

o.system('docker rm -f mysql wordpress && rm -fr ~/wp-add/ && docker network rm wp_mysql_net')
