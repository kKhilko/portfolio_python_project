from random import randrange

from model.group import Group


def test_group_modify_name(app):
    if app.group.count() == 0:
        app.group.create_new(Group(name="test"))
    old_group = app.group.get_list()
    index = randrange(len(old_group))
    group = Group(name="New group")
    group.id = old_group[index].id
    app.group.modify_by_index(index, group)
    assert len(old_group) == app.group.count()
    new_group = app.group.get_list()
    old_group[index] = group
    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)


def test_group_modify_header(app):
    if app.group.count() == 0:
        app.group.create_new(Group(name="test"))
    old_group = app.group.get_list()
    index = randrange(len(old_group))
    app.group.modify_by_index(index, Group(header="New group header"))
    assert len(old_group) == app.group.count()


#
# def test_group_modify_footer(app):
#     if app.group.count() == 0:
#         app.group.create_new(Group(name="test"))
#     old_group = app.group.get_list()
#     app.group.modify_first(Group(footer="New group footer"))
#     new_group = app.group.get_list()
#     assert len(old_group) == len(new_group)
