#!/bin/sh
groonga -d --protocol http -n /tmp/groonga.db
tail -f /dev/null
