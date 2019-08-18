from app.errors.exceptions import DatabaseException
from app.errors.http_errors import JsonDatabaseError,JsonValidateError
from app.web import web
from app.web.forms import ProjectAddForm
from app.web.models import ProjectInfo
from flask import render_template, request, abort, redirect, jsonify


@web.route('/list_projects')
def list_projects():
    # projects = ProjectInfo.all()
    page = request.args.get('page',1)
    paginate = ProjectInfo.paginate(page)
    projects = paginate.items
    return render_template('projects.html',projects=projects,paginate=paginate)

@web.route('/create_project',methods=['GET','POST'])
def create_project():

    # get 展示输入框
    if request.method == 'GET':
        form = ProjectAddForm()
        return render_template('project.html',form=form)
    # post
    form = ProjectAddForm(request.form)
    if form.validate():
        try:
            ProjectInfo.insert(form.data)
            return redirect('/list_projects')
        except DatabaseException as e:
            error_msg = '请求数据不合理'
            return render_template('project.html',form=form,error_msg=error_msg)


    return render_template('project.html',form=form)



@web.route('/edit_project/<int:p_id>')
def edit_project(p_id):
    project = ProjectInfo.query.get(int(p_id))
    if not project:
        return redirect('/list_projects')
    # get 展示输入框
    if request.method == 'GET':
        form = ProjectAddForm(obj=project)
        return render_template('project_edit.html',form=form)
    # post
    form = ProjectAddForm(request.form)
    if form.validate():
        try:
            project.update(form.data)
            return redirect('/list_projects')
        except DatabaseException as e:
            error_msg = '请求数据不合理'
            return render_template('project.html',form=form,error_msg=error_msg)


    return render_template('project.html',form=form)


@web.route('/delete_project',methods=['GET','POST'])
def delete_project():
    # 获取请求数据
    p_id = request.json.get('id','')
    # 验证：
    try:
        res = ProjectInfo.query.get(int(p_id))
        if res:
            pass
        raise JsonDatabaseError('没有这个项目')
        # return jsonify({'msg':'没有这个项目'})
    except:
        raise JsonValidateError("id 格式不正确")
        # return jsonify({'msg':'id格式不正确'})