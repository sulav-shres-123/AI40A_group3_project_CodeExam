"""Shared helpers for every page controller."""
from flask import render_template


class BaseController:
    def render(self, template, **context):
        return render_template(template, **context)
