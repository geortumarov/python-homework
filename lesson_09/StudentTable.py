from sqlalchemy import create_engine, text


class StudentTable:
    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def create_student(self, user_id, level, education_form, subject_id=1):
        with self.__db.connect() as conn:
            conn.execute(
                text("""
                    INSERT INTO student(
                     user_id, level, education_form, subject_id)
                    VALUES (:user_id, :level, :education_form, :subject_id)
                """),
                {
                    "user_id": user_id,
                    "level": level,
                    "education_form": education_form,
                    "subject_id": subject_id
                }
            )
            conn.commit()

    def get_student(self, user_id, subject_id=1):
        with self.__db.connect() as conn:
            result = conn.execute(
                text("SELECT * FROM student "
                     "WHERE user_id = :user_id "
                     "AND subject_id = :subject_id"),
                {"user_id": user_id, "subject_id": subject_id}
            )
            return result.mappings().first()

    def update_student(self, user_id, new_level,
                       new_education_form, subject_id=1):
        with self.__db.connect() as conn:
            conn.execute(
                text("""
                    UPDATE student
                    SET level = :level, education_form = :education_form
                    WHERE user_id = :user_id AND subject_id = :subject_id
                """),
                {
                    "user_id": user_id,
                    "level": new_level,
                    "education_form": new_education_form,
                    "subject_id": subject_id
                }
            )
            conn.commit()

    def delete_student(self, user_id, subject_id=1):
        with self.__db.connect() as conn:
            conn.execute(
                text("DELETE FROM student "
                     "WHERE user_id = :user_id AND subject_id = :subject_id"),
                {"user_id": user_id, "subject_id": subject_id}
            )
            conn.commit()

    def get_next_user_id(self):
        with self.__db.connect() as conn:
            result = conn.execute(text("SELECT MAX(user_id) FROM student"))
            max_id = result.scalar()
            return (max_id or 0) + 1
