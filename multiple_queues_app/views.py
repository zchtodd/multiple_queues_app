from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .tasks import fibonacci, nth_prime


@csrf_exempt
def calculate_fibonacci(request):
    if request.method == "POST":
        try:
            N = int(request.POST.get("N"))
            result = fibonacci.delay(N)
            return JsonResponse(
                {"task_id": result.task_id, "status": "Task submitted successfully!"},
                status=200,
            )
        except ValueError:
            return JsonResponse({"error": "Invalid N value provided."}, status=400)
    else:
        return JsonResponse({"error": "Only POST method is allowed."}, status=405)


@csrf_exempt
def calculate_prime(request):
    if request.method == "POST":
        try:
            N = int(request.POST.get("N"))
            result = nth_prime.delay(N)
            return JsonResponse(
                {"task_id": result.task_id, "status": "Task submitted successfully!"},
                status=200,
            )
        except ValueError:
            return JsonResponse({"error": "Invalid N value provided."}, status=400)
    else:
        return JsonResponse({"error": "Only POST method is allowed."}, status=405)
