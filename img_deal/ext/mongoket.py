# coding: utf8


class Document(dict):
    def __init__(self, *args, **kwargs):
        super(Document, self).__init__()

        if "mongoket_collection" in kwargs:
            mongoket_collection = kwargs["mongoket_collection"]
            del kwargs["mongoket_collection"]
            self.mongoket_collection = mongoket_collection
        self.update(**kwargs)

    def save(self, force=False, **kwargs):
        return self.mongoket_collection.collection.save(self, **kwargs)


class Collection(object):
    document_class = Document
    default_values = {}
    structure = None

    def __init__(self, collection=None):
        self.collection = collection
        self.database = collection.database
        self.client = self.database.client

    def __call__(self, *args, **kwargs):
        """ Instanciates a new *Document* from this collection """
        kwargs["mongoket_collection"] = self
        instance = self.document_class(*args, **kwargs)
        if hasattr(self, "default_values") and self.default_values:
            for k, v in self.default_values.items():
                new_v = v() if callable(v) else v
                if k not in instance:
                    instance[k] = new_v
        return instance

    def __getattr__(self, attr):
        if hasattr(self.collection, attr):
            return getattr(self.collection, attr)
