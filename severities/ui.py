from reviewboard.reviews.ui.base import FileAttachmentReviewUI


class SeverityReviewUI(FileAttachmentReviewUI):
    """ReviewUI for file reviews with severity"""
    template_name = 'severities_extension/severity.html'
    object_key = 'file_object'