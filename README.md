# music_festival
Учебный проект - портал музыкального фестиваля

На самом деле - это заготовка для любого события с автоматизированным сбором и обработкой заявок на участие и распределение по N-тайслотов в M-локациях.

БОльшая часть текстового наполнения пишется в Markdown через стандартные формы.

#ToDo
##Приложения
- info
- committee
- timetable
- blog

###info
Отображение следующей информации:
- общая информация о событии
- список подтвержденных участников
 - детальная информация о участниках
 - время и место выступления (выступлений)
- список локаций для выступлений
- галерея
- блог
- способы добраться
- контакты

###committee
Работа программного комитета.
Два группы учетных записей.
Открытая для самостоятельной регистрации участников. Закрытая членов ПК.
1 Участники самостоятельно подают заявки
2 ПК голосует
3 по результатам голосования заявка принимается или отклоняется (поднимается флаг в списке заявок)

###timetable
Есть две исходные таблицы:
- список подтвержденных участников
- список локаций для выступлений

Формируется таблица таймслотов

По согласованию с участником (принятая заявка) выделяется таймслот.
В этот момент участник попадает в список подтвержденных участников приложения info. На всякий случай это разные базы.

###blog
Новости, заметки, свежие участники и прочее.
Заполняется программным комитетом и прочими PRщиками.