from django.shortcuts import render
from django.http import JsonResponse , HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import  NoteSerializer
from .models import Note



@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    
    return   Response(serializer.data)

@api_view(['GET'])
def getNote(request , pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    
    return   Response(serializer.data)



@api_view(['POST'])
def createNote(request ):
    Data = request.data
    note = Note.objects.create(
        body = Data["body"]
    )    
    serializer = NoteSerializer(note, many=False)
    
    return   Response(serializer.data)
    
    
@api_view(['PUT'])
def updatedNote(request , pk ):
    data = request.data
    note = Note.objects.get(id=pk)
     
    serializer = NoteSerializer(note, data = request.data )
    if serializer.is_valid():
        serializer.save()
    
    return   Response(serializer.data)
    
 

@api_view(['DELETE'])
def deleteNote(request , pk):
    note = Note.objects.get(id=pk)    
    note.delete()
     
    return   Response("deleted was succffully !!!")



 
# def test (request):
#     return HttpResponse('Ahlan Ramadan')



# @api_view(['GET'])
# def getRoutes (request):
    
#     routes = [
#         {
#             'endpoints':'/notes/',
#             'method':'GET',
#             'body':None,
#             'description':'Returns an array of notes'            
#         },
#         {
#             'endpoints':'/notes/id',
#             'method':'GET',
#             'body':None,
#             'description':'Returns a single note object'            
#         },
#         {
#             'endpoints':'/notes/create/',
#             'method':'POST',
#             'body':{'body': ""},
#             'description':'Creates new note with data sent in post requirement'            
#         },
#         {
#             'endpoints':'/notes/id/update/',
#             'method':'PUT',
#             'body':{'body': ""},
#             'description':'Creates an existing note with data '            
#         },
#         {
#             'endpoints':'/notes/id/delete/',
#             'method':'DELETE',
#             'body':None,
#             'description':'Deletes an existing note'          
#         }
#     ]
    
#     # return JsonResponse(routes , safe=False);
#     return Response(routes)




