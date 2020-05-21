# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import viewsets

from rest_framework import authentication, permissions, viewsets

from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework import status

from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.generics import RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView

from .serializers import *
from .models import *

# Create your views here.


class DefaultsMixin(object):
    """docstring for DefaultsM"""
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
        )
    permission_classes = (
        permissions.IsAuthenticated,
        )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by =100



class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
     queryset = User.objects.all()
     serializer_class = UserSerializer


class SprintViewSet(DefaultsMixin, viewsets.ModelViewSet):
	"""
	A viewset for viewing and editing user instances.
	"""
	#permission_classes = (IsAuthenticated,)
	#model = Sprint
	queryset = Sprint.objects.order_by('end');
	serializer_class = SprintSerializer


class TaskViewSet(viewsets.ModelViewSet):
	"""
	A viewset for viewing and editing user instances.
	"""
	#permission_classes = (IsAuthenticated,)
	#model = Sprint
	queryset = Task.objects.all();
	serializer_class = TaskSerializer


class UserLoginAPIView(GenericAPIView):

    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.user
            print 'user',user
            token, _ = Token.objects.get_or_create(user=user)
            return Response(
                data=TokenSerializer(token).data,
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )



class UserTokenAPIView(RetrieveDestroyAPIView):
    lookup_field = "key"
    serializer_class = TokenSerializer
    queryset = Token.objects.all()

    def filter_queryset(self, queryset):
        return queryset.filter(user=self.request.user)

    def retrieve(self, request, key, *args, **kwargs):
    	print 'Users',self.request.user
        if key == "current":
            instance = Token.objects.get(key=request.auth.key)
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        return super(UserTokenAPIView, self).retrieve(request, key, *args, **kwargs)

    def destroy(self, request, key, *args, **kwargs):
        if key == "current":
            Token.objects.get(key=request.auth.key).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return super(UserTokenAPIView, self).destroy(request, key, *args, **kwargs)