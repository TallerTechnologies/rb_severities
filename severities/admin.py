from reviewboard.extensions.base import get_extension_manager

from severities.extension import SeverityExtension
from severities.models import Severity


# You must get the loaded instance of the extension to register to the
# admin site.
extension_manager = get_extension_manager()
extension = extension_manager.get_enabled_extension(SeverityExtension.id)

# Register the Model to the severitiess admin site.
extension.admin_site.register(Severity)