#!/bin/sh
heroku config:get DATABASE_URL -s  >> .env -a bfds-tax-records
