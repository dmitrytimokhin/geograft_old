# Телеграм бот ProdGgBot для компании GeoGraft.

---

### Репозиторий создан для публикации финального кода проекта:
* Суммаризация информации с сайта;
* Создание базы данных на основе SQLAlchemy;
* Регистрация пользователей;
* Мониторинг доступности времени и запись пользователей на прием;
* Применение обученных нейросетевых моделей.

---
#### Детализация проекта:
1. С сайта взята слудющая информация:
   
   1.1. Описание услуг и цен;
   
   1.2. Результаты после операций по пересадке волос;
   
   1.3. Рекоммендаци до и после операционного периода;
   
   1.4. Контакты;

2. Реализовано создание следующих таблиц:
   
   2.1. Клиенты -  хранится мета-информация при регистрации пользователя;
   
   2.2. Услуги - хранится мета-информация об услугах и их стоимости;
   
   2.3. Филиалы - хранится мета-информация об доступных филиалах клиники;
   
   2.4. Запись - хранится информация между таблицами "Клиенты"-"Услуги"-"Филиалы", заполняется при записи на услугу;
   
   2.5. Отмена - хранится информация об отмене записей, связана с талицей "Запись";
   
   2.6. Оплата - хранится информация об оплате оказанных услуг.

3. При стартовой команде бот запрашивает мета-информацию о пользователе и записывает ее в таблицу "Клиенты":
   
   3.1. Дополняется информацией при записи на консультацию/операцию по пересадке волос - создание папки клиента, и хранение его фотографий головы, анализов.

4. При записи клиента анализируются доступные окна на ближайшие два месяца, клиент сам в праве выбрать необходимую дату и время;
   
   4.1. У каждого филиала свое количество процедурных кабинетов;
   
   4.2. Запись на операцию для филиала доступна 2 единицы на кабинет в день (10:00; 16:00);
   
   4.3. Запись на процедуру ПРП возможна каждые 30 минут на филиал;
   
   4.4. Запись пациента на операцию возможна при наличие всех анализов;

5. Дообучение и применение трёх нейросетевых моделей:
    
   5.1. Обучение модели YOLOv5 для детекции макушки головы. Необходима для детекции и обрезки фотографии, присылаемой пользователем на экспресс-тест степени алопеции;
   
   5.2. Обучение и применение YOLOv5 для классификации степени алопеции. Необходима для определения уровня облысения пациента по шкале Норвуда и количества операций и графтов;
   
     5.2.1. Итоговый текст генерируется на основе GPT модели, в промт которой задается степень облысения полученная в предыдущем пункте;
   
   5.3. Обучение и применение YOLOv5 для детекции и классификации формы лица. Необходима для подбора современных причесок, подходящих под тип лица пациента;
   
     5.2.1. Итоговый текст генерируется на основе GPT модели, в промт которой задается форма лица полученная в предыдущем пункте.
