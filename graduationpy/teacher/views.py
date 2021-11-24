import json
import pymysql

from teacher.service import excel
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from teacher.models import Quote


@csrf_exempt
def test_interface(request):
    content = dict()
    content['isOk'] = 'ok'
    data = json.dumps(content)
    return HttpResponse(content=data, content_type='application/json')


def execute_excel(request):
    global result
    db = pymysql.connect("localhost", "root", "root", "graduation", 8086)

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = "select studentNumber,clockInProject,clockTime,clockState,errorReason from studentclockin " \
          "where clockInTeacherNumber='001'"

    try:
        cursor.execute(sql)
        result = cursor.fetchall()

    except Exception:
        print("出现异常")

    teacher = request.GET.get("teacher", None)
    major = request.GET.get("major", None)
    project = request.GET.get("project", None)

    print(teacher, major, project)

    excel.execute_excel(result)

    return HttpResponse(json.dumps({'isOk': 'ok'}))
