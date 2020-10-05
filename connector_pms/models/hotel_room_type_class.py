# Copyright 2018 Alexandre Díaz <dev@redneboa.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import _, models
from openerp.exceptions import ValidationError


class HotelRoomTypeClass(models.Model):
    _inherit = "hotel.room.type.class"

    _locked_codes = []

    def write(self, vals):
        for record in self:
            if record.code_class in self._locked_codes:
                raise ValidationError(_("Can't modify channel room type class"))
        return super(HotelRoomTypeClass, self).write(vals)

    def unlink(self):
        for record in self:
            if record.code_class in self._locked_codes:
                raise ValidationError(_("Can't delete channel room type class"))
        return super(HotelRoomTypeClass, self).unlink()