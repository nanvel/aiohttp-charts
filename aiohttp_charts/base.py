from . import get_chart_id


class BaseChart:

    def __init__(self, title, height=400, extra=None):
        self.title = title
        self.height = height
        self.extra = extra or ''
        self._lines = []
        self._chart_id = None

    @property
    def chart_id(self):
        if self._chart_id is None:
            self._chart_id = get_chart_id()
        return self._chart_id
