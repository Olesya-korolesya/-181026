from django.shortcuts import render

# Задание1
# def user_index(request):
#     context = {
#     'user_name': 'Руслан'
#     }
#     return render(request, 'index.html', context)

#Задание2
# def user_index(request):
#
#     context = {
#         'name': 'Павел',
#         'age': 45,
#         'phone': '+79234567891',
#         'email': 'pavel@pavel.com',
#     }
#
#     return render(request, 'index.html', context)

#Задание 3

# def user_index(request):
#
#     profile_data = {
#         'name': 'Павел',
#         'age': 45,
#         'phone': '+79234567891',
#         'email': 'pavel@pavel.com'
#     }
#     return render(request, 'index.html', {'profile_data': profile_data})

# Задание 4

# def user_index(request):
#
#     profile_data = ['Павел', 45, '+79234567891', 'pavel@pavel.com']
#
#     return render(request, 'index.html', {'profile_data': profile_data})

#Задание 5

# from django.utils import timezone
#
# def user_index(request):
#
#     current_datetime = timezone.now()
#
#     context = {
#         'current_time': current_datetime,
#     }
#     return render(request, 'index.html', context)

#Задание 6

#
# def user_index(request):
#     context = {
#         'employees': [
#             {'name': 'Алексей', 'experience': 5},
#             {'name': 'Павел', 'experience': 3},
#         ]
#     }
#     return render(request, 'index.html', context)

#Задание 7

# def user_index(request):
#
#     user_list = ['Игорь', 'Андрей', 'Дмитрий', 'Алексей', 'Николай', 'Евгений', 'Иван', 'Павел', 'Руслан', 'Денис']
#
#     return render(request, 'index.html', {'user_list': user_list})

#Задание 8

# def user_index(request):
#
#     user_list = [{'name': 'Дмитрий', 'experience': 9},
#
#              {'name': 'Павел',   'experience': 5},
#
#              {'name': 'Алексей', 'experience': 3},
#
#              {'name': 'Иван',    'experience': 0},
#
#              {'name': 'Денис',   'experience': 2},
#
#              {'name': 'Игорь',   'experience': 7},
#
#              {'name': 'Руслан',  'experience': 1},
#
#              {'name': 'Евгений', 'experience': 4},
#
#              {'name': 'Андрей',  'experience': 2},
#
#              {'name': 'Николай', 'experience': 8}]
#
#     return render(request, 'index.html', {'user_list': user_list})

#Задание 9

# def user_index(request):
#
#     employees_list = [{'name': 'Дмитрий', 'experience': 9},
#
#              {'name': 'Павел',   'experience': 5},
#
#              {'name': 'Алексей', 'experience': 3},
#
#              {'name': 'Иван',    'experience': 0},
#
#              {'name': 'Денис',   'experience': 2},
#
#              {'name': 'Игорь',   'experience': 7},
#
#              {'name': 'Руслан',  'experience': 1},
#
#              {'name': 'Евгений', 'experience': 4},
#
#              {'name': 'Андрей',  'experience': 2},
#
#              {'name': 'Николай', 'experience': 8}]
#
#     return render(request, 'index.html', {'user_list': employees_list})

#Задание 10

# def user_index(request):
#
#     employees_list = [{'name': 'Дмитрий', 'experience': 9},
#
#              {'name': 'Павел',   'experience': 5},
#
#              {'name': 'Алексей', 'experience': 3},
#
#              {'name': 'Иван',    'experience': 0},
#
#              {'name': 'Денис',   'experience': 2},
#
#              {'name': 'Игорь',   'experience': 7},
#
#              {'name': 'Руслан',  'experience': 1},
#
#              {'name': 'Евгений', 'experience': 4},
#
#              {'name': 'Андрей',  'experience': 2},
#
#              {'name': 'Николай', 'experience': 8}]
#
#     return render(request, 'index.html', {'user_list': employees_list})
#
