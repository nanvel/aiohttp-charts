from aiohttp import web
from jinja2 import Environment, select_autoescape, FileSystemLoader

from .utils.path import rel


jinja_env = Environment(
    loader=FileSystemLoader(rel('templates')),
    autoescape=select_autoescape(['html', 'xml'])
)


class ChartsComposer:

    def __init__(self, title):
        self.title = title
        self._charts = []
        self._template = jinja_env.get_template('charts.j2')

    def add_chart(self, chart):
        self._charts.append(chart)

    def compose(self, app):
        return web.Response(
            body=self._template.render({
                'charts': self._charts,
                'development': app.get('aiohttp_charts_development', False)
            }),
            content_type='text/html'
        )
