# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "mss_customization"
app_title = "MSS Customization"
app_publisher = "Libermatic"
app_description = "Customizations for MS Stores"
app_icon = "octicon octicon-file-directory"
app_color = "yellow"
app_email = "info@libermatic.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/mss_customization/css/mss_customization.css"
# app_include_js = "/assets/mss_customization/js/mss_customization.js"

# include js, css files in header of web template
# web_include_css = "/assets/mss_customization/css/mss_customization.css"
# web_include_js = "/assets/mss_customization/js/mss_customization.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "mss_customization.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "mss_customization.install.before_install"
after_install = "mss_customization.install.after_install"
setup_wizard_complete = "mss_customization.install.after_wizard_complete"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "mss_customization.notifications.get_notification_config"

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

doc_events = {
    'Journal Entry': {
        'on_cancel':
            "mss_customization.mss_loan.doctype.gold_loan.gold_loan.update_loan_on_jv_cancel",
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"mss_customization.tasks.all"
# 	],
# 	"daily": [
# 		"mss_customization.tasks.daily"
# 	],
# 	"hourly": [
# 		"mss_customization.tasks.hourly"
# 	],
# 	"weekly": [
# 		"mss_customization.tasks.weekly"
# 	]
# 	"monthly": [
# 		"mss_customization.tasks.monthly"
# 	]
# }

# Testing
# -------

before_tests = "mss_customization.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "mss_customization.event.get_events"
# }
