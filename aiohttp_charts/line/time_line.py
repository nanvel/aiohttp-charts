import datetime
import json

from ..utils.colors import COLORS
from .. import get_chart_id


class TimeLineChart:

    MAIN_AXES = 'main'

    def __init__(self, title, height=400):
        self.title = title
        self.height = height
        self._lines = []
        self.chart_id = get_chart_id()

    def add_line(self, label, points, axes_id=None, fill=False):
        axes_id = axes_id or self.MAIN_AXES
        self._lines.append(
            {
                'points': points,
                'axes_id': axes_id,
                'label': label,
                'fill': fill
            }
        )

    @property
    def datasets(self):
        result = []
        for n, line in enumerate(self._lines):
            data = []
            for p in line['points']:
                data.append({
                    'x': p[0].isoformat() if isinstance(p[0], datetime.datetime) else p[0],
                    'y': p[1]
                })
            c = {
                'label': line['label'],
                'borderColor': COLORS[n],
                'backgroundColor': 'rgba(200, 200, 200, 0.5)',
                'fill': line['fill'],
                'yAxisID': line['axes_id'],
                'data': data
            }
            result.append(c)

        return result

    @property
    def yaxes(self):
        axes = set()
        for line in self._lines:
            axes.add(line['axes_id'])
        result = []

        if self.MAIN_AXES in axes:
            result.append({
                'type': 'linear',
                'display': True,
                'position': 'left',
                'id': self.MAIN_AXES
            })
            axes.remove(self.MAIN_AXES)
        else:
            result.append({
                'type': 'linear',
                'display': True,
                'position': 'left',
                'id': axes.pop()
            })

        for a in axes:
            result.append({
                'type': 'linear',
                'display': True,
                'position': 'right',
                'id': a,
                'gridLines': {
                    'drawOnChartArea': False
                }
            })

        return result

    def to_js(self):
        return json.dumps({
            'type': 'line',
            'data': {
                'datasets': self.datasets
            },
            'options': {
                'scales': {
                    'xAxes': [{
                        'type': 'time'
                    }],
                    'yAxes': self.yaxes
                },
                'animation': False,
                'elements': {
                    'line': {
                        'tension': 0
                    }
                }
            }
        })
