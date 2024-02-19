from rest_framework.views import APIView
from .serializers import StudentSerializer
from django.http import JsonResponse
from .models import Student
from django.http.response import JsonResponse, Http404
from rest_framework.response import Response

# Create your views here.

class StudentView(APIView):
    
    def post(self, request):
        data = request.data
        serializer = StudentSerializer(data=data)

        if serializer.is_valid():

            # Check if student already exists
            existing_student = Student.objects.filter(
                first_name = data['first_name'],
                last_name = data['last_name'],
                email = data['email'],
                reg_no = data['reg_no'],
            ).first()

            if existing_student:
                return JsonResponse(
                    "Student already exists",
                    safe=False
                )
            
            # If student doesn't exist, create a new one
            serializer.save()
            return JsonResponse(
                "Student created successfully",
                safe=False
            )
        
        return JsonResponse(
            "Failed to add student",
            safe=False
        )
    

    def get_student(self, pk):
        try:
            student = Student.objects.get(pk=pk)
            return student
        except Student.DoesNotExist:
            raise Http404
    

    def get(self, request, pk=None):
        if pk:
            data = self.get_student(pk)
            serializer = StudentSerializer(data)
        else:
            data = Student.objects.all()
            serializer = StudentSerializer(data, many=True)
            
        return Response(serializer.data)
    

    def put(self, request, pk=None):
        student_to_update = Student.objects.get(student_id=pk)
        serializer = StudentSerializer(student_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(
                "Student updated successfully",
                safe=False
            )
        else:
            return JsonResponse(
                "Failed to update student",
                safe=False
            )


    def delete(self, request, pk):
        student_to_delete = Student.objects.get(student_id=pk)
        student_to_delete.delete()
        return JsonResponse(
            "Student deleted successfully",
            safe=False
        )


