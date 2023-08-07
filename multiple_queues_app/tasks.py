from celery import shared_task


@shared_task(queue="fibonacci")
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


@shared_task(queue="prime")
def nth_prime(n):
    count = 0
    num = 1

    while count < n:
        num += 1
        if num < 2:
            continue
        if any(num % i == 0 for i in range(2, int(num**0.5) + 1)):
            continue
        count += 1

    return num
