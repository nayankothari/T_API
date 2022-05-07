from requests import Response
from rest_framework.views import APIView
from api.models import *
from api.serializers import RPSSerializer, DPSSerializer, CustomerSerializer, RPSSerializerTxn, DPSSerializerTxn
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated


class RewardDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        if request.GET.get("office"):
            rps = RewardPointSystem.objects.filter(office=request.GET.get("office"),
                                                   branch=request.GET.get("branch"),
                                                   mobile_number=request.GET.get("mobile_number"))
            serializer = RPSSerializer(rps, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse({"msg": "no data in this range"}, status=400)



class SaveRewardDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = RPSSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.data, status=400)



class SaveDiscountDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = DPSSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)



class RewardStatusView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        response = {}
        try:
            office = request.GET.get("office")
            mobile_number = request.GET.get("mobile_number")
            points_from_rps = RewardPointSystem.objects.filter(office=office,
                                                        mobile_number=mobile_number).values_list('points', flat=True)
            points_from_dps = DiscountPointSystem.objects.filter(office=office,
                              mobile_number=mobile_number).values_list('points', flat=True)

            data = round(float(sum(points_from_rps) - sum(points_from_dps)), 3)
            response.update({"data": data})
        except Exception as e:
            response.update({"error": e})
            return JsonResponse(response, status=400)
        return JsonResponse(response, status=200)


class RewardStatusForOfficeAndCard(APIView):
    permission_classes = (IsAuthenticated,)
    '''
        filter data based on office and card number
    '''
    def get(self, request):
        response = {}
        try:
            office = request.GET.get("office")
            card_number = request.GET.get("card_number")
            points_from_rps = RewardPointSystem.objects.filter(office=office,
                                                               card_number=card_number).values_list('points', flat=True)
            points_from_dps = DiscountPointSystem.objects.filter(office=office,
                              card_number=card_number).values_list('points', flat=True)

            data = round(float(sum(points_from_rps) - sum(points_from_dps)), 3)
            response.update({"data": data})
        except Exception as e:
            response.update({"error": e})
            return JsonResponse(response, status=400)
        return JsonResponse(response, status=200)



class UpdateRewardDetail(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            office = request.POST.get("office")
            branch = request.POST.get("branch")
            bill_number = request.POST.get("bill_number")
            obj = RewardPointSystem.objects.get(office=office,
                                                branch=branch,
                                                bill_number=bill_number)
            serializer = RPSSerializer(obj,data=request.POST)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)
            return JsonResponse(serializer.errors, status=400)
        except:
            return JsonResponse({"data":"Bill not found"}, status=405)


class UpdateDiscountDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            office = request.POST.get("office")
            branch = request.POST.get("branch")
            bill_number = request.POST.get("bill_number")
            obj = DiscountPointSystem.objects.get(office=office,
                                                branch=branch,
                                                bill_number=bill_number)
            serializer = DPSSerializer(obj, data=request.POST)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)
            return JsonResponse(serializer.errors, status=400)
        except:
            return JsonResponse({"data":"Bill not found"}, status=405)

class CustomerDetailAPI(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        serializer = CustomerSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.data, status=400)



class CustomerDetail_Office_Mobile(APIView):
    permission_classes = (IsAuthenticated,)
    ''' 
       filter data based on office and mobile number
    '''
    def get(self, request):
        if request.GET.get("office"):
            cs = CustomerDetails.objects.filter(office=request.GET.get("office"),
                                                number=request.GET.get("number"))
            serializer = CustomerSerializer(cs, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse({"msg": "no data in this range"}, status=400)


class CustomerDetail_Office_Card(APIView):
    permission_classes = (IsAuthenticated,)
    ''' 
            filter data based on office and card number
        '''

    def get(self, request):
        if request.GET.get("office"):
            cs = CustomerDetails.objects.filter(office=request.GET.get("office"),
                                                card_number=request.GET.get("card_number"))
            serializer = CustomerSerializer(cs, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse({"msg": "no data in this range"}, status=400)


class CustomerDetail_Office_Mobile_Card(APIView):
    permission_classes = (IsAuthenticated,)
    ''' 
        filter data based on office, mobile and card number
    '''

    def get(self, request):
        if request.GET.get("office"):
            cs = CustomerDetails.objects.filter(office=request.GET.get("office"),
                                                number=request.GET.get("number"),
                                                card_number=request.GET.get("card_number"))
            serializer = CustomerSerializer(cs, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse({"msg": "no data in this range"}, status=400)


class CustomerDetailUpdate(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        office = request.POST.get("office")
        number = request.POST.get("old_number")
        try:
            obj = CustomerDetails.objects.get(office=office, number=number)
            serializer = CustomerSerializer(obj, data=request.POST, partial=True)
            if serializer.is_valid():
                serializer.save()
            try:
                filtered_result_rps = RewardPointSystem.objects.filter(office=office, mobile_number=number)
                for i in filtered_result_rps:
                    serializer2 = RPSSerializer(i, data=request.POST, partial=True)
                    if serializer2.is_valid():
                        serializer2.save()
                try:
                    filtered_result_dps = DiscountPointSystem.objects.filter(office=office, mobile_number=number)
                    for result in filtered_result_dps:
                        serializer3 = DPSSerializer(result, data=request.POST, partial=True)
                        if serializer3.is_valid():
                            serializer3.save()
                    return JsonResponse(serializer.data, status=200)
                except Exception:
                    return JsonResponse(serializer.data, status=200)
            except Exception:
                return JsonResponse(serializer.data, status=200)
        except Exception:
            pass
        return JsonResponse({"msg": "Data not update on server. try again !"}, status=400)



class CustomerRewardTransactions(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        response = {}
        try:
            office = request.GET.get("office")
            mobile_number = request.GET.get("mobile_number")
            points_from_rps = RewardPointSystem.objects.filter(office=office,
                                                        mobile_number=mobile_number)
            points_from_dps = DiscountPointSystem.objects.filter(office=office,
                              mobile_number=mobile_number)
            serializer = RPSSerializerTxn(points_from_rps, many=True)
            serializer1 = DPSSerializerTxn(points_from_dps, many=True)
            data= {"RPS": serializer.data, "RDS": serializer1.data}
            response.update({"data": data})
        except Exception as e:
            response.update({"error": e})
            return JsonResponse(response, status=400)
        return JsonResponse(response, status=200)


class CustomerRewardTransactionsByCard(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        response = {}
        try:
            office = request.GET.get("office")
            card_number = request.GET.get("card_number")
            points_from_rps = RewardPointSystem.objects.filter(office=office,
                                                        card_number=card_number)
            points_from_dps = DiscountPointSystem.objects.filter(office=office,
                              card_number=card_number)
            serializer = RPSSerializerTxn(points_from_rps, many=True)
            serializer1 = DPSSerializerTxn(points_from_dps, many=True)
            data= {"RPS": serializer.data, "RDS": serializer1.data}
            response.update({"data": data})
        except Exception as e:
            response.update({"error": e})
            return JsonResponse(response, status=400)
        return JsonResponse(response, status=200)
