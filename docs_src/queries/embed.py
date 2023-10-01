import mongoz

database_uri = "mongodb://localhost:27017"
registry = mongoz.Registry(database_uri)


class UserType(mongoz.EmbeddedDocument):
    level: str = mongoz.String()


class User(mongoz.Document):
    is_active: bool = mongoz.Boolean(default=True)
    first_name: str = mongoz.String(max_length=50)
    last_name: str = mongoz.String(max_length=50)
    email: str = mongoz.Email(max_lengh=100)
    password: str = mongoz.String(max_length=1000)
    user_type: UserType = mongoz.Embed(UserType)

    class Meta:
        registry = registry
        database = "my_db"
