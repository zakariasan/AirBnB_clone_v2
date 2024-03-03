from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import Base

classes = {'State': 'State', 'City': 'City',
           'User': 'User', 'Place': 'Place',
           'Review': 'Review', 'Amenity': 'Amenity'}
user = getenv("HBNB_MYSQL_USER")
passwd = getenv("HBNB_MYSQL_PWD")
db = getenv("HBNB_MYSQL_DB")
host = getenv("HBNB_MYSQL_HOST")
env = getenv("HBNB_ENV")


class DBStorage:
    """Connect and create tables"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of __object__"""
        from models.state import State
        from models.city import City
        from models.user import User
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity

        objects = {}
        if cls:
            if isinstance(cls, str) and cls in classes:
                cls = classes[cls]
            if cls in classes.values():
                query_result = self.__session.query(cls).all()
                for obj in query_result:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    objects[key] = obj
        else:
            for class_name, class_obj in classes.items():
                query_result = self.__session.query(class_obj).all()
                for obj in query_result:
                    key = f"{class_name}.{obj.id}"
                    objects[key] = obj
        return objects

    def new(self, obj):
        """Add an object to the current database"""
        self.__session.add(obj)

    def save(self):
        """Commit the changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete an element in the table"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create a database session"""
        Base.metadata.create_all(self.__engine)
        session_p = sessionmaker(bind=self.__engine,
                                 expire_on_commit=False)
        self.__session = scoped_session(session_p)

    def close(self):
        """ remove() method on the private session attribute"""
        self.__session.close()
