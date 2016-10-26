# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "issue_and_log"
app_title = "Issue and Log"
app_publisher = "Ragav"
app_description = "issue and log"
app_icon = "octicon octicon-comment"
app_color = "#202020"
app_email = "sragav95@gmail.com"
app_license = "GNU"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/issue_and_log/css/issue_and_log.css"
# app_include_js = "/assets/issue_and_log/js/issue_and_log.js"

# include js, css files in header of web template
# web_include_css = "/assets/issue_and_log/css/issue_and_log.css"
# web_include_js = "/assets/issue_and_log/js/issue_and_log.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "issue_and_log.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "issue_and_log.install.before_install"
# after_install = "issue_and_log.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "issue_and_log.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"issue_and_log.tasks.all"
# 	],
# 	"daily": [
# 		"issue_and_log.tasks.daily"
# 	],
# 	"hourly": [
# 		"issue_and_log.tasks.hourly"
# 	],
# 	"weekly": [
# 		"issue_and_log.tasks.weekly"
# 	]
# 	"monthly": [
# 		"issue_and_log.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "issue_and_log.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "issue_and_log.event.get_events"
# }

