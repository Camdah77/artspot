from django.db import models, connections
from django.contrib.auth import SESSION_KEY

class Meta:
    app_label = 'artspot'

connections.close_all()