from django.conf.urls import url
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^self/$', views.about, name="about"),
    # url(r'^get_verified/$', views.ngo, name="ngo"),
    # url(r'^not_verified/$', views.not_verified, name="not_verified"),
    # url(r'^admin_verify/$', views.verify_from_admin, name="verification_from_admin"),
    # url(r'^verified_as_true/(?P<pk>\d+)/$',views.Verification_Status_True, name="verified_as_true"),
    # url(r'^verified_as_false/(?P<pk>\d+)/$',views.Verification_Status_False, name="verified_as_false"),
    # url(r'^mail_Y/$', views.mail_Y, name="mail_of_acceptance"),
    # url(r'^mail_N/$', views.mail_N, name="mail_of_rejectance"),
    # url(r'^post_request/$', views.post_request, name="post_request"),
    # url(r'^fund_request/$', views.donation,name="fund request"),
    # url(r'^payment/$', views.payment, name='payment'),
    # url(r'^charge/$', views.charge, name="charge"),
    url(r'^product/$', views.products, name="products"),
    url(r'^product/1/$', views.pro1, name="pro1"),
    url(r'^product/2/$', views.pro2, name="pro2"),
    url(r'^product/3/$', views.pro3, name="pro3"),
    url(r'^product/4/$', views.pro4, name="pro4"),
    url(r'^software/$', views.software, name="software"),
    url(r'^software/1/$', views.sof1, name="sof1"),
    url(r'^software/2/$', views.sof2, name="sof2"),
    url(r'^calibrate/$', views.calibrate, name="calibrate"),
    url(r'^calibrate/1/$', views.cal1, name="cal1"),
    url(r'^calibrate/2/$', views.cal2, name="cal2"),
    url(r'^atex/$', views.Atex, name="Atex"),
    url(r'^atex/1/$', views.Ax1, name="Ax1"),
    url(r'^atex/2/$', views.Ax2, name="Ax2"),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)