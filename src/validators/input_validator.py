class InputValidator:
    @staticmethod
    def validate(data, schema):
        return schema(**data)
