from django.contrib.gis.db import models

class Flocklocation(models.Model):
    """
    Stores location, count information for flock observations.
    """

    obsdate = models.DateField(auto_now = False, auto_now_add = False),
    count = models.IntegerField('Flock Count')
    geom = models.PointField()
    user_create = models.ForeignKey('auth.user')
    create_date = models.DateTimeField('Created',
        auto_now = False,
        auto_now_add = True)
    user_last_modify = models.ForeignKey('auth.user')
    last_modify_date = models.DateTimeField('Last Modified',
        auto_now = True,
        auto_now_add = False)

    def __str__(self):
        return self.id + ' - ' self.obsdate
        #+ ' - ' + self.count + ' - (' + geom.y + ' , '  + geom.x + ')'
