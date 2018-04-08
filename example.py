import datetime

from aiohttp import web

from aiohttp_charts import setup_charts, ChartsComposer
from aiohttp_charts.line import TimeLineChart


def handler(request):
    composer = ChartsComposer(title="Example")

    chart = TimeLineChart(title='Example chart 1')
    now = datetime.datetime.utcnow()
    chart.add_line(
        label='Line 1',
        points=[(now + datetime.timedelta(seconds=i), i) for i in range(10)]
    )
    chart.add_line(
        label='Line 2',
        axes_id='axes1',
        points=[(now + datetime.timedelta(seconds=i), 100 - i * 5) for i in range(10)]
    )
    composer.add_chart(chart)

    return composer.compose(app=request.app)


if __name__ == '__main__':
    app = web.Application()

    app.router.add_get('/', handler)
    setup_charts(app, development=True)

    web.run_app(app, port=8080)
