from django.db import models


class YDocUpdateManager(models.Manager):
    async def get_snapshot(self, name):
        try:
            doc = await self.aget(name=name)
            return doc.data
        except YDocUpdate.DoesNotExist:
            return None

    async def save_snapshot(self, name, data):
        return await self.aupdate_or_create(name=name, defaults={"data": data})


class YDocUpdate(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    timestamp = models.DateTimeField(auto_now=True)
    data = models.BinaryField()

    objects = YDocUpdateManager()

    def __str__(self):
        return self.name
