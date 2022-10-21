from email.policy import default
from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File

from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask


class QRCode(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, default='Link')
    name = models.CharField(max_length=500)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        QRcode = qrcode.QRCode()
        QRcode.add_data(self.name)
        QRcode.make()
        QRimg = QRcode.make_image(
            image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer(),
            color_mask=RadialGradiantColorMask(),
            # embeded_image_path="media/logo.png"   
        )
        fname = 'qr_code-str(self.id).png'
        buffer = BytesIO()
        QRimg.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        QRimg.close()
        super().save(*args, **kwargs)