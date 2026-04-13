from StudentTable import StudentTable

db_connection_string = "postgresql://postgres:свой пароль@localhost:5432/Geor"


def test_create_student():
    db = StudentTable(db_connection_string)
    new_id = db.get_next_user_id()

    db.create_student(
        user_id=new_id,
        level="Beginner",
        education_form="personal",
        subject_id=1
    )

    student = db.get_student(new_id)
    assert student is not None
    assert student["user_id"] == new_id
    assert student["level"] == "Beginner"
    assert student["education_form"] == "personal"
    db.delete_student(new_id)


def test_update_student():
    db = StudentTable(db_connection_string)
    new_id = db.get_next_user_id()
    db.create_student(
        user_id=new_id,
        level="Elementary",
        education_form="group",
        subject_id=1
    )
    db.update_student(
        user_id=new_id,
        new_level="Advanced",
        new_education_form="personal"
    )
    updated = db.get_student(new_id)
    assert updated["level"] == "Advanced"
    assert updated["education_form"] == "personal"
    db.delete_student(new_id)


def test_delete_student():
    db = StudentTable(db_connection_string)
    new_id = db.get_next_user_id()
    db.create_student(
        user_id=new_id,
        level="Pre-Intermediate",
        education_form="group",
        subject_id=1
    )
    assert db.get_student(new_id) is not None
    db.delete_student(new_id)
    assert db.get_student(new_id) is None
