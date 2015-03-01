from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from yoparty.models import YoMember, YoGroup
from yoparty import yoapi


class Command(BaseCommand):
    help = "To be called by cron to send location Yos."

    def handle(self, *args, **options):
        time = timezone.now()-settings.LOCATION_DELAY_TIME
        groups = YoGroup.objects.filter(location_time__lte=time)
        for g in groups:
            members = YoMember.objects.filter(group=g).exclude(location_time__isnull=True)
            if members.count() < 2:
                for m in members:
                    m.location_time = None
                    m.save(update_fields=['location_time'])
            else:
                if g.location_type in ['M', 'U']:
                    print("mean or userMean")
                    mlat = mlng = 0.0
                    for m in members:
                        mlat += m.lat
                        mlng += m.lng
                    mlat /= len(members)
                    mlng /= len(members)
                elif g.location_type == 'L':
                    print("userLoc")
                    m = members.order_by('location_time')[0]
                    mlat, mlng = m.lat, m.lng

                if g.location_type == 'U':
                    print("userLoc")
                    # mlat and mlng are mean now
                    distrec = 9999999
                    for m in members:
                        dist = (mlat-m.lat)**2 + (mlng-m.lng)**2
                        if  dist < distrec:
                            distrec = dist
                            mlat, mlng = m.lat, m.lng

                for m in members:
                    print(m)
                    yoapi.send_yo(m.username, api_token=g.api_token, location='%s;%s' % (mlat, mlng))
                print(mlat, mlng)

            g.location_time = None
            g.save(update_fields=['location_time'])
