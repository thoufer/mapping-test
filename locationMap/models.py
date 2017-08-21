from django.contrib.gis.db import models
from datetime import date

class Observation(models.Model):
    """
    Stores location, count information for flock observations.

    TODO: Currently points are saved in WGS84 projection.. Minnesota state plane
    might be more approprite.
    """

    obsdate = models.DateField('Date of Observation',
        auto_now = False,
        auto_now_add = False,
        default = date.today)
    count = models.IntegerField('Flock Count')
    location = models.PointField('Location', srid = 4326)
    user_create = models.ForeignKey('auth.user')
    create_date = models.DateTimeField('Created',
        auto_now = False,
        auto_now_add = True)
    last_modify_date = models.DateTimeField('Last Modified',
        auto_now = True,
        auto_now_add = False)

    def __str__(self):
        #return str(self.obsdate) + ' - ' + str(self.count) + \
        #' - (' + str(self.location.x) + ' ' + str(self.location.y) + ')'
        return str(self.id) + ' : ' + str(self.obsdate)
