from django.db import models
from server.models import Machine

class Whdmachine(models.Model):
	machine = models.ForeignKey(Machine)
	serial = models.TextField()
	hostname = models.TextField()
	mac_address_en0 = models.TextField(blank=True, null=True)
	productname = models.TextField()
	memorytotal = models.TextField()
	cpu = models.TextField()
	macosx_productversion = models.TextField()
	ipaddress = models.TextField()
	sp_local_host_name = models.TextField()
	macaddress_wifi = models.TextField(blank=True, null=True)
	macaddress_eth = models.TextField(blank=True, null=True)
	hd_total = models.TextField()
	
	def __unicode__(self):
		return self.hostname
	class Meta:
		ordering = ['hostname']
