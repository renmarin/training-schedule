import graphene
from graphene_django import DjangoObjectType

from django.contrib.auth.models import User
from training_schedule.models import Schedule

from django.core.exceptions import ObjectDoesNotExist

# Для опциональной возможности искать тренировки по  пользователям
class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "username", "schedules")


class ScheduleType(DjangoObjectType):
    class Meta:
        model = Schedule
        fields = ("id", "user", "name", "date", "time")


class Query(graphene.ObjectType):
    schedules = graphene.List(
        ScheduleType,
        start_date=graphene.String(required=False),
        end_date=graphene.String(required=False),
        start_time=graphene.String(required=False),
        end_time=graphene.String(required=False)
    )
    detail_by_id = graphene.Field(ScheduleType, id=graphene.ID(required=True))
    user_by_id = graphene.Field(UserType, id=graphene.ID(required=True))

    # Возвращает список расписание тренировок в пределах заданных параметров
    # При отсутствии или ошибке возвращает расписание всех тренировок
    # Сортировано по дате и времени
    def resolve_schedules(
            root, info,
            start_date="1970-01-01", end_date="2100-12-31",
            start_time="00:00:00", end_time="23:59:59"
    ):
        try:
            return Schedule.objects.filter(
                date__gte=start_date, date__lte=end_date,
                time__gte=start_time, time__lte=end_time
            ).order_by('date', 'time').all()
        except ObjectDoesNotExist:
            return None
        except ValueError:
            return Schedule.objects.order_by('date', 'time').all()

    # Возвращает детали тренировки по ID
    def resolve_detail_by_id(root, info, id):
        try:
            return Schedule.objects.get(id=id)
        except ObjectDoesNotExist:
            return None

    # Возвращает детали тренировок пользователя по ID.
    def resolve_user_by_id(self, info, id):
        try:
            return User.objects.get(id=id)
        except ObjectDoesNotExist:
            return None

schema = graphene.Schema(query=Query)
