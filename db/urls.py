from rest_framework import routers
from db.api import UserView

router = routers.DefaultRouter()
router.register('api/users', UserView, 'db')

urlpatterns = router.urls
