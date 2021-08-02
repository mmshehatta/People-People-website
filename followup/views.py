from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from followup.models import Question, ContactUs, Review
from followup.serializers import QuestionSerializer, ContactUsSerializer, ReviewSerializer

from django.core.files.storage import default_storage

# Create your views here.


@csrf_exempt
def questionApi(request,id=0):
    if request.method=='GET':
        questions = Question.objects.all()
        questions_serializer = QuestionSerializer(questions, many=True)
        return JsonResponse(questions_serializer.data, safe=False)
    
    elif request.method=='POST':
        question_data=JSONParser().parse(request)
        question_serializer = QuestionSerializer(data=question_data)
        if question_serializer.is_valid():
            question_serializer.save()
            return JsonResponse("Added SuccessFully!!", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    
    elif request.method == 'PUT':
        question_data = JSONParser().parse(request)
        question=Question.objects.get(id=question_data['id'])
        question_serializer=QuestionSerializer(question, data=question_data)
        if question_serializer.is_valid():
            question_serializer.save()
            return JsonResponse("Updated Successfully !!", safe=False)
        return JsonResponse("Failed to Update", safe=False)

    elif request.method=='DELETE':
        question=Question.objects.get(id=id)
        question.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def contactusApi(request,id=0):
    if request.method=='GET':
        contacts = ContactUs.objects.all()
        contacts_serializer = ContactUsSerializer(contacts, many=True)
        return JsonResponse(contacts_serializer.data, safe=False)
    
    elif request.method=='POST':
        contact_data=JSONParser().parse(request)
        contact_serializer = ContactUsSerializer(data=contact_data)
        if contact_serializer.is_valid():
            contact_serializer.save()
            return JsonResponse("Added SuccessFully!!", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    
    elif request.method == 'PUT':
        contact_data = JSONParser().parse(request)
        contact=ContactUs.objects.get(id=contact_data['id'])
        contact_serializer=ContactUsSerializer(contact, data=contact_data)
        if contact_serializer.is_valid():
            contact_serializer.save()
            return JsonResponse("Updated Successfully !!", safe=False)
        return JsonResponse("Failed to Update", safe=False)

    elif request.method=='DELETE':
        contact=ContactUs.objects.get(id=id)
        contact.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def reviewApi(request,id=0):
    if request.method=='GET':
        reviews = Review.objects.all()
        reviews_serializer = ReviewSerializer(reviews, many=True)
        return JsonResponse(reviews_serializer.data, safe=False)
    
    elif request.method=='POST':
        review_data=JSONParser().parse(request)
        review_serializer = ReviewSerializer(data=review_data)
        if review_serializer.is_valid():
            review_serializer.save()
            return JsonResponse("Added SuccessFully!!", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    
    elif request.method == 'PUT':
        review_data = JSONParser().parse(request)
        review=Review.objects.get(id=review_data['id'])
        review_serializer=ReviewSerializer(review, data=review_data)
        if review_serializer.is_valid():
            review_serializer.save()
            return JsonResponse("Updated Successfully !!", safe=False)
        return JsonResponse("Failed to Update", safe=False)

    elif request.method=='DELETE':
        review=Review.objects.get(id=id)
        review.delete()
        return JsonResponse("Deleted Successfully", safe=False)