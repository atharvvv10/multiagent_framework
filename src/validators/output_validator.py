class OutputValidator:
    @staticmethod
    def validate(data, schema):
        return schema(**data)
