from reviewboard.extensions.base import Extension
from reviewboard.extensions.hooks import ReviewUIHook
from severities.ui import SeverityReviewUI


class SeverityExtension(Extension):
    is_configurable = True
    has_admin_site = True

    def __init__(self, *args, **kwargs):
        super(SeverityExtension, self).__init__(*args, **kwargs)
        self.reviewui_hook = ReviewUIHook(self, [SeverityReviewUI])
