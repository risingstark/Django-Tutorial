"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from courses.views import (
        my_fav,
        CourseView,
        CourseListView
    )

app_name = 'courses'
urlpatterns = [
    #path('', my_fav, name='courses-list'),
    path('', CourseListView.as_view(), name='courses-list'),
    # path('create/', product_create_view , name='product-create'),
     path('<int:id>/', CourseView.as_view(), name='course-detail'),
    # path('<int:id>/delete', product_delete_view, name='product-delete'),
]





