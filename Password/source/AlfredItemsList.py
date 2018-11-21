# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from cgi import escape
from uuid import uuid4


class AlfredItemsList(object):
    def __init__(self, items=None, fileicon=False):
        self.items = items or []
        icon_tag = '<icon type="fileicon">' if fileicon else '<icon>'
        self.pattern = (
            '<item arg="{arg}" uid="{uid}" valid="{valid}">"' +
                '<title>{title}</title>' +
                '<subtitle>{subtitle}</subtitle>' +
                icon_tag+'{icon}</icon>' +
            '</item>'
        )

    def append(self, arg, title, subtitle, icon='', valid='yes', uid=None):
        uid = uid or str(uuid4())
        self.items.append(
            (arg, escape(title), escape(subtitle), icon, valid, uid)
        )

    def is_empty(self):
        return self.items == []

    def __str__(self):
        items = "".join([
            self.pattern.format(
                arg=arg,
                title=escape(title),
                subtitle=escape(subtitle),
                icon=icon,
                valid=valid,
                uid=uid
            ) for arg, title, subtitle, icon, valid, uid in self.items
        ])
        return ('<items>' + items + '</items>').encode('utf-8')

    def __add__(self, other):
        return AlfredItemsList(self.items + other.items)
