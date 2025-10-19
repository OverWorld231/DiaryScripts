from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Commendation
import random

example_commendation = [
    "Молодец!",
    "Отлично!",
    "Ты меня порадовал!",
    "Здорово",
    "Гораздо лучше, чем я ожидал!",
    "Ты меня приятно удивил!",
    "Великолепно!",
    "Прекрасно!",
    "Ты меня очень обрадовал!",
    "Очень хороший ответ",
    "Талантливо!",
]


def fix_marks(schoolkid):
    Mark.objects.filter(schoolkid=schoolkid, points__lt=4).update(points=5)


def remove_chastisement(schoolkid):
    Chastisement.objects.filter(schoolkid=schoolkid).delete()


def create_commendation(schoolkid, subject, commendation):
    lessons_student = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject__title__contains=subject,
    ).order_by("-date")
    lesson_student = lessons_student.first()
    Commendation.objects.create(
        text=commendation,
        created=lesson_student.date,
        schoolkid=schoolkid,
        subject=lesson_student.subject,
        teacher=lesson_student.teacher,
    )


def main():
    full_name = input("Введите полностью ФИО ученика: ")
    schoolkid = Schoolkid.objects.get(full_name__contains=full_name)
    commendation = random.choice(example_commendation)
    subject = input("Введите предмет: ")
    remove_chastisement(schoolkid)
    fix_marks(schoolkid)
    create_commendation(schoolkid, subject, commendation)


if __name__ == "__main__":
    main()
