# coding=utf-8
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from account.views import (UserLoginAPIView, UsernameCheckAPIView, UserRegisterAPIView,
                           UserChangePasswordAPIView, EmailCheckAPIView,
                           UserAdminAPIView, UserInfoAPIView)
from announcement.views import AnnouncementAdminAPIView

from contest.views import ContestAdminAPIView, ContestProblemAdminAPIView, ContestPasswordVerifyAPIView

from group.views import (GroupAdminAPIView, GroupMemberAdminAPIView,
                         JoinGroupAPIView, JoinGroupRequestAdminAPIView)

from admin.views import AdminTemplateView

from problem.views import TestCaseUploadAPIView, ProblemTagAdminAPIView, ProblemAdminAPIView
from submission.views import SubmissionAPIView, SubmissionAdminAPIView
from contest_submission.views import ContestSubmissionAPIView
from monitor.views import QueueLengthMonitorAPIView

from contest_submission.views import contest_problem_my_submissions_list_page


urlpatterns = [
    url(r'^install/$', "install.views.install"),
    url("^$", TemplateView.as_view(template_name="oj/index.html"), name="index_page"),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^admin/$', TemplateView.as_view(template_name="admin/admin.html"), name="admin_spa_page"),
    url(r'^admin/contest/$', TemplateView.as_view(template_name="admin/contest/add_contest.html"),
        name="add_contest_page"),
    url(r'^admin/template/(?P<template_dir>\w+)/(?P<template_name>\w+).html$', AdminTemplateView.as_view(),
        name="admin_template"),

    url(r'^login/$', TemplateView.as_view(template_name="oj/account/login.html"), name="user_login_page"),
    url(r'^register/$', TemplateView.as_view(template_name="oj/account/register.html"),
        name="user_register_page"),
    url(r'^change_password/$', TemplateView.as_view(template_name="oj/account/change_password.html"),
        name="user_change_password_page"),
    url(r'^announcement/(?P<announcement_id>\d+)/$', "announcement.views.announcement_page",
        name="announcement_page"),

    url(r'^api/user/$', UserInfoAPIView.as_view(), name="user_info_api"),
    url(r'^api/login/$', UserLoginAPIView.as_view(), name="user_login_api"),
    url(r'^api/register/$', UserRegisterAPIView.as_view(), name="user_register_api"),
    url(r'^api/change_password/$', UserChangePasswordAPIView.as_view(), name="user_change_password_api"),
    url(r'^api/username_check/$', UsernameCheckAPIView.as_view(), name="username_check_api"),
    url(r'^api/email_check/$', EmailCheckAPIView.as_view(), name="email_check_api"),
    url(r'^api/contest/password/$', ContestPasswordVerifyAPIView.as_view(), name="contest_password_verify_api"),
    url(r'^api/contest/submission/$', ContestSubmissionAPIView.as_view(), name="contest_submission_api"),
    url(r'^api/submission/$', SubmissionAPIView.as_view(), name="submission_api"),

    url(r'^api/admin/announcement/$', AnnouncementAdminAPIView.as_view(), name="announcement_admin_api"),
    url(r'^api/admin/contest/$', ContestAdminAPIView.as_view(), name="contest_admin_api"),
    url(r'^api/admin/user/$', UserAdminAPIView.as_view(), name="user_admin_api"),
    url(r'^api/admin/group/$', GroupAdminAPIView.as_view(), name="group_admin_api"),
    url(r'^api/admin/group_member/$', GroupMemberAdminAPIView.as_view(), name="group_member_admin_api"),
    url(r'^api/admin/group_join/$', JoinGroupAPIView.as_view(), name="group_join_admin_api"),
    url(r'^api/admin/problem/$', ProblemAdminAPIView.as_view(), name="problem_admin_api"),
    url(r'^api/admin/contest_problem/$', ContestProblemAdminAPIView.as_view(), name="contest_problem_admin_api"),
    url(r'^api/admin/test_case_upload/$', TestCaseUploadAPIView.as_view(), name="test_case_upload_api"),
    url(r'^api/admin/tag/$', ProblemTagAdminAPIView.as_view(), name="problem_tag_admin_api"),
    url(r'^api/admin/join_group_request/$', JoinGroupRequestAdminAPIView.as_view(),
        name="join_group_request_admin_api"),
    url(r'^api/admin/submission/$', SubmissionAdminAPIView.as_view(), name="submission_admin_api_view"),
    url(r'^api/admin/monitor/$', QueueLengthMonitorAPIView.as_view(), name="queue_length_monitor_api"),



    url(r'^contest/(?P<contest_id>\d+)/problem/(?P<contest_problem_id>\d+)/$', "contest.views.contest_problem_page",
        name="contest_problem_page"),
    url(r'^contest/(?P<contest_id>\d+)/problem/(?P<contest_problem_id>\d+)/submissions/$',
        "contest_submission.views.contest_problem_my_submissions_list_page",
        name="contest_problem_my_submissions_list_page"),

    url(r'^contest/(?P<contest_id>\d+)/$', "contest.views.contest_page", name="contest_page"),
    url(r'^contest/(?P<contest_id>\d+)/problems/$', "contest.views.contest_problems_list_page",
        name="contest_problems_list_page"),
    url(r'^contest/(?P<contest_id>\d+)/submissions/$', "contest_submission.views.contest_problem_submissions_list_page",
        name="contest_problem_submissions_list_page"),
    url(r'^contest/(?P<contest_id>\d+)/submissions/(?P<page>\d+)/$',
        "contest_submission.views.contest_problem_submissions_list_page", name="contest_problem_submissions_list_page"),

    url(r'^contests/$', "contest.views.contest_list_page", name="contest_list_page"),
    url(r'^contests/(?P<page>\d+)/$', "contest.views.contest_list_page", name="contest_list_page"),
    url(r'^contest/(?P<contest_id>\d+)/$', "contest.views.contest_page", name="contest_page"),


    url(r'^problem/(?P<problem_id>\d+)/$', "problem.views.problem_page", name="problem_page"),
    url(r'^problem/(?P<problem_id>\d+)/$', "problem.views.problem_page", name="problem_page"),
    url(r'^problems/$', "problem.views.problem_list_page", name="problem_list_page"),
    url(r'^problems/(?P<page>\d+)/$', "problem.views.problem_list_page", name="problem_list_page"),
    url(r'^problem/(?P<problem_id>\d+)/submissions/$', "submission.views.problem_my_submissions_list_page",
        name="problem_my_submissions_page"),


    url(r'^submission/(?P<submission_id>\w+)/$', "submission.views.my_submission", name="my_submission_page"),
    url(r'^submissions/$', "submission.views.my_submission_list_page", name="my_submission_list_page"),
    url(r'^submissions/(?P<page>\d+)/$', "submission.views.my_submission_list_page", name="my_submission_list_page"),

    url(r'^contest/(?P<contest_id>\d+)/rank/$', "contest.views.contest_rank_page", name="contest_rank_page")

]