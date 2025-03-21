"""
URL configuration for docs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from .views import (
    accordion,
    alert,
    alert_dialog,
    badge,
    button,
    card,
    checkbox,
    combobox,
    command,
    command_dialog,
    dialog,
    dropdown_menu,
    form,
    input,
    installation,
    introduction,
    label,
    navigation_menu,
    popover,
    progress,
    select,
    separator,
    sheet,
    table,
    tabs,
    textarea,
    toast,
)

urlpatterns = [
    path("", introduction, name="introduction"),
    path("introduction/", introduction, name="introduction"),
    path("installation/", installation, name="installation"),
    path("accordion/", accordion, name="accordion"),
    path("alert/", alert, name="alert"),
    path("alert-dialog/", alert_dialog, name="alert_dialog"),
    path("badge/", badge, name="badge"),
    path("button/", button, name="button"),
    path("card/", card, name="card"),
    path("checkbox/", checkbox, name="checkbox"),
    path("combobox/", combobox, name="combobox"),
    path("command/", command, name="command"),
    path("command-dialog/", command_dialog, name="command_dialog"),
    path("dialog/", dialog, name="dialog"),
    path("dropdown-menu/", dropdown_menu, name="dropdown_menu"),
    path("form/", form, name="form"),
    path("input/", input, name="input"),
    path("label/", label, name="label"),
    path("navigation-menu/", navigation_menu, name="navigation_menu"),
    path("popover/", popover, name="popover"),
    path("progress/", progress, name="progress"),
    path("select/", select, name="select"),
    path("separator/", separator, name="separator"),
    path("sheet/", sheet, name="sheet"),
    path("table/", table, name="table"),
    path("tabs/", tabs, name="tabs"),
    path("textarea/", textarea, name="textarea"),
    path("toast/", toast, name="toast"),
]
