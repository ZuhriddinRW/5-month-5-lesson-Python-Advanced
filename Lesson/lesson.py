# Database, Socket, File, -> ochilganidan keyin yopilishi kerak bo'lgan block lar
# from contextlib import contextmanager
#
# @contextmanager
# def file_manager(file_name, mode):
#     f = None
#     try:
#         if "." not in file_name:
#             raise NameError
#         print(f"File '{file_name}' is opening....")
#         f = open(file_name, mode)
#         yield f
#     finally:
#         if f:
#             print(f"File '{file_name}' is closing...")
#             f.close()
#
# with file_manager('text.txt', 'r') as file:
#     # f = file.write("adasdasdasdasd")
#     f = file.read()
#     print(f)



# Instance and Static method
# class MyClass:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def return_name(self):
#         print(f"Hello, {self.surname} {self.name}")
#
#     @staticmethod
#     def summary(a, b):
#         return a + b
#
# info = MyClass('Zuhriddin', 'Shodmonov')
#
# info.return_name()
# print(info.summary(1, 10))

# import asyncio
# import time
#
# async def function1():
#     print('First function started')
#     await asyncio.sleep(2)
#     print('First function ended')
#
# async def function2():
#     print('Second function started')
#     await asyncio.sleep(5)
#     print('Second function ended')
#
# async def main():
#     await asyncio.gather(function1(), function2())
#
# asyncio.run(main())

# Decorator functon

def my_decorator(func):
    def my_function(*args, **kwargs):
        print('Zuhriddin')
        func(*args, **kwargs)
        print('Shodmonov')
    return my_function

@my_decorator
def summary(a, b):
    print(a + b)

summary(1, 10)





















