from .composer import ChartsComposer
from .utils.path import rel


_chart_counter = 0


def setup_charts(app, development=False):
    if development:
        app.router.add_static('/charts-static', rel('static'))
    app['aiohttp_charts_development'] = development


def get_chart_id():
    global _chart_counter
    _chart_counter += 1
    return _chart_counter
