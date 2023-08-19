# Тестовое задание для Hammer System
# Реализация взаимодействия по API для регистрации и входа в профиль

## Описание

Данная реализация позволяет пользователям зарегистрироваться на сайте, используя номер телефона. При успешной регистрации пользователю будет сгенерирован инвайт код.

## Требования

- Python 3.x
- Django
- Postgres SQL

## Установка

1. Склонируйте репозиторий:

```shell
git clone https://github.com/yourusername/yourproject.git
```

2. Создайте базу данных в Postgres SQL:

```shell
createdb yourdb
```

4. Настройте настройки базы данных в файле `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'yourdb',
        'USER': 'youruser',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

5. Выполните миграции:

```shell
python manage.py migrate
```

## Использование

1. Запустите сервер:

```shell
python manage.py runserver
```

2. Откройте браузер и перейдите по адресу `http://localhost:8000`.

3. На главной странице будет отображена форма для ввода телефона. Введите свой телефон и нажмите кнопку "Зарегистрироваться".

4. При успешной регистрации вам будет сгенерирован инвайт код. Сохраните его, так как он потребуется для входа в профиль.

5. Имитируйте отправку кода на указанный номер.

6. Перейдите на страницу входа и введите полученный код в соответствующее поле.

7. После успешной авторизации вы будете перенаправлены на свой профиль.

## API views.py
Так проиходит регистрация пользователя и проверка на то, существует ли он в базе данных
```
def register(request):
    if request.method == 'POST':
        person=Enter()
        form=UserRegisterForm(request.POST)
        person.inv_code=gener_inv_code()
        person.phone_number=request.POST.get("phone_number")
        if form.is_valid():
            person.save()
        return redirect('code-enter')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
```
Иммитация ввода кода
```
def code(request):
    if request.method == 'POST':
        
        form = UserCodeForm(request.POST)
        
        return redirect('profile')
    else:
        print(request.GET)
        form = UserCodeForm()
    return render(request, 'code.html', {'form': form})
```
Переход на профиль и ввод инвайт кода
```
def profile(request):
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile') 
    else:
        form = UserProfileForm()
    
    context = {'form': form}
    return render(request, 'profile.html', context)
```
