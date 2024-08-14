def tests_function():
    x = 1
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

inner_function()
# выдает ошибку NameError: name 'inner_function' is not defined. Did you mean: 'tests_function'?

