class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return f'<{self.__class__.__name__}:{self.name}>'


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModeMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print(f'Found model: {name}')
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print(f'Found mapping: {k} => {v}')
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModeMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(f"'Model' object has no attribute '{key}'")

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = f"insert into {self.__table__}({', '.join(fields)}) values ({', '.join(params)})"
        print(f'SQL: {sql}')
        print(f'ARGS: {str(args)}')


class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


u = User(id=12345, name='Aurelius', email='test@orm.org', password='pwd')
u.save()
