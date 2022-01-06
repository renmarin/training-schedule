import graphene
from graphene_django import DjangoObjectType

from django.contrib.auth.models import User
from training_schedule.models import Schedule

from django.core.exceptions import ObjectDoesNotExist


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "username", "schedules")


class ScheduleType(DjangoObjectType):
    class Meta:
        model = Schedule
        fields = ("id", "user", "name", "date", "time")


class Query(graphene.ObjectType):
    schedule_by_id = graphene.List(ScheduleType, id=graphene.ID(required=False))
    schedules = graphene.List(
        ScheduleType,
        start_date=graphene.String(required=False),
        end_date=graphene.String(required=False),
        start_time=graphene.String(required=False),
        end_time=graphene.String(required=False)
    )

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

    def resolve_schedule_by_id(root, info, id=None):
        # show all schedules if no id given
        if not id:
            return Schedule.objects.all()
        try:
            return Schedule.objects.filter(id=id).all()
        except ObjectDoesNotExist:
            return None
        except ValueError:
            return Schedule.objects.all()

schema = graphene.Schema(query=Query)
