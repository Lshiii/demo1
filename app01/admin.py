from django.shortcuts import render
from app01 import models
def admin_list(request):
    """管理员列表"""
    queryset = models.Admin.objects.all()

    context = {
        'queryset': queryset
    }
    return render(request, 'admin_list.html', context)