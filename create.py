#-*- coding: utf-8 -*-

import os as o



o.system('sudo docker network create wp_mysql_net')

o.system('docker run --name mysql \
	-v ~/wp-app/wp_db:/var/lib/mysql \
	--network=wp_mysql_net \
	-e MYSQL_ROOT_PASSWORD=Hsndn81hhanJks9mans \
	-d mysql')

o.system('docker run --restart=always \
	-d -p 80:80 \
	--name wordpress \
	-v ~/wp-app/www:/var/www/html \
	--network=wp_mysql_net \
	-e WORDPRESS_DB_HOST=mysql \
	-e WORDPRESS_DB_NAME=wordpress \
	-e WORDPRESS_DB_USER=root \
	-e WORDPRESS_DB_PASSWORD=Hsndn81hhanJks9mans \
	wordpress')

