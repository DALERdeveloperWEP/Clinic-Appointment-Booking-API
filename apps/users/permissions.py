from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin' 
    

class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'doctor' 


class IsPatient(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'patient' 


class IsOwnerByDoctor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.doctor == request.user 
    
    
class IsOwnerByPatient(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.patient == request.user 
    
    
class IsOwnerByAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.admin == request.user 

